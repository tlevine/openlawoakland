#!/bin/sh
set -e

extract_images() {
  volume=$(basename "$1" .pdf)
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
}

mkdir -p tmp
for pdf in $(ls pdf); do
  # If it has already run, don't run.
  images_total=$(pdfimages -list "pdf/$pdf" | sed 1,2d | wc -l)
  images_finished=$(ls tmp|grep $(basename "$pdf" .pdf)|grep -v '\.txt$'|wc -l)
  if test "$images_total" -eq "$images_finished"; then
    echo "The images have already been extracted from ${pdf}."
    continue
  elif test "$images_total" -lt "$images_finished"; then
    echo 'Something is wrong with the tmp directory;'
    echo "$pdf only has $images_total images, but the"
    echo "tmp directory has $images_finished images from ${pdf}."
    exit 1
  elif test "$images_total" -gt "$images_finished"; then
    extract_images "$pdf"
  else
    echo 'Something really weird happened.'
    echo "I was on the file \"$pdf\"."
    echo "It seems to contain $images_total images."
    echo "The tmp directory contains $images_finished images from {$pdf}."
  fi
done
