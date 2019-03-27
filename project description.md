You are given several files which are plain text encoded by ASCII. You are required to write computer programs to compress these files and write a report. 
* Each compression program should be able to compress a file f to a compressed version f* and recover f from f*. 
* Try each of the following algorithms:
  * Huffman coding for the alphabet of letters
  * Huffman coding for the alphabet of words
  * Lempel-Ziv coding (choose a version by yourself)
* Evaluate your compression ratio as size(f*) over size(f). For Huffman coding, f* should embed the dictionary.  
* Compare your programs with common compressors in your computer, e.g., 7zip, RAR.
* Evaluate your program length.
* A bonus will be given if you can find a different algorithm do better than the above ones. 
* Small recovery error is allowed, but should be evaluated in your report.
* You can write the program by any programming language, but you should not include any existing library/source of the data compression algorithms. 


List of the files:

```
asyoulik.txt
Encoding: ANSI
Shakespeare
from The Canterbury Corpus,http://corpus.canterbury.ac.nz/descriptions/#calgary

alice29.txt
Encoding: ANSI
English text
from The Canterbury Corpus,http://corpus.canterbury.ac.nz/descriptions/#calgary

lcet10.txt
Encoding: ANSI
Technical writing
from The Canterbury Corpus,http://corpus.canterbury.ac.nz/descriptions/#calgary

plrabn12.txt
Encoding: ANSI
Poetry
from The Canterbury Corpus,http://corpus.canterbury.ac.nz/descriptions/#calgary

bible.txt
Encoding: ANSI
The King James version of the bible
from The Large Corpus, http://corpus.canterbury.ac.nz/descriptions/#calgary

world192.txt
Encoding: ANSI
The CIA world fact book
from The Large Corpus, http://corpus.canterbury.ac.nz/descriptions/#calgary
```