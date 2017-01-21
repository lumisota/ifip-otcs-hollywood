#!/bin/bash

#add-apt-repository ppa:dreibh/ppa -y
#sudo apt-get update
#sudo apt-get install netperfmeter -y
#sudo add-apt-repository ppa:mc3man/trusty-media -y
#sudo apt-get update
#sudo apt-get install python-twisted python-twisted-bin python-twisted-core python-twisted-web gstreamer0.10-plugins-* gstreamer0.10-ffmpeg gstreamer0.10-tools python-gst0.1 libgstreamer0.10-dev python-scipy python-psutil -y
#sudo apt-get install build-essential libpcap-dev -y
#wget https://github.com/appneta/tcpreplay/releases/download/v4.1.2/tcpreplay-4.1.2.tar.gz
#tar -xvf tcpreplay-4.1.2.tar.gz
#cd tcpreplay-4.1.2
#./configure
#make
#sudo make install
#cd ..
sudo git clone https://github.com/ldecicco/tapas.git
git clone https://github.com/lumisota/hollywood-api.git
cd hollywood-api
make