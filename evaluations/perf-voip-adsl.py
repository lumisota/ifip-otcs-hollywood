from mininet.topo import Topo
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.log import lg, info
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
import sys
import os.path
from subprocess import call
import time

dash_test_files = ["car-20120827-85.mp4", 
                   "car-20120827-86.mp4", 
                   "car-20120827-87.mp4", 
                   "car-20120827-88.mp4", 
                   "car-20120827-89.mp4", 
                   "car-20120827-8b.mp4", 
                   "car-20120827-8c.mp4", 
                   "car-20120827-8d.mp4", 
                   "car-20120827-manifest.mpd"]
     
class DumbbellTopo(Topo):
    def build(self, bw=8, delay="0ms"):
        delay = ""
        queue_size = 0
        if sys.argv[1].split('-')[2] == "uk":
            delay = "10ms"
            queue_size = 14
        elif sys.argv[1].split('-')[2] == "us":
            delay = "35ms"
            queue_size = 48
        print delay, queue_size
        switch1 = self.addSwitch('switch1')
        switch2 = self.addSwitch('switch2')
        appClient = self.addHost('aClient')
        appServer = self.addHost('aServer')
        crossClient = self.addHost('cClient')
        crossServer = self.addHost('cServer')
        self.addLink(appClient, switch1)
        self.addLink(crossClient, switch1)
        self.addLink(appServer, switch2)
        self.addLink(crossServer, switch2)
        self.addLink(switch1, switch2, bw=bw, delay=delay, max_queue_size=queue_size)

def hollywood():
    dumbbell = DumbbellTopo()
    network = Mininet(topo=dumbbell, host=CPULimitedHost, link=TCLink, autoPinCpus=True)
    network.start()
    dumpNodeConnections(network.hosts)
    network.pingAll()
    hollywood = 0
    
    crossClient = network.get('cClient')                
    crossServer = network.get('cServer')
    appClient = network.get('aClient')
    appServer = network.get('aServer')

    # disable offloading - when enabled, permits segments larger than 1500 bytes
    crossClient.cmd('ethtool -K ' + str(crossClient.intf()) + ' gso off')
    crossServer.cmd('ethtool -K ' + str(crossServer.intf()) + ' gso off')
    appClient.cmd('ethtool -K ' + str(appClient.intf()) + ' gso off')
    appServer.cmd('ethtool -K ' + str(appServer.intf()) + ' gso off')

    if sys.argv[1].split('-')[4] == "iii":
        for file_name in dash_test_files:
            if not os.path.isfile("/vagrant/evaluations/mpeg-dash-data/" + file_name):
                call(["wget", "-P", "/vagrant/evaluations/mpeg-dash-data/", "http://yt-dash-mse-test.commondatastorage.googleapis.com/media/" + file_name])

    if sys.argv[1].split('-')[5] == "tcph":
        hollywood = 1
    try:
        runName = 'perf-voip-adsl-' + sys.argv[1].split('-')[2] + '-pd' + sys.argv[1].split('-')[3][2:-2] + 'ms-' + sys.argv[1].split('-')[4] + '-' + sys.argv[1].split('-')[5]

        # cross traffic
        if sys.argv[1].split('-')[4] == "i":
            crossClient.cmd('netperfmeter 9000 > /vagrant/figures/data/' + runName + '.cclient-out &')
            crossServer.cmd('netperfmeter ' + crossClient.IP() + ':9000 -tcp const0:const1460:const0:const0 > /vagrant/figures/data/' + runName + '.cserver-out &')
        elif sys.argv[1].split('-')[4] == "ii":    
            crossServer.cmd('sudo python /vagrant/evaluations/http-server.py > /vagrant/figures/data/' + runName + '.cserver-out &')
            crossClient.cmd('sudo python /vagrant/evaluations/http-client.py ' + crossServer.IP() + '  > /vagrant/figures/data/' + runName + '.cclient-out &')
        elif sys.argv[1].split('-')[4] == "iii":    
            crossServer.cmd('cd /vagrant/evaluations/mpeg-dash-data; sudo python -m SimpleHTTPServer 80 > /vagrant/figures/data/' + runName + '.cserver-out &')
            crossClient.cmd('sudo python ~/tapas/play.py -u http://' + crossServer.IP() + '/car-20120827-manifest.mpd > /vagrant/figures/data/' + runName + '.cclient-out &')
        elif sys.argv[1].split('-')[4] == "iv":    
            crossClient.cmd('netperfmeter 9000 > /vagrant/figures/data/' + runName + '.cclient-out &')
            crossServer = crossServer.cmd('netperfmeter ' + crossClient.IP() + ':9000 -udp const900:const1472:const0:const0:onoff=0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170 > /vagrant/figures/data/' + runName + '.cserver-out &')

        # run receiver on client
        appClient.cmd('~/hollywood-api/receiver ' + str(hollywood) + ' ' + sys.argv[1].split('-')[3][2:-2] + ' > /vagrant/figures/data/' + runName + '.aclient-out & echo $! > receiver-pid')
        receiverPid = appClient.cmd('cat receiver-pid')
        print "receiver pid = ", receiverPid
        appClient.cmd('tcpdump -S port 8882 > /vagrant/figures/data/' + runName + '.aclient-tcpdump &')

        # run sender on server; take tcpdump to measure retransmissions
        appServer.cmd('tcpdump -S port 8882 > /vagrant/figures/data/' + runName + '.aserver-tcpdump &')
        appServer.cmd('~/hollywood-api/sender ' + appClient.IP() + ' ' + sys.argv[1].split('-')[3][2:-2] + ' ' + str(hollywood) + ' > /vagrant/figures/data/' + runName + '.aserver-out')

        appClient.cmd('wait', int(receiverPid))
        appClient.cmd('sudo cat /var/log/kern.log > /vagrant/figures/data/' + runName + '.aclient-kernlog')
    except Exception as e:
        print "Exception!"
        print e
    finally:
        network.stop()
        time.sleep(5)

if __name__ == '__main__':
    hollywood()
