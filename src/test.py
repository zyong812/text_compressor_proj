from huffman_letter_compressor import HuffmanLetterComperessor
from huffman_word_compressor import HuffmanWordComperessor
from bitarray import bitarray
from lz_tree_compressor import LZTreeCompressor

# import ipdb; ipdb.set_trace()
# corpus = 'afdsfd svsddf,sdfs,23 lhiiuh{{~{,,x?'
corpus = 'As a doctor, how do you do that?'

def test_for_hfm_letter(corpus):
    file_path = 'lll.bin'
    hfm_letter = HuffmanLetterComperessor(corpus, using_cached_codes=False)
    hfm_letter.encode(file_path, src_str=corpus)
    decode_str = hfm_letter.decode(bin_file_path=file_path)

    print(hfm_letter.coding_func)
    print(decode_str)
    print(corpus == decode_str)

# test_for_hfm_letter(corpus)

def test_for_hfm_word(corpus):
    file_path = 'lll.bin'
    hfm_word = HuffmanWordComperessor(corpus, using_cached_codes=False)
    hfm_word.encode(file_path, src_str=corpus)
    decode_str = hfm_word.decode(bin_file_path=file_path)

    print(hfm_word.coding_func)
    print(decode_str)
    print(corpus == decode_str)

# test_for_hfm_word(corpus)

def test_for_lz_tree():
    src_bin = bitarray('1011010100010')
    file_path = 'lz.bin'
    print('Original: ' + src_bin.to01())

    lz = LZTreeCompressor()
    lz.encode(file_path, src_str=src_bin)
    decoder_str = lz.decode(bin_file_path=file_path)
    print('Recovered: ' + decoder_str)

test_for_lz_tree()
