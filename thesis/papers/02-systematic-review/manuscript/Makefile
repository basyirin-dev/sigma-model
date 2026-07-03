# Paper 02 Makefile
# Requires: latexmk, pdflatex, bibtex

.PHONY: pdf clean

pdf:
	TEXINPUTS=.:$$TEXINPUTS latexmk -pdf manuscript.tex

clean:
	latexmk -c manuscript.tex
	rm -f *.bbl *.run.xml *.synctex.gz
