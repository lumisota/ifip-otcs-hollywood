import sys
import math

received = []
messages = {}
buckets = {}

with open(sys.argv[1]) as f:
    for line in f:
        split_line = line[:-1].split()
        status = split_line[1]
        if status == "Received":
            message_num = int(split_line[3])
            if message_num not in messages:
                messages[message_num] = {"received": float(split_line[0][1:-1]), "played": False}
                received.append(message_num)
        elif status == "Played":
            message_num = int(split_line[2])
            messages[message_num]["played"] = True

largest_bucket = -1 
first_time = -1
for message in received:
    if first_time == -1:
        first_time = messages[message]["received"]
    if messages[message]["played"] == True:
        message_time = messages[message]["received"]-first_time
        message_bucket = message_time/0.5
        message_bucket = int(math.ceil(message_bucket))
        if message_bucket == 0:
            message_bucket = 1
        if message_bucket-1 > largest_bucket:
            largest_bucket = message_bucket-1
        buckets[message_bucket-1] = buckets.get(message_bucket-1, 0) + 160

if largest_bucket == -1:
    largest_bucket = 240

total = 0

for i in range(largest_bucket+1):
    print (i+1)*0.5, buckets.get(i, 0) 
    total += buckets.get(i, 0) 