TEX_SRC     = manuscript.tex
PDF_OUT     = manuscript.pdf
BIB_SRC     = bibliography.bib

all: pdf

pdf: $(PDF_OUT)

$(PDF_OUT): $(TEX_SRC) $(BIB_SRC)
	latexmk -pdf -f $(TEX_SRC)

clean:
	latexmk -C
	rm -f *.aux *.bbl *.blg *.bcf *.fdb_latexmk *.fls *.log *.out *.run.xml *.bcf *.xml

.PHONY: all pdf clean
