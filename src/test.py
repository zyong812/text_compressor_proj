from huffman_letter import HuffmanLetterComperessor

corpus = 'afdsfdsvsddf,sdfs,23lhiiuh'

file_path = '../data/xxx.bin'
hfm = HuffmanLetterComperessor(corpus)
hfm.encode(corpus, file_path)
decode_str = hfm.decode(file_path)
print(decode_str)

