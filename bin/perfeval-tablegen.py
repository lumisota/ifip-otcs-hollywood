import math

def avg(l):
    if len(l) == 0:
        return 0
    else:
        return sum(l)/float(len(l))

total_goodput = {}
sd = {}
avgs = {}

for protocol in ["tcp", "tcph"]:
    for ctraffic in ["i", "ii", "iii"]:
        for pd in ["150", "110", "60"]:
            tg = 0
            with open("figures/data/perf-voip-adsl-uk-pd%sms-%s-%s-tg.dat" % (pd, ctraffic, protocol)) as dat:
                for line in dat:
                    tg += int(line.split()[1])
            total_goodput[pd + "-" + ctraffic + "-" + protocol] = tg
            with open("figures/data/perf-voip-adsl-uk-pd%sms-%s-%s.elapsed" % (pd, ctraffic, protocol)) as dat:
                latencies = []
                for line in dat:
                    latencies.append(float(line.split()[1]))
                avgs[pd + "-" + ctraffic + "-" + protocol] = avg(latencies)
                variance = map(lambda x: (x - avgs[pd + "-" + ctraffic + "-" + protocol] )**2, latencies)
                avgs[pd + "-" + ctraffic + "-" + protocol] = "%.1f" % avgs[pd + "-" + ctraffic + "-" + protocol] 
                sd[pd + "-" + ctraffic + "-" + protocol]  = "%.1f" % math.sqrt(avg(variance))

outputFile = open('figures/perfeval-results.tex', 'w+')

outputFile.write("\\begin{tabular}{ccccccc}\n")
outputFile.write("\\toprule\n")     
outputFile.write("Scenario/result & \multicolumn{2}{c}{Long-lived TCP} & \multicolumn{2}{c}{HTTP} & \multicolumn{2}{c}{MPEG-DASH} \\\\\n")
outputFile.write("& TCP & TCP-H & TCP & TCP-H & TCP & TCP-H \\\\\n")
outputFile.write("\\midrule\n")     
outputFile.write("\\textbf{Scenario 1} & & & & & & \\\\\n")
outputFile.write("Total goodput (bytes) & %(150-i-tcp)d & %(150-i-tcph)d & %(150-ii-tcp)d & %(150-ii-tcph)d & %(150-iii-tcp)d & %(150-iii-tcph)d \\\\\n" % total_goodput)
outputFile.write("Avg. latency (ms) & %(150-i-tcp)s & %(150-i-tcph)s & %(150-ii-tcp)s & %(150-ii-tcph)s & %(150-iii-tcp)s & %(150-iii-tcph)s \\\\\n" % avgs)
outputFile.write("SD. latency (ms) & %(150-i-tcp)s & %(150-i-tcph)s & %(150-ii-tcp)s & %(150-ii-tcph)s & %(150-iii-tcp)s & %(150-iii-tcph)s \\\\\n" % sd)
outputFile.write("\\midrule\n")     
outputFile.write("\\textbf{Scenario 2} & & & & & & \\\\\n")
outputFile.write("Total goodput (bytes) & %(110-i-tcp)d & %(110-i-tcph)d & %(110-ii-tcp)d & %(110-ii-tcph)d & %(110-iii-tcp)d & %(110-iii-tcph)d \\\\\n" % total_goodput)
outputFile.write("Avg. latency (ms) & %(110-i-tcp)s & %(110-i-tcph)s & %(110-ii-tcp)s & %(110-ii-tcph)s & %(110-iii-tcp)s & %(110-iii-tcph)s \\\\\n" % avgs)
outputFile.write("SD. latency (ms) & %(110-i-tcp)s & %(110-i-tcph)s & %(110-ii-tcp)s & %(110-ii-tcph)s & %(110-iii-tcp)s & %(110-iii-tcph)s \\\\\n" % sd)
outputFile.write("\\midrule\n")     
outputFile.write("\\textbf{Scenario 3} & & & & & & \\\\\n")
outputFile.write("Total goodput (bytes) & %(60-i-tcp)d & %(60-i-tcph)d & %(60-ii-tcp)d & %(60-ii-tcph)d & %(60-iii-tcp)d & %(60-iii-tcph)d \\\\\n" % total_goodput)
outputFile.write("Avg. latency (ms) & %(60-i-tcp)s & %(60-i-tcph)s & %(60-ii-tcp)s & %(60-ii-tcph)s & %(60-iii-tcp)s & %(60-iii-tcph)s \\\\\n" % avgs)
outputFile.write("SD. latency (ms) & %(60-i-tcp)s & %(60-i-tcph)s & %(60-ii-tcp)s & %(60-ii-tcph)s & %(60-iii-tcp)s & %(60-iii-tcph)s \\\\\n" % sd)
outputFile.write("\\bottomrule\n")
outputFile.write("\\end{tabular}\n")

outputFile.close()
