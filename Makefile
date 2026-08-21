# Σ-Model — Root Makefile
# Modern academic research workflow: paper builds, tests, linting, and reproduction.

.PHONY: help all test lint paper companion arxiv figures clean

help:           ## Show available targets
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

all: test paper ## Run test suite and build paper manuscript

test:           ## Run automated test suite with pytest
	PYTHONPATH=code:$$PYTHONPATH pytest -v tests/

lint:           ## Run linter checks (ruff)
	ruff check code/ tests/

paper:          ## Build primary manuscript PDF (paper/manuscript.pdf)
	$(MAKE) -C paper pdf

companion:      ## Build companion technical report PDF (paper/companion/companion.pdf)
	cd paper/companion && pdflatex -interaction=nonstopmode companion.tex && bibtex companion && pdflatex -interaction=nonstopmode companion.tex

arxiv:          ## Package arXiv submission bundle
	$(MAKE) -C paper arxiv

figures:        ## Generate all publication figures (code/experiments/generate_figures.py)
	PYTHONPATH=code:$$PYTHONPATH python code/experiments/generate_figures.py

clean:          ## Clean build and LaTeX artifacts
	$(MAKE) -C paper clean
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

