import sys
import math

if (len(sys.argv) != 2):
    exit("Usage: latency-stats.py [.elapsed]")

def avg(l):
    return sum(l)/float(len(l))
    
latencies = []
variance = map(lambda x: (x - avg)**2, latencies)

with open(sys.argv[1]) as dat:
    for line in dat:
        latencies.append(float(line.split()[1]))

average = avg(latencies)
variance = map(lambda x: (x - average)**2, latencies)
standard_deviation = math.sqrt(avg(variance))

print "Average latency: %f" % (average)
print "Standard deviation: %f" % (standard_deviation)