set style fill solid

unset colorbox
unset key

unset key
unset ytics
unset xtics

set xrange [0:130]
set yrange [0:1]

set palette model RGB defined (0 "orange", 1 "green", 2 "red")

plot "figures/data/perf-".name."-playout.dat" using 1:(1):2 with boxes linecolor rgb variable