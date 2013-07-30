#!/bin/sh
set -e

# The jpg and pmm files are just the municode logo.
for image in $(ls tmp|sed -n '/\.pbm$/ s/\.pbm$//p'); do
  tesseract "tmp/${image}.pbm" "tmp/${image}" -l eng
  break
done
