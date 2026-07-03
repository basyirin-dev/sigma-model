# Σ-Align Thesis — Root Makefile
# Per-paper builds delegate to each paper's local Makefile.

.PHONY: help all paper01 paper01-clean paper02 paper02-clean paper06 paper06-clean

help:           ## Show available targets
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

all: paper01 paper02 paper06  ## Build all papers

paper01:        ## Build Paper 01 (Scoping Review)
	$(MAKE) -C thesis/papers/01-scoping-review/manuscript

paper01-clean:  ## Clean Paper 01 build artifacts
	$(MAKE) -C thesis/papers/01-scoping-review/manuscript clean

paper02:        ## Build Paper 02 (Systematic Review)
	$(MAKE) -C thesis/papers/02-systematic-review/manuscript

paper02-clean:  ## Clean Paper 02 build artifacts
	$(MAKE) -C thesis/papers/02-systematic-review/manuscript clean

paper06:        ## Build Paper 06 (Σ-Model)
	$(MAKE) -C paper

paper06-clean:  ## Clean Paper 06 build artifacts
	$(MAKE) -C paper clean
