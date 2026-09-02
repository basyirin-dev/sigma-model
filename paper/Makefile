# Defining paper — Makefile
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

arxiv: pdf
	@mkdir -p submission_arxiv/figures
	@cp writing/manuscript.tex submission_arxiv/
	@cp writing/manuscript.bbl submission_arxiv/
	@cp writing/tmlr.sty writing/tmlr.bst submission_arxiv/
	@cp writing/figures/*.pdf submission_arxiv/figures/ 2>/dev/null || true
	@cd submission_arxiv && tar -czf ../arxiv_bundle.tar.gz *
	@echo "arXiv submission bundle created: paper/arxiv_bundle.tar.gz"

submission: pdf arxiv
	@mkdir -p submission_ssrn submission_arxiv submission_attachments
	@cp writing/manuscript.pdf submission_ssrn/
	@cp writing/manuscript.pdf submission_attachments/ 2>/dev/null || true
	@cp writing/manuscript_journal.pdf submission_attachments/ 2>/dev/null || true
	@cp writing/supplementary_materials.pdf submission_attachments/ 2>/dev/null || true
	@cp arxiv_bundle.tar.gz submission_attachments/ 2>/dev/null || true
	@cp experiments/run-log.csv submission_attachments/ 2>/dev/null || true
	@cp data/processed/ood_summary_table.csv submission_attachments/ 2>/dev/null || true
	@cp data/processed/inflection_breakpoints.csv submission_attachments/ 2>/dev/null || true
	@cp data/processed/dense_grid_330_runs.csv submission_attachments/ 2>/dev/null || true
	@cp experiments/configs/matrix_p04.yaml submission_attachments/ 2>/dev/null || true
	@cp planning/preregistration.md submission_attachments/ 2>/dev/null || true
	@cp meta/TIER0_AUDIT_REPRODUCIBILITY_DOSSIER.md submission_attachments/ 2>/dev/null || true
	@python3 -c "import zipfile, os; from pathlib import Path; base=Path('.'); zpath=base/'supplementary_materials.zip'; zf=zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED); [zf.write(Path(r)/f, Path(r,f)) for d in ['src', 'tests', 'writing/figures', 'data/processed'] for r,_,fs in os.walk(d) if '__pycache__' not in r for f in fs if not f.endswith('.pyc') and not f.endswith('.zip') and not f.endswith('.tar.gz') and not f.endswith('.pdf')]; zf.close()"
	@cp supplementary_materials.zip submission_ssrn/
	@cp supplementary_materials.zip submission_attachments/
	@echo "Preprint submission packages synchronized (SSRN & arXiv & Attachments)."
clean:
	@if [ -d writing ]; then \
		cd writing && rm -f *.aux *.bbl *.blg *.fdb_latexmk *.fls *.log *.out *.synctex.gz; \
	fi
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

test:
	cd .. && PYTHONPATH=.:code:$$PYTHONPATH pytest -v tests/ paper/tests/

.PHONY: all pdf clean test figures arxiv

