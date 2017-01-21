unset key
unset ytics

unset colorbox
unset key

set xrange [0:130]
set yrange [0:1]

plot "figures/data/perf-".name."-barcode.dat" using 1:(1):4 with boxes linecolor rgb variable