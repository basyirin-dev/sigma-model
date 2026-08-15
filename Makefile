# Σ-Model — Root Makefile
# The single active deliverable is the σ-Trap paper (paper/).
# The thesis monograph and Papers 01/02 are archived (archive/thesis/).

.PHONY: help all paper06 paper06-clean

help:           ## Show available targets
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

all: paper06    ## Build the σ-Trap paper

paper06:        ## Build Paper 06 (σ-Trap, TMLR format)
	$(MAKE) -C paper

paper06-clean:  ## Clean Paper 06 build artifacts
	$(MAKE) -C paper clean
