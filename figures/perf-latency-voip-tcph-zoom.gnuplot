set style fill solid
set palette model RGB defined ( 0 'black' )
unset colorbox
unset key

set ylabel "Latency (ms)"

set xrange [84:85]
set yrange [0:300]

plot "figures/data/perf-voip-adsl-uk-pd60ms-i-tcph.elapsed" using 1:($2):0 with boxes palette, \
     150 notitle lt rgb "red"
