# Report - Data compression

- [Report - Data compression](#report---data-compression)
  - [1. Implementation and results](#1-implementation-and-results)
    - [Huffman coding (letter-level)](#huffman-coding-letter-level)
    - [Huffman coding (word-level)](#huffman-coding-word-level)
    - [Lempel-Ziv coding](#lempel-ziv-coding)
  - [Evaluation](#evaluation)
    - [2. Compared with my algorithms](#2-compared-with-my-algorithms)
    - [Compared with common compressor tools](#compared-with-common-compressor-tools)
    - [Evaluate encode and decode time (optional)](#evaluate-encode-and-decode-time-optional)
    - [Evaluate program length](#evaluate-program-length)
  - [3. Discussion](#3-discussion)

使用 Python 代码实现了三种算法

## 1. Implementation and results

### Huffman coding (letter-level)

estimate probability dict
Huffman Tree (figure)
Huffman codes (figure)
Encoding and decoding process

### Huffman coding (word-level)

word segmentation
estimate probability dict
Huffman Tree (figure)
Huffman codes (figure)
Encoding and decoding process

### Lempel-Ziv coding

encoding: 
* split to sub sequences
* convert to (pointer, bit) array
* convert to binary stream (according to $log(s(n))$)

decoding: 
* split to (pointer, bit) array
* recover to sub sequences
* concatenate to original binary stream

each with a 

## Evaluation

### 2. Compared with my algorithms

chart 

### Compared with common compressor tools

chart 

### Evaluate encode and decode time (optional)

LZ need optimize

### Evaluate program length

不知道要写什么，列个表列出每种算法的长度？

## 3. Discussion

* `bitarray` package 
* `json` to store dict

different algorithm 

recovery error 