unset key
unset ytics
unset xtics

unset colorbox
unset key

set xrange [84:85]
set yrange [0:1]

plot "figures/data/perf-voip-adsl-uk-pd60ms-i-tcph-barcode.dat" using 1:(1):4 with boxes linecolor rgb variable