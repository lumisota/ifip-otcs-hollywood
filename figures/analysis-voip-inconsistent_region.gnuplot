set terminal pdf color font "Times,14"
set output "figures/analysis-voip-inconsistent_region.pdf"

Tmax     = 150
Tframing = 20

set xrange [0:240]
set yrange [0:Tmax+10]

set style fill solid

f(x) = x + 4 * Tframing
g(x) = Tmax - Tframing - (x / 2.0)
h(x) = f(x)<g(x)?f(x):g(x)
i(x) = Tframing

set ytics out

set xtics out 0,10
set mxtics 5

set xlabel "T_{rtt} (ms)"
set ylabel "T_{playout} (ms)"

set arrow from 20,0 to 20,150 nohead front dashtype 2

set arrow from 0,60 to 20,60 nohead front dashtype 2
set arrow from 0,110 to 20,110 nohead front dashtype 2
set arrow from 0,150 to 20,150 nohead front dashtype 2

set xtics rotate

plot Tframing notitle, \
     '+' using 1:(f($1)):(g($1)) with filledc below lc rgb "#0DFF01" fillstyle pattern 2 notitle, \
     '+' using 1:(i($1)):(h($1)) with filledc below lc rgb "#FF000A" fillstyle pattern 5 notitle, \
     f(x) lt 2 lc rgb "#0DFF01" lw 1 notitle, \
     g(x) lt 2 lc rgb "#FF000A" lw 1 notitle, \
     "<echo '20 150 I'" with labels point pt 7 offset char 1,0 font ',11' notitle, \
     "<echo '20 110 II'" with labels point pt 7 offset char 1,0 font ',11' notitle, \
     "<echo '20 60 III'" with labels point pt 7 offset char 1,0 font ',11' notitle