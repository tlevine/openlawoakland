## Steps

### 1. Download
Download Oakland's laws as three PDF files containing scans of paper.
Save them as `pdf/${volume}.pdf`.

```sh
./1-download.sh
```

### 2. Images
Extract the images. Save them as `tmp/${volume}-${page}-${imageId}.${extension}`.

```sh
./2-images.sh
```

### 3. Text
Convert the images to text. Save them as `tmp/${volume}-${page}-${imageId}.txt`.

```sh
./3-text.sh
```

### 4. Chunk
Chunk the text into reasonable groupings, like generalized sections

```sh
./4-chunk.py
```

### 5. Hierarchy
Model the text as the specific hierarchy that the code follows, with titles,
sections, subsections, &c.

```sh
./5-hierarchy.py
```
### 6. Cross-references

```sh
./6-cross-references.py
```

### 7. Spellings
Correct spellings somewhere along the way. I don't know whether the beginning
or end will be easier. Maybe we'll eventually need two steps for this, with one
rough pass in the beginning and one better pass in the end.

### 8. Schema
Convert it into the DC code browser schema.

## Notes
I might skip some of the structuring and just extract citations for an
exercise in network analysis.
