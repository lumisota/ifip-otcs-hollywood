set style fill solid

unset colorbox
unset key

unset key
unset ytics
unset xtics

set xrange [84:85]
set yrange [0:1]

plot "figures/data/perf-voip-adsl-uk-pd60ms-i-tcph-playout.dat" using 1:(1):2 with boxes linecolor rgb variable