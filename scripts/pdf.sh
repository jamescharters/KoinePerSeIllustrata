#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

pandoc -s --toc --template=templates/default.latex -o kpsi.tex src/title.txt $(ls -1 src/*.md)
xelatex kpsi.tex
# Twice to build TOC correctly
xelatex kpsi.tex
mv kpsi.pdf docs/
rm kpsi.{log,aux,out,toc,tex}
