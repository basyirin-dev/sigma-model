TEX_SRC     = manuscript.tex
PDF_OUT     = manuscript.pdf
ARXIV_DIR   = ../arxiv-submission
FIGURES_SRC = figures
BIB_SRC     = bibliography.bib
all: pdf

pdf: $(PDF_OUT)

$(PDF_OUT): $(TEX_SRC) $(BIB_SRC) tmlr.sty tmlr.bst
	TEXINPUTS=.:$$TEXINPUTS latexmk -pdf -f $(TEX_SRC)

arxiv: pdf
	mkdir -p $(ARXIV_DIR)/companion
	cp $(TEX_SRC) $(ARXIV_DIR)/
	# arXiv copy: preprint option so the real author name renders (stylefile default is
	# "Anonymous authors"); see tmlr.sty \if@accepted + \if@preprint branches.
	sed -i 's/\\usepackage{tmlr}/\\usepackage[accepted,preprint]{tmlr}/' $(ARXIV_DIR)/manuscript.tex
	cp manuscript.bbl $(ARXIV_DIR)/
	cp -r $(FIGURES_SRC) $(ARXIV_DIR)/
	cp $(BIB_SRC) $(ARXIV_DIR)/
	cp tmlr.sty tmlr.bst $(ARXIV_DIR)/
	cp companion/companion.tex companion/companion.bbl companion/companion.bib $(ARXIV_DIR)/companion/
	# Compile the preprint-option copy so the shipped PDF matches the shipped source
	# (the canonical paper/manuscript.pdf is the double-blind build and must not ship).
	cd $(ARXIV_DIR) && pdflatex -interaction=nonstopmode manuscript.tex >/dev/null 2>&1 && pdflatex -interaction=nonstopmode manuscript.tex >/dev/null 2>&1
	cd $(ARXIV_DIR) && tar czf ../sigma-arxiv-submission.tar.gz \
		manuscript.tex manuscript.bbl manuscript.pdf bibliography.bib figures/ \
		tmlr.sty tmlr.bst companion/
	@echo "arXiv bundle: $$(cd $(ARXIV_DIR) && ls ../sigma-arxiv-submission.tar.gz)"

clean:
	latexmk -C
	rm -f *.aux *.bbl *.blg *.bcf *.fdb_latexmk *.fls *.log *.out *.run.xml *.bcf *.xml

.PHONY: all pdf arxiv clean
