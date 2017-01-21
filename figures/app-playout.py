import sys

if (len(sys.argv) != 2):
    exit("Usage: app-playout.py [client log]")

first_time = -1
c_map = {"Played": 14610650, "Expired": 5577355, "Undelivered": 15098113}
with open(sys.argv[1]) as log:
    log.readline()
    log.readline()
    for entry in log:
        entry = entry[:-1].split()
        time = float(entry[0][1:-1])
        if first_time == -1:
            first_time = time
        if entry[1] != "Received" and entry[1] != "Playout":
            print time-first_time, c_map[entry[1]]