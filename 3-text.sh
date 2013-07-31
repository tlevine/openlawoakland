#!/bin/sh
set -e

# The jpg and pmm files are just the municode logo.
for image in $(ls tmp|sed -n '/\.pbm$/ s/\.pbm$//p'); do
  if test -e "tmp/${image}.txt"; then
    echo "Skipping tmp/${image}.pbm because it has already been OCRed"
    continue
  elif test $(stat -c %s "tmp/$image.pbm") -lt 10000; then
    echo "Skipping tmp/${image}.pbm because it's tiny"
    continue
  else
    echo "OCRing tmp/${image}.pbm"
    tesseract "tmp/${image}.pbm" "tmp/${image}" -l eng
  fi
done

# Combine into one file
for volume in volume1 volume2 planning; do
  cat "tmp/${volume}-*.txt" > "tmp/${volume}.txt"
done
