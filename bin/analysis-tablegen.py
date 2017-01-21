# Analysis utility table builder

def tcp_rtt_bound(t_max, t_framing):
	return (2.0 * (t_max-5*t_framing)) / 3.0

def hlwd_rtt_bound(t_max, t_framing):
	return 2.0 * (t_max - 2*t_framing)

voip_bound = (tcp_rtt_bound(150, 20), hlwd_rtt_bound(150, 20))
odv_bound = (tcp_rtt_bound(30000, 2000), hlwd_rtt_bound(30000, 2000))
live_bound = (tcp_rtt_bound(1000, 200), hlwd_rtt_bound(1000, 200))

outputFile = open('figures/analysis-utilitycompare.tex', 'w+')

outputFile.write("\\begin{tabular}{lS[table-format=5,table-text-alignment=center]S[table-format=5.1]S[table-format=5]cccc}\n")
outputFile.write("\\toprule\n")     
outputFile.write("Application & {$T_\mathrm{max}$ (ms)} & \multicolumn{2}{c}{RTT Bound (ms)} &" \
				 "\multicolumn{2}{c}{Useful within a continent?} &" \
                                 "\multicolumn{2}{c}{Useful intercontinental?} \\\\\n")
outputFile.write("& & {Standard} & {Hollywood} & Standard & Hollywood & Standard & Hollywood \\\\\n")
outputFile.write("\\midrule\n")   
outputFile.write("Voice telephony & 150 & %.1f & %.0f & Y & Y & \cellcolor{green!15}N & \cellcolor{green!15}Y \\\\\n" % (voip_bound[0], voip_bound[1]))
outputFile.write("On-demand video & 30000 & %.1f & %.0f & Y & Y & Y & Y \\\\\n" % (odv_bound[0], odv_bound[1]))
outputFile.write("Live video & 1000 & %.1f & %.0f & \cellcolor{green!15}N & \cellcolor{green!15}Y & \cellcolor{green!15}N & \cellcolor{green!15}Y \\\\\n" % (live_bound[0], live_bound[1]))
outputFile.write("\\bottomrule\n")
outputFile.write("\\end{tabular}\n")

outputFile.close()
