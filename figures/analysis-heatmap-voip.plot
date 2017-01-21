set term postscript eps enhanced color defaultplex "Times-Roman" 24
set output '|ps2pdf -dEPSCrop - figures/analysis-heatmap-voip.pdf'
set border front linetype -1 linewidth 1.000
set palette defined (0 "white", 1 "#238443")
set view map
set samples 100, 100
set isosamples 100, 100
unset surface
unset key
set style data pm3d
set style function pm3d
set ticslevel 0
set title ""
set xlabel "RTT (ms)" font "Times-Roman, 28"
set xrange [ 0.0000 : 250.0000 ] noreverse nowriteback
set ylabel "Play-out delay (ms)" font "Times-Roman, 28"
set yrange [ 0.0000 : 150.0000 ] noreverse nowriteback
set zrange [ 0.0000 : 100.00000 ] noreverse nowriteback
set pm3d interpolate 0,0
set pm3d implicit at b
splot "data/analysis/heatmap-voip-playout.txt"
