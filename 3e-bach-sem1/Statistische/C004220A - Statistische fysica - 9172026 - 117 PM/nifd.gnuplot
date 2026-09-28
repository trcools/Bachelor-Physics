# Statistical Physics 1, Chapter 11
# Jan Ryckebusch, November 2011
#  Contour plots of n_i^{FD} and dN(\epsilon) for T < T_{F}
#  output: FDTdepen.eps and FDepsilonTdepen.eps
#
gnuplot<<??
set size square
set isosample 150,150
set nokey 
set pm3d map
set xlabel "{/Symbol e} / {/Symbol e}_{F}" font "Times-Italic, 25"
# document SymbolsandGnuplot.pdf
set ylabel "T/T_{F}" font "Times-Italic, 25"
set title "FD gemiddeld bezettingsgetal (T<T_{F})" font "Times-Italic, 25"
set xrange [0:+2]
set yrange [0:0.8]
#
# 
splot 1./(exp(1./y*(x-1))+1)
#
set term x11
set term post portrait enh color
set output "FDTdepen.eps"
replot
#
??
gnuplot<<!!
set size square
set isosample 150,150
set nokey 
set pm3d map
set xlabel "{/Symbol e} / {/Symbol e}_{F}" font "Times-Italic, 25"
# document SymbolsandGnuplot.pdf
set ylabel "T/T_{F}" font "Times-Italic, 25"
set title  " FD energiedistributie d N({/Symbol e}) / (f({/Symbol e}_{F}) d {/Symbol e})" font "Times-Italic, 25"
set xrange [0:+2]
set yrange [0:0.8]
#
# 
splot sqrt(x)/(exp(1./y*(x-1))+1)
#
set term x11
set term post portrait enh color
set output "FDepsilonTdepen.eps"
replot
#
!!



