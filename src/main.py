import os
import glob
from huffman_letter import HuffmanLetterComperessor
from huffman_word import HuffmanWordComperessor
# import ipdb;ipdb.set_trace()

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
    # print(hfm.decode(tgt_file_path)[:1000])

####### HuffmanLetterComperessor #######
# hfm_letter = HuffmanLetterComperessor(corpus)
# evaluate(hfm_letter)

####### HuffmanWordComperessor #######
hfm_word = HuffmanWordComperessor(corpus)
evaluate(hfm_word)

filter(lambda x: if x[-1] == False, enumerate(tree))
probs_with_index = [(i, x[1]) for i, x in enumerate(tree) if x[-1] == False]
probs = list(map(lambda x: x[1], probs_with_index))
min1 = probs_with_index[argmin(probs)][0]
probs[min1] = np.inf
min2 = probs_with_index[argmin(probs)][0]