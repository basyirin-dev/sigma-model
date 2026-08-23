# Paper 02 — Makefile
# Builds manuscript PDF, runs tests, generates figures, and packages submission bundle

TEX_SRC     = writing/manuscript.tex
PDF_OUT     = writing/manuscript.pdf
FIGURES_SRC = writing/figures
BIB_SRC     = writing/bibliography.bib

all: test pdf

pdf:
	@if [ -f $(TEX_SRC) ]; then \
		cd writing && latexmk -pdf -f manuscript.tex; \
	else \
		echo "Manuscript source writing/manuscript.tex will be created in Phase 08."; \
	fi

figures:
	@echo "Figure generation pipeline will be activated in Phase 07."

arxiv:
	@echo "arXiv submission bundling will be activated in Phase 11."

clean:
	@if [ -d writing ]; then \
		cd writing && rm -f *.aux *.bbl *.blg *.fdb_latexmk *.fls *.log *.out *.synctex.gz; \
	fi
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

test:
	PYTHONPATH=src:../code:$$PYTHONPATH pytest -v tests/

.PHONY: all pdf clean test figures arxiv

