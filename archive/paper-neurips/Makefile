.PHONY: pdf clean arxiv

pdf:
	pdflatex -interaction=nonstopmode main.tex
	bibtex main
	pdflatex -interaction=nonstopmode main.tex
	pdflatex -interaction=nonstopmode main.tex
	@echo ""
	@echo "=== Undefined references ==="
	@if grep -q "undefined" main.log; then grep "LaTeX Warning:.*undefined" main.log; else echo "(none)"; fi
	@ls -lh main.pdf

clean:
	rm -f main.aux main.log main.out main.toc main.bbl main.blg main.run.xml

arxiv: pdf
	mkdir -p arxiv
	cp main.tex arxiv/
	cp *.sty arxiv/ 2>/dev/null || true
	cp *.bib arxiv/
	cp -r figures arxiv/
	cp -r supplement arxiv/
	cd arxiv && tar czf ../arxiv-submission.tar.gz *
	rm -rf arxiv
