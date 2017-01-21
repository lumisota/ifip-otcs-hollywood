import sys

i = 0

first_ts = -1

with open(sys.argv[1]) as f:
	for line in f:
		line = line[:-1].split()
		#print line
		if line[1] == "Received":
		    if first_ts == -1:
		        first_ts = float(line[0][1:-1])
		    print float(line[0][1:-1])-first_ts, float(line[5][:-1])*1000
			#if i not in message_times:
			#	message_times[i] = float(line[5][:-1])*1000
			#i = i + 1

#for i in range(6000):
#	print i, message_times.get(i, 0)