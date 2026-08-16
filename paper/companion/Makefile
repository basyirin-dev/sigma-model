# Companion technical report build (same toolchain as the narrow paper).
TEX_SRC     = companion.tex
PDF_OUT     = companion.pdf
BIB_SRC     = companion.bib ../bibliography.bib

all: pdf

pdf: $(PDF_OUT)

$(PDF_OUT): $(TEX_SRC) $(BIB_SRC)
	BIBINPUTS=..:$$BIBINPUTS TEXINPUTS=..:$$TEXINPUTS latexmk -pdf -f $(TEX_SRC)

clean:
	latexmk -C
	rm -f *.aux *.bbl *.blg *.bcf *.fdb_latexmk *.fls *.log *.out *.run.xml

.PHONY: all pdf clean
