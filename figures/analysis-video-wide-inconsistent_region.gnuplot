set terminal pdf color font "Times,14"
set output "figures/analysis-video-wide-inconsistent_region.pdf"

Tmax     = 2000
Tframing = 200

set xrange [0:3400]
set yrange [0:2100]

set style fill solid

f(x) = x + 4 * Tframing
g(x) = Tmax - Tframing - (x / 2.0)
h(x) = f(x)<g(x)?f(x):g(x)
i(x) = Tframing

set ytics out

set xtics out 0,250

set xlabel "T_{rtt} (ms)"
set ylabel "T_{playout} (ms)"

set xtics rotate

plot Tframing notitle, \
     '+' using 1:(f($1)):(g($1)) with filledc below lc rgb "#0DFF01" fillstyle pattern 2 notitle, \
     '+' using 1:(i($1)):(h($1)) with filledc below lc rgb "#FF000A" fillstyle pattern 5 notitle, \
     f(x) lt 2 lc rgb "#0DFF01" lw 1 notitle, \
     g(x) lt 2 lc rgb "#FF000A" lw 1 notitle