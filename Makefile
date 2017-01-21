# ================================================================================================
# Generic Makefile for a LaTeX paper -- this requires GNU make.
# Colin Perkins <csp@csperkins.org>

# This is the basename for the LaTeX source.  The files $(TEX_BASE).tex and
# $(TEX_BASE).bib should exist, and contain the paper text and bibliography.
# The $(TEX_OTHER) and $(TEX_GENERATED) variables should include all .tex
# files included (\input) into $(TEX_BASE).tex (full filenames, including
# the .tex extension). The $(TEX_GENERATED) files are produced by running
# this Makefile, and will be removed by "make clean"; the $(TEX_STATIC)
# files are static and are not removed.
TEX_BASE      = utltcp-paper
TEX_STATIC    = sections/intro.tex \
			    sections/background.tex \
			    sections/arch.tex \
			    sections/analysis.tex \
			    sections/perf-eval.tex \
			    sections/dep-eval.tex \
			    sections/relwork.tex \
			    sections/performance.tex \
			    sections/reproducibility.tex \
			    sections/conc.tex
TEX_GENERATED = figures/analysis-utilitycompare.tex \
                figures/perfeval-results.tex

# A list of any graphics file included in the LaTeX document. These must be
# in PDF format, and the filenames must include the .pdf extension. Those
# files listed in $(GRAPHICS_GENERATED) should be built by this Makefile;
# they will be removed by "make clean". The files in $(GRAPHICS_STATIC) are
# static figures which are not removed by "make clean".
GRAPHICS_GENERATED = figures/analysis-voip-inconsistent_region.pdf \
					 figures/analysis-video-wide-inconsistent_region.pdf \
					 figures/analysis-video-zoomed-inconsistent_region.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-i-tcp-latency.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-i-tcph-latency.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-i-tcp-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-i-tcph-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-i-tcp-playout.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-i-tcph-playout.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-i-tg.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-ii-tcp-latency.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-ii-tcph-latency.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-ii-tcp-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-ii-tcph-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-ii-tcp-playout.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-ii-tcph-playout.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-ii-tg.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-iii-tcp-latency.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-iii-tcph-latency.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-iii-tcp-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-iii-tcph-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-iii-tcp-playout.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-iii-tcph-playout.pdf \
					 figures/perf-voip-adsl-uk-pd150ms-iii-tg.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-i-tcp-latency.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-i-tcph-latency.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-i-tcp-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-i-tcph-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-i-tcp-playout.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-i-tcph-playout.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-i-tg.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-ii-tcp-latency.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-ii-tcph-latency.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-ii-tcp-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-ii-tcph-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-ii-tcp-playout.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-ii-tcph-playout.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-ii-tg.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-iii-tcp-latency.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-iii-tcph-latency.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-iii-tcp-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-iii-tcph-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-iii-tcp-playout.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-iii-tcph-playout.pdf \
					 figures/perf-voip-adsl-uk-pd110ms-iii-tg.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-i-tcp-latency.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-i-tcph-latency.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-i-tcp-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-i-tcph-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-i-tcp-playout.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-i-tcph-playout.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-i-tg.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-ii-tcp-latency.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-ii-tcph-latency.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-ii-tcp-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-ii-tcph-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-ii-tcp-playout.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-ii-tcph-playout.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-ii-tg.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-iii-tcp-latency.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-iii-tcph-latency.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-iii-tcp-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-iii-tcph-barcode.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-iii-tcp-playout.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-iii-tcph-playout.pdf \
					 figures/perf-voip-adsl-uk-pd60ms-iii-tg.pdf \
					 figures/perf-tg-voip-tcp-zoom.pdf \
					 figures/perf-playout-voip-tcp-zoom.pdf \
					 figures/perf-latency-voip-tcp-zoom.pdf \
					 figures/perf-barcode-voip-tcp-zoom.pdf \
					 figures/perf-tg-voip-tcph-zoom.pdf \
					 figures/perf-playout-voip-tcph-zoom.pdf \
					 figures/perf-latency-voip-tcph-zoom.pdf \
					 figures/perf-barcode-voip-tcph-zoom.pdf

GRAPHICS_STATIC    = figures/hol-blocking-delay.pdf \
					 figures/message-resegmentation.pdf \
					 figures/analysis-validation-heatmap.pdf \
           			 figures/analysis-delay-region.pdf \
					 figures/analysis-HoL-region-v2.pdf \
					 figures/analysis-HoL-time.pdf \
					 figures/goodput-placeholder.pdf \
					 figures/message-flow-combined.pdf

# A list of any other files generated by running this Makefile, that should be
# removed when "make clean" is executed. $(TEX_BASE).pdf does not depend on
# these files, but $(TEX_GENERATED) or $(GRAPHICS_GENERATED) will likely do so.
OTHER_GENERATED = otcs-cover-letter.pdf

.PRECIOUS: figures/data/perf-%.message-times figures/data/perf-%-tg.dat figures/data/perf-%.elapsed figures/data/perf-%-barcode.dat figures/data/perf-%-playout.dat figures/data/perf-%-barcode.xtics

all: $(OTHER_GENERATED) $(GRAPHICS_GENERATED) $(TEX_BASE).pdf

# ================================================================================================
# Add paper-specific rules here, to build $(TEX_GENERATED):

# ================================================================================================
# Add paper-specific rules here, to build $(GRAPHICS_GENERATED):

figures/data/perf-%.elapsed: figures/data/perf-%.aclient-out figures/extract-message-elapsed.py
	python2.7 figures/extract-message-elapsed.py figures/data/perf-$*.aclient-out > figures/data/perf-$*.elapsed

figures/data/perf-%-barcode.dat figures/data/perf-%-barcode.xtics: figures/data/perf-%.aclient-tcpdump figures/data/perf-%.aclient-kernlog figures/loss-barcode-gen-recv.py
	python2.7 figures/loss-barcode-gen-recv.py figures/data/perf-$*.aclient-tcpdump figures/data/perf-$*.aclient-kernlog > figures/data/perf-$*-barcode.dat

figures/data/perf-%-playout.dat: figures/data/perf-%.aclient-out figures/app-playout.py
	python2.7 figures/app-playout.py figures/data/perf-$*.aclient-out > figures/data/perf-$*-playout.dat
	
figures/data/perf-%.aclient-out figures/data/perf-%.aclient-tcpdump figures/data/perf-%.aserver-tcpdump: Vagrantfile evaluations/perf-voip-adsl.py
	@echo "================================================================================"
	@echo "== Building $@"
	vagrant up
	vagrant ssh -c "sudo sysctl -w net.ipv4.tcp_low_latency=1"
	-vagrant ssh -c "sudo python /vagrant/evaluations/perf-voip-adsl.py $*"
	vagrant halt
	vagrant destroy -f 
	@echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"

figures/data/perf-%-tg.dat: figures/data/perf-%.aclient-out figures/tg-extract-new.py
	python2.7 figures/tg-extract-new.py figures/data/perf-$*.aclient-out > figures/data/perf-$*-tg.dat

figures/perf-%-latency.pdf: figures/perf-latency.gnuplot-pdf figures/perf-latency.gnuplot figures/data/perf-%.elapsed
	gnuplot -e "name='$*'" figures/perf-latency.gnuplot-pdf figures/perf-latency.gnuplot

figures/perf-%-barcode.pdf: figures/perf-barcode.gnuplot-pdf figures/perf-barcode.gnuplot figures/data/perf-%-barcode.xtics figures/data/perf-%-barcode.dat
	gnuplot -e "name='$*'" figures/perf-barcode.gnuplot-pdf figures/data/perf-$*-barcode.xtics figures/perf-barcode.gnuplot

figures/perf-%-playout.pdf: figures/perf-playout.gnuplot-pdf figures/perf-playout.gnuplot figures/data/perf-%-playout.dat
	gnuplot -e "name='$*'" figures/perf-playout.gnuplot-pdf figures/perf-playout.gnuplot

figures/perf-%-tg.pdf: figures/perf-tg.gnuplot-pdf figures/perf-tg.gnuplot figures/data/perf-%-tcp-tg.dat figures/data/perf-%-tcph-tg.dat
	gnuplot -e "name='$*'" figures/perf-tg.gnuplot-pdf figures/perf-tg.gnuplot

figures/analysis-%-inconsistent_region.pdf: figures/analysis-%-inconsistent_region.gnuplot
	gnuplot figures/analysis-$*-inconsistent_region.gnuplot

figures/%.pdf: figures/%.gnuplot figures/%.gnuplot-pdf
	gnuplot figures/$*.gnuplot-pdf figures/$*.gnuplot
    
# ================================================================================================
# Add paper-specific rules here, to build $(OTHER_GENERATED):

figures/analysis-utilitycompare.tex: bin/analysis-tablegen.py
	python2.7 bin/analysis-tablegen.py

figures/perfeval-results.tex: bin/perfeval-tablegen.py
	python2.7 bin/perfeval-tablegen.py

otcs-cover-letter.pdf: otcs-cover-letter.tex
	@bin/latex-build.sh otcs-cover-letter
    
# ================================================================================================
# No user-serviceable parts below

REGEX_CITE = "LaTeX Warning: Citation.*undefined"
REGEX_LABL = "LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right."
BLANK_LINE = "================================================================================"

# Ghostscript (gs) is used to post-process the output to embed all fonts.
%.pdf: %.tex %.bib $(TEX_STATIC) $(TEX_GENERATED) $(GRAPHICS_STATIC) $(GRAPHICS_GENERATED) $(OTHER_GENERATED)
	@bin/latex-build.sh     $(TEX_BASE)
	@bin/check-pdf-fonts.sh $(TEX_BASE).pdf $(TEX_BASE).fonts
	@bin/check-for-duplicate-words.sh $(TEX_BASE).tex $(TEX_STATIC) $(TEX_GENERATED)
	@bin/check-for-weasel-words.sh    $(TEX_BASE).tex $(TEX_STATIC) $(TEX_GENERATED)
	@bin/check-for-todo.sh            $(TEX_BASE).tex $(TEX_STATIC) $(TEX_GENERATED)

data-clean:
	vagrant destroy -f
	-rm -rf figures/data/*


paper-clean:
	-rm -f $(TEX_BASE).pdf $(TEX_BASE).aux $(TEX_BASE).log $(TEX_BASE).blg $(TEX_BASE).bbl $(TEX_BASE).out $(TEX_BASE).fonts $(TEX_GENERATED) $(GRAPHICS_GENERATED) $(OTHER_GENERATED)
	-rm -rf figures/data/*.elapsed figures/data/*tg.dat figures/data/*playout.dat figures/data/*barcode.dat figures/data/*barcode.xtics

clean: data-clean paper-clean
