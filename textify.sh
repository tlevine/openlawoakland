#!/bin/sh
set -e
volume=$(basename "$1" .pdf)

# Extract images
pdfimages -j -p "pdf/${volume}.pdf" "tmp/${volume}"

# OCR images
(
  cd tmp
  for extension in jpg pbm ppm
    do
    for file in $(ls|grep "\.{$extension}\$"); do
      echo "$file"
      bn=$(basename "$file" "$extension")

      # Ignore errors because it always has errors.
      tesseract "$file" "$bn" -l eng || sleep 0
    done
  done
)
