.PHONY: pdf clean arxiv

pdf:
	lualatex -interaction=nonstopmode main.tex
	bibtex main
	lualatex -interaction=nonstopmode main.tex
	lualatex -interaction=nonstopmode main.tex
	@echo ""
	@echo "=== Undefined references ==="
	@if grep -q "undefined" main.log; then grep "LaTeX Warning:.*undefined" main.log; else echo "(none)"; fi
	@ls -lh main.pdf

clean:
	rm -f main.aux main.log main.out main.toc main.fdb_latexmk main.fls main.bbl main.blg

arxiv: pdf
	mkdir -p arxiv
	cp main.tex arxiv/
	cp *.tex arxiv/
	cp *.sty arxiv/ 2>/dev/null || true
	cp *.bst arxiv/ 2>/dev/null || true
	cp ../paper/bibliography.bib arxiv/
	cp -r figures arxiv/
	cd arxiv && tar czf ../arxiv-submission.tar.gz *
	rm -rf arxiv
