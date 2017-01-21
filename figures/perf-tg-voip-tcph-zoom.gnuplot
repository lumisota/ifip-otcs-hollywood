set yrange [0:7000]
set xrange [84:85]

set ylabel "Bytes"

plot "figures/data/perf-voip-adsl-uk-pd60ms-i-tcph-tg.dat" using 1:2 notitle with lines