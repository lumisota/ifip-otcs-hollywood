import sys
import math

receive_order = []
receive_time = {}
played = []
buckets = {}

with open(sys.argv[1]) as f:
    for line in f:
        split_line = line[:-1].split()
        #print split_line
        if split_line[1] == "Received":
            if split_line[3] not in receive_order:
                receive_order.append(int(split_line[3]))
                receive_time[int(split_line[3])] = float(split_line[0][1:-1])
        elif split_line[1] == "Played":
            played.append(int(split_line[2]))
           
largest_bucket = -1 
first_time = -1
for message in receive_order:
    if first_time == -1:
        first_time = receive_time[message]
    if message in played:
        message_time = receive_time[message]-first_time
        message_bucket = message_time/0.5
        message_bucket = int(math.ceil(message_bucket))
        if message_bucket == 0:
            message_bucket = 1
        if message_bucket-1 > largest_bucket:
            largest_bucket = message_bucket-1
        buckets[message_bucket-1] = buckets.get(message_bucket-1, 0) + 160
        #print message_time, message_bucket-1

if largest_bucket == -1:
    largest_bucket = 240
    
for i in range(largest_bucket+1):
    print (i+1)*0.5, buckets.get(i, 0) 
        