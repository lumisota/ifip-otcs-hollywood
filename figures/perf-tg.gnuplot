set yrange [0:14000]
set xrange [0:130]

set ylabel "Bytes/sec"

plot "figures/data/perf-".name."-tcp-tg.dat" using 1:($2*2) title "TCP" with lines, \
     "figures/data/perf-".name."-tcph-tg.dat" using 1:($2*2) title "Hollywood" with lines