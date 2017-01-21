import sys

if (len(sys.argv) != 3):
    exit("Usage: loss-barcode-gen-recv.py [tcpdump file] [kernlog]")

init_time = -1

expected_seq = -1
unexpected_mode = False
mode_to_colour = {0: 14610650, 1: 5577355, 2: 15098113, 3: 65535}

incon_ts = []

tcp_seq = 0
replaced = []
with open(sys.argv[2]) as log:
    for line in log:
        if "Hollywood (PR): sending TCP segment" in line:
            tcp_seq = line[:-1].split()[-1][:-1]
        elif "replaced!" in line:
            if tcp_seq not in replaced:
                replaced.append(tcp_seq)
                
with open(sys.argv[1]) as tcpdump:
    for segment in tcpdump:
        segment = segment.split(",")
        segment = [element.strip() for element in segment]
        type, seq = segment[1].split()
        #print segment
        if type == "seq":
            length = int(segment[7].split()[1])
            if length == 0:
                continue
            seq, next_seq = seq.split(':')
            time = segment[0].split()[0].split(':')
            time = float(time[2]) + float(time[1])*60 + float(time[0])*3600
            length = int(segment[7].split()[1])
            if init_time == -1:
                init_time = time
            time = time - init_time
            mode = 0
            if expected_seq != -1 and seq != expected_seq:
                mode = 1
                unexpected_mode = True
            elif seq == expected_seq and unexpected_mode == True:
                mode = 2
                unexpected_mode = False
            expected_seq = next_seq
            if seq in replaced:
                    mode = 3
                    incon_ts.append(time)
            print time, seq, length, mode_to_colour[mode]

xtics_out_file = sys.argv[1].split(".")[0]

xtics_out = open(xtics_out_file + '-barcode.xtics', 'w+')
for incon in incon_ts:
    xtics_out.write("set xtics add (\"\" %f)\n" % (incon))
xtics_out.close()
