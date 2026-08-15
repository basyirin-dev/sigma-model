# Σ-Align Monograph — Makefile
# Build the monograph with latexmk (thesis/monograph.tex).

MAIN = monograph
LATEXMK = latexmk
OPTS = -pdf -interaction=nonstopmode -halt-on-error -file-line-error

.PHONY: all pdf watch clean

all: pdf

pdf:            ## Build monograph PDF
	$(LATEXMK) $(OPTS) $(MAIN).tex

watch:          ## Rebuild continuously on change
	$(LATEXMK) -pvc -pdf $(MAIN).tex

clean:          ## Clean build artifacts (keep PDF)
	$(LATEXMK) -c $(MAIN).tex

realclean:      ## Clean build artifacts incl. PDF
	$(LATEXMK) -C $(MAIN).tex
