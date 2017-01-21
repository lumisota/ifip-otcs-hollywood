import datetime
import sys

received = []
goodput = {}

max_second = 0

with open(sys.argv[1]) as f:
    first_ts, first_msg = f.readline().split()
    first_ts = datetime.datetime.fromtimestamp(float(first_ts))
    first_msg = int(first_msg)
    playout_ts = first_ts + datetime.timedelta(milliseconds=50)
    #print first_ts
    #print playout_ts
    received.append(first_msg)
    goodput[0] = 160
    for line in f:
        ts, msg = line.split()
        ts = datetime.datetime.fromtimestamp(float(ts))
        try: 
            msg = int(msg)
        except:
            break
        target_ts = playout_ts + datetime.timedelta(milliseconds=22*(msg-first_msg))
        if (msg < first_msg):
            continue
            #print ts, msg, "discarded"
        elif (msg in received):
            continue
            #print ts, msg, "duplicate"
        elif (ts > target_ts):
            continue
            #print ts, msg, "late", target_ts
        else:
            second = (ts - first_ts).seconds
            #print ts, msg, "played", second
            goodput[second] = goodput.get(second, 0) + 160
            max_second = max_second if second < max_second else second
        received.append(msg)

for i in range(max_second+1):
    print i, goodput.get(i, 0)