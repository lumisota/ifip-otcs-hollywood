set yrange [0:7000]
set xrange [108.5:109.5]

set ylabel "Bytes"

plot "figures/data/perf-voip-adsl-uk-pd60ms-i-tcp-tg.dat" using 1:2 notitle with lines