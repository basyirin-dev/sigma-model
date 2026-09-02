# Σ-Model — Root Makefile
# Modern academic research workflow: paper builds, tests, linting, and reproduction.
# The active deliverable is the DEFINING PAPER in paper/.
# (Paper 01 was rejected by TMLR, absorbed into the defining paper, and is archived under archive/paper01/.)

.PHONY: help all test lint paper figures submission arxiv clean

help:           ## Show available targets
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

all: test paper ## Run test suite and build the defining-paper manuscript

test:           ## Run the automated test suite (root infra + defining paper)
	PYTHONPATH=.:code:paper/src:$$PYTHONPATH pytest -v tests/ paper/tests/

lint:           ## Run linter checks (ruff)
	ruff check code/ tests/ paper/src/ paper/tests/

paper:          ## Build the defining-paper manuscript PDF (paper/writing/manuscript.pdf)
	$(MAKE) -C paper pdf

figures:        ## Generate all publication figures
	PYTHONPATH=.:code:paper/src:$$PYTHONPATH python paper/src/analysis/generate_publication_figures.py

submission:     ## Build submission packages for the defining paper
	$(MAKE) -C paper submission

arxiv:          ## Package the defining-paper arXiv submission bundle
	$(MAKE) -C paper arxiv

clean:          ## Clean build and LaTeX artifacts
	@if [ -f paper/Makefile ]; then $(MAKE) -C paper clean; fi
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
