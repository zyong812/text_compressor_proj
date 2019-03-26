import huffman_letter
import numpy as np
import pandas as pd
from bitarray import bitarray

corpus = 'afdsfdsvsddf,sdfs,23lhiiuh'

p_dict = huffman_letter.estimate_probabilities(corpus)


tree = huffman_letter.build_tree(p_dict)
coding_func = huffman_letter.coding_func(tree, 11)

# encoding
# import ipdb; ipdb.set_trace()

# 改成使用 bitarray extend function
bits = ''.join(list(map(lambda x: coding_func[x], corpus)))

with open('xxx.bin', 'wb') as f:
    bitarray(bits).tofile(f)

# decoding
decoding_func = dict(map(lambda kv: (kv[1], kv[0]), coding_func.items()))
bit_stream = bitarray()
with open('xxx.bin', 'rb') as f:
    bit_stream.fromfile(f)

import ipdb; ipdb.set_trace()
decode_str = []
start = 0
for i in range(len(bit_stream)):
    code = bit_stream[start:i].to01()
    if code in decoding_func:
        decode_str.append(decoding_func[code])
        start = i

decode_str = ''.join(decode_str)
print(decode_str)
