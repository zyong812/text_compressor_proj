import os
import glob
from huffman_letter_compressor import HuffmanLetterComperessor
from huffman_word_compressor import HuffmanWordComperessor
from lz_tree_compressor import LZTreeCompressor
# import ipdb;ipdb.set_trace()

path = '../data/test/*.txt'
# path = '../data/*.txt'
file_paths = glob.glob(path)
corpus = ''
for file_path in file_paths:
    with open(file_path, 'r') as f:
        corpus += f.read()

def evaluate(compressor):
    print('Evaluation for ' + compressor.name + ':')
    for sample_file in file_paths:
        tgt_file_path = sample_file.replace('.txt', '_'+ compressor.name + '.bin')
        compressor.encode(tgt_file_path, src_file_path=sample_file)

        org_size        = os.path.getsize(sample_file)
        compressed_size = os.path.getsize(tgt_file_path)
        print('\t' + sample_file + '\t' + \
            str(org_size) + ' -> ' + str(compressed_size) + '\t' + \
            'ratio: ' + str(compressed_size / org_size))

        # validate for decode
        decompress_path = sample_file.replace('.txt', '_'+ compressor.name + '.d')
        compressor.decode(tgt_file_path, decompress_path)

####### HuffmanLetterComperessor #######
hfm_letter = HuffmanLetterComperessor(corpus)
evaluate(hfm_letter)

####### HuffmanWordComperessor #######
hfm_word = HuffmanWordComperessor(corpus)
evaluate(hfm_word)

####### LZTreeCompressor #######
lz_tree = LZTreeCompressor()
evaluate(lz_tree)