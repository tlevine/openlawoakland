#!/bin/sh

set -e

FILE="$1"

if [ ! -f "$FILE" ]; then
  echo "USAGE: $0 [pdf]"
  exit 1
fi

# Extract images.
# Use jpeg so we don't have to determine whether ppm or pbm is used.
pdfimages "$FILE" "$FILE"

# Extract text to `echo $FILE|sed s/pdf$/txt/`
pdftotext "$FILE"
mv "`echo \"$FILE\"|sed s/pdf$/txt/`" "$FILE.txt"

# OCR
for extension in pbm ppm
  do
  for file in "$FILE"-[0-9][0-9][0-9]."${extension}"
    do

    # In case no files match this glob
    [ -e $file ] || continue

    echo $file

    # Ignore errors because it always has errors.
    tesseract "$file" "$file" -l eng &&
      cat "$file.txt" >> "$FILE.txt" || sleep 0
  done
done
