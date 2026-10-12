# React & React Native - Zero to Master (book)

* `React_ReactNative_Zero_to_Master.pdf` - the book (grows one Part at a time; currently: title page, TOC, how to use, Part 0).
* `src/*.md` - Markdown source, one file per chunk, concatenated alphabetically.
* `build_tools/build.sh` - rebuilds the PDF (needs `pandoc` and Playwright's Chromium).
* `build_tools/check_examples.py` - runs every ```` ```js ```` example with Node to verify the shown output.
