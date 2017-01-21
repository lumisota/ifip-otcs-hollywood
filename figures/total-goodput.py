import sys

if (len(sys.argv) != 2):
    exit("Usage: total-goodput.py [-tg.dat]")

total_goodput = 0

with open(sys.argv[1]) as dat:
    for line in dat:
        total_goodput += int(line.split()[1])
        
print "Total goodput: %d" % (total_goodput)