import os
import glob
from huffman_letter_compressor import HuffmanLetterComperessor
from huffman_word_compressor import HuffmanWordComperessor
from lz_tree_compressor import LZTreeCompressor
import pandas as pd
# import ipdb;ipdb.set_trace()

# path = '../data/test/*.txt'
path = '../data/*.txt'
file_paths = glob.glob(path)
corpus = ''
for file_path in file_paths:
    with open(file_path, 'r') as f:
        corpus += f.read()

def evaluate(compressor):
    res = []
    print('Evaluate for ' + compressor.name)
    for sample_file in file_paths:
        tgt_file_path = sample_file.replace('.txt', '_'+ compressor.name + '.compressed')
        compressor.encode(tgt_file_path, src_file_path=sample_file)

        org_size        = round(os.path.getsize(sample_file) / 1024, 1)
        compressed_size = round(os.path.getsize(tgt_file_path) / 1024, 1)
        ratio = round(compressed_size / org_size, 3)

        # validate for decode
        decompress_path = sample_file.replace('.txt', '_'+ compressor.name + '.decompressed')
        compressor.decode(tgt_file_path, decompress_path)

        res.append([compressor.name, sample_file.replace("../data/", ''), org_size, compressed_size, ratio])
    
    res = pd.DataFrame(res, columns=['Compressor', 'File name', 'Original size(kB)', 'Compressed size(kB)', 'Compress ratio'])
    return res

####### HuffmanLetterComperessor #######
hfm_letter = HuffmanLetterComperessor(corpus)
res1 = evaluate(hfm_letter)
print(res1)

####### HuffmanWordComperessor #######
hfm_word = HuffmanWordComperessor(corpus)
res2 = evaluate(hfm_word)
print(res2)

# ####### LZTreeCompressor #######
lz_tree = LZTreeCompressor()
res3 = evaluate(lz_tree)
print(res3)

# ####### gzip #######
res4 = evaluate('gzip')


import ipdb;ipdb.set_trace()
res = pd.concat([res1, res2, res3], ignore_index=True)
res.to_csv('eval_res.csv', index = None, header=True)
