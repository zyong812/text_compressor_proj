import os
import glob
from huffman_letter import HuffmanLetterComperessor
from huffman_word import HuffmanWordComperessor
# import ipdb;ipdb.set_trace()

# path = '../data/test/*.txt'
path = '../data/*.txt'
file_paths = glob.glob(path)
corpus = ''
for file_path in file_paths:
    with open(file_path, 'r') as f:
        corpus += f.read()

def evaluate(compressor):
    print('Evaluation for ' + compressor.name + ':')
    for sample_file in file_paths:
        tgt_file_path = sample_file.replace('.txt', compressor.name + '.bin')
        compressor.encode(tgt_file_path, src_file_path=sample_file)

        org_size        = os.path.getsize(sample_file)
        compressed_size = os.path.getsize(tgt_file_path)
        print('\t' + sample_file + '\t' + \
            str(org_size) + ' -> ' + str(compressed_size) + '\t' + \
            'ratio: ' + str(compressed_size / org_size))
    # print(compressor.decode(tgt_file_path)[:1000])

####### HuffmanLetterComperessor #######
# hfm_letter = HuffmanLetterComperessor(corpus)
# evaluate(hfm_letter)

####### HuffmanWordComperessor #######
# 建树过程太耗时，可以考虑把 code 保存下来
hfm_word = HuffmanWordComperessor(corpus)
evaluate(hfm_word)
