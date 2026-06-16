#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

for file in src/*.md; do
  output=${file%.md}.html
  output=docs/${output#src/}
  pandoc -s --template=templates/default.html -o "$output" src/title.txt "$file"
done
