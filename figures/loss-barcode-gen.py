import sys

if (len(sys.argv) != 2):
	exit("Usage: loss-barcode-gen.py [tcpdump file]")

sending_order = []
sending_time = []
segments = {}
ack_counts = {}

first_seq = 0

barcode = []

first_ts = -1
with open(sys.argv[1]) as tcpdump:
	for segment in tcpdump:
		segment = segment.split(",")
		segment = [element.strip() for element in segment]
		#print segment
		ts = segment[0].split()[0]
		ts = ts.split(':')
		#print ts
		ts_secs = float(ts[2]) + float(ts[1])*60 + float(ts[0])*60*60
		if first_ts == -1:
		    first_ts = ts_secs
		ts_offset = ts_secs-first_ts
		type, sequence_num = segment[1].split()
		seg_len = int(segment[-1].split()[1])
		if type == "seq":
			sequence_num = sequence_num.split(":")[0]
			sequence_num = int(sequence_num)
			if seg_len > 0:
				if first_seq == 0:
					first_seq = sequence_num+seg_len
				barcode.append(0)
				sending_order.append(sequence_num+seg_len)
				sending_time.append(ts_offset)
				segments[sequence_num+seg_len] = 0
		if type == "ack":
			sequence_num = int(sequence_num)
			ack_counts[sequence_num] = ack_counts.get(sequence_num, 0) + 1
			if ack_counts[sequence_num] == 5:
				# means that segment sent after this one was lost
				index_of_lost = len(sending_order) - sending_order[::-1].index(sequence_num)
				seq_of_lost = sending_order[index_of_lost]
				segments[seq_of_lost] = 1
			#print type, sequence_num, seg_len

#print segments
#print ack_counts
#print sending_order
i = 0
for seq in sending_order:
	print sending_time[i], segments[seq]
	i = i + 1