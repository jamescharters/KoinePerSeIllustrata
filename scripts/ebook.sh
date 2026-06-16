#!/usr/bin/env bash
set -euo pipefail

pandoc -s --toc -o docs/kpsi.epub src/title.txt $(ls -1 src/*.md)
