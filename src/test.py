from huffman_letter import HuffmanLetterComperessor
from huffman_word import HuffmanWordComperessor
from bitarray import bitarray

# import ipdb; ipdb.set_trace()
corpus = 'afdsfd svsddf,sdfs,23 lhiiuh{{~{,,x'
# corpus = 'As a doctor, how do you do that?'

def test_for_hfm_letter(corpus):
    file_path = 'lll.bin'
    hfm_letter = HuffmanLetterComperessor(corpus)
    hfm_letter.encode(file_path, src_str=corpus)
    decode_str = hfm_letter.decode(file_path)

    print(hfm_letter.coding_func)
    print(decode_str)
    print(corpus == decode_str)

# test_for_hfm_letter(corpus)

file_path = 'lll.bin'
hfm_word = HuffmanWordComperessor(corpus)
hfm_word.encode(file_path, src_str=corpus)
decode_str = hfm_word.decode(file_path)

print(hfm_word.coding_func)
print(decode_str)
print(corpus == decode_str)
