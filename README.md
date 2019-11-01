# LyricAnalyser
Takes a file with song lyrics and creates a histogram of word usage, in descending order.

The default song is Colors by Halsey, because it was on the radio when I tested the final program.

To change the file edit this line

```
with open("halseyColors.txt", "r") as song:
```
To whatever file you have added. E.g:
```
with open("song.txt", "r") as song:
```
