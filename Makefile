# Σ-Model — Root Makefile
# Modern academic research workflow: paper builds, tests, linting, and reproduction.

.PHONY: help all test lint paper paper01 paper02 companion arxiv figures clean

help:           ## Show available targets
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

all: test paper ## Run test suite and build paper manuscript

test:           ## Run automated test suite with pytest
	PYTHONPATH=code:paper02/src:$$PYTHONPATH pytest -v tests/ paper02/tests/

lint:           ## Run linter checks (ruff)
	ruff check code/ tests/

paper: paper01  ## Default paper target: build Paper 01 manuscript PDF

paper01:        ## Build Paper 01 v2 manuscript PDF (paper01/manuscript.pdf)
	$(MAKE) -C paper01 pdf

paper02:        ## Build Paper 02 deliverables and submission packages
	$(MAKE) -C paper02 submission

companion:      ## Build Paper 01 companion technical report PDF (paper01/companion/companion.pdf)
	cd paper01/companion && pdflatex -interaction=nonstopmode companion.tex && bibtex companion && pdflatex -interaction=nonstopmode companion.tex

arxiv:          ## Package Paper 01 arXiv submission bundle
	$(MAKE) -C paper01 arxiv

figures:        ## Generate all publication figures
	PYTHONPATH=.:code:paper02/src:$$PYTHONPATH python paper02/src/analysis/generate_publication_figures.py

clean:          ## Clean build and LaTeX artifacts
	$(MAKE) -C paper01 clean
	@if [ -f paper02/Makefile ]; then $(MAKE) -C paper02 clean; fi
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true


