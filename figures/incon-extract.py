import sys

if (len(sys.argv) != 2):
    exit("Usage: incon-extract.py [kern log]")

first_time = -1
c_map = {"Played": 32768, "Expired": 16776960, "Undelivered": 16711680}
tcp_seq = 0
replaced = []
with open(sys.argv[1]) as log:
    for line in log:
        if "Hollywood (PR): sending TCP segment" in line:
            tcp_seq = int(line[:-1].split()[-1][:-1])
        elif "replaced!" in line:
            if tcp_seq not in replaced:
                replaced.append(tcp_seq)

for seq in replaced:
    print seq