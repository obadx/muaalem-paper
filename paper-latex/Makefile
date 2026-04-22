# Makefile for LaTeX project

MAIN = main
LATEX = lualatex -shell-escape -interaction=nonstopmode
# Previously was `biber`
BIBTEX = bibtex

.PHONY: all bib build clean cleanall zip

all: build

bib:
	$(BIBTEX) $(MAIN)

build:
	$(LATEX) $(MAIN).tex
	$(BIBTEX) $(MAIN)
	$(LATEX) $(MAIN).tex

quick:
	$(LATEX) $(MAIN).tex

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.lol *.gls *.glo *.ist *.glg *.xdy *.nav *.snm *.vrb *.synctex.gz *.bcf *.run.xml

cleanall: clean
	rm -f $(MAIN).pdf

zip:
	zip -r paper.zip main.tex references.bib abstract.tex Makefile \
		sections/ figures/ fonts/ assets/ \
		sn-jnl.cls sn-*.bst -x "*.bak*" -x "*.log"

watch:
	@echo "Watching for changes... (Ctrl+C to stop)"
	@while true; do \
		inotifywait -q -e modify *.tex *.bib; \
		make quick; \
	done

help:
	@echo "Available targets:"
	@echo "  all      - Build complete document (default)"
	@echo "  bib      - Run BibTeX only"
	@echo "  build    - Build document with BibTeX if needed"
	@echo "  quick    - Single pass compilation (no BibTeX)"
	@echo "  clean    - Remove auxiliary files"
	@echo "  cleanall - Remove auxiliary files and PDF"
	@echo "  zip     - Create zip archive for Overleaf upload"
	@echo "  watch    - Watch for changes and recompile"
	@echo "  help     - Show this help message"
