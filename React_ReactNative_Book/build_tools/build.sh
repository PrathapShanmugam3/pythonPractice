#!/usr/bin/env bash
# Build the book PDF from src/*.md (alphabetical order). Needs: pandoc + Chromium (Playwright's).
set -euo pipefail
cd "$(dirname "$0")/.."
OUT="React_ReactNative_Zero_to_Master.pdf"
CHROME="${CHROME:-$(ls /opt/pw-browsers/chromium-*/chrome-linux/chrome 2>/dev/null | head -1)}"
TMP="$(mktemp -d)"
pandoc src/*.md -f markdown+raw_html+header_attributes -t html5 --standalone --highlight-style=pygments \
  --metadata pagetitle="React & React Native - Zero to Master" -c build_tools/style.css \
  --embed-resources -o "$TMP/book.html" 2>/dev/null || pandoc src/*.md -f markdown+raw_html -t html5 -s --metadata pagetitle="React Book" -c build_tools/style.css --self-contained -o "$TMP/book.html"
"$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf="$OUT" "file://$TMP/book.html" 2>&1 | tail -1
echo "Built $OUT"
