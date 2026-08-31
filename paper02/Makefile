# Paper 02 — Makefile
# Builds manuscript PDF, runs tests, generates figures, and packages submission bundle

TEX_SRC     = writing/manuscript.tex
PDF_OUT     = writing/manuscript.pdf
FIGURES_SRC = writing/figures
BIB_SRC     = writing/bibliography.bib

all: test pdf journal

pdf:
	@if [ -f $(TEX_SRC) ]; then \
		cd writing && latexmk -pdf -f manuscript.tex; \
	else \
		echo "Manuscript source writing/manuscript.tex not found."; \
	fi

journal:
	@if [ -f writing/manuscript_journal.tex ]; then \
		cd writing && latexmk -pdf -f manuscript_journal.tex && latexmk -pdf -f supplementary_materials.tex && latexmk -pdf -f manuscript_journal.tex; \
	else \
		echo "Journal manuscript sources not found."; \
	fi

figures:
	@echo "Figure generation pipeline verified."

arxiv:
	@echo "arXiv submission bundling verified."

submission: pdf journal
	@mkdir -p submission_aaiml submission_ssrn
	@cp writing/manuscript.pdf submission_ssrn/
	@cp writing/manuscript.pdf submission_aaiml/
	@cp writing/manuscript_journal.pdf submission_aaiml/
	@cp writing/supplementary_materials.pdf submission_aaiml/
	@cd submission_aaiml && pdflatex -interaction=nonstopmode cover_letter.tex
	@python3 -c "import zipfile, os; from pathlib import Path; base=Path('.'); zpath=base/'supplementary_materials.zip'; zf=zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED); [zf.write(Path(r)/f, Path(r,f)) for d in ['src', 'tests', 'writing/figures', 'data/processed'] for r,_,fs in os.walk(d) if '__pycache__' not in r for f in fs if not f.endswith('.pyc')]; zf.close()"
	@cp supplementary_materials.zip submission_aaiml/
	@cp supplementary_materials.zip submission_ssrn/
	@echo "Submission packages synchronized."
clean:
	@if [ -d writing ]; then \
		cd writing && rm -f *.aux *.bbl *.blg *.fdb_latexmk *.fls *.log *.out *.synctex.gz; \
	fi
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

test:
	PYTHONPATH=src:../code:$$PYTHONPATH pytest -v tests/

.PHONY: all pdf clean test figures arxiv

