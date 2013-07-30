## Outline
1. Download Oakland's laws as three PDF files containing scans of paper.
    Save them as `pdf/${volume}.pdf`.
2. Extract the images. Save them as `tmp/${volume}-${page}-${imageId}.${extension}`.
3. Convert the images to text. Save them as `tmp/${volume}-${page}-${imageId}.txt`.
4. Chunk the text into reasonable groupings, like generalized sections
5. Model the text as the specific hierarchy that the code follows, with titles,
    sections, subsections, &c.
6. Find cross-references.
7. Correct spellings somewhere along the way. I don't know whether the beginning
    or end will be easier. Maybe we'll eventually need two steps for this, with
    one rough pass in the beginning and one better pass in the end.
8. Convert it into the DC code browser schema.

I might skip some of the structuring and just extract citations for an
exercise in network analysis.
