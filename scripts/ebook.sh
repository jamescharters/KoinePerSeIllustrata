#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

pandoc -s --toc -o docs/kpsi.epub src/title.txt $(ls -1 src/*.md)
