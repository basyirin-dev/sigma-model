TEX_SRC     = manuscript.tex
PDF_OUT     = manuscript.pdf
ARXIV_DIR   = ../arxiv-submission
FIGURES_SRC = figures
BIB_SRC     = bibliography.bib
JAIR_CLS    = jair.cls acmart.cls acmauthoryear.bbx acmauthoryear.cbx acmdatamodel.dbx

all: pdf

pdf: $(PDF_OUT)

$(PDF_OUT): $(TEX_SRC) $(BIB_SRC) $(JAIR_CLS)
	TEXINPUTS=.:$$TEXINPUTS latexmk -pdf -f $(TEX_SRC)

arxiv: pdf
	mkdir -p $(ARXIV_DIR)
	cp $(TEX_SRC) $(ARXIV_DIR)/
	cp $(PDF_OUT) $(ARXIV_DIR)/
	cp -r $(FIGURES_SRC) $(ARXIV_DIR)/
	cp $(BIB_SRC) $(ARXIV_DIR)/
	cp $(JAIR_CLS) $(ARXIV_DIR)/
	cd $(ARXIV_DIR) && tar czf ../sigma-arxiv-submission.tar.gz \
		manuscript.tex manuscript.pdf bibliography.bib figures/ \
		$(JAIR_CLS)
	@echo "arXiv bundle: $$(cd $(ARXIV_DIR) && ls ../sigma-arxiv-submission.tar.gz)"

clean:
	latexmk -C
	rm -f *.aux *.bbl *.blg *.bcf *.fdb_latexmk *.fls *.log *.out *.run.xml *.bcf *.xml

.PHONY: all pdf arxiv clean
