import collections
from bitarray import bitarray
from huffman_code import HuffmanCode

class HuffmanLetterComperessor:
    def __init__(self, corpus):
        self.name = 'hfm_letter'
        prob_dict = self._estimate_probabilities(corpus)
        hfm_tree  = HuffmanCode(prob_dict)

        self.coding_func    = hfm_tree.assign_codes()
        self.decoding_func  = dict(map(lambda kv: (kv[1], kv[0]),self.coding_func.items()))

    def encode(self, tgt_file_path, src_file_path=None, src_str=''):
        if src_file_path == None:
            src = src_str
        else:
            with open(src_file_path, 'r') as f:
                src = f.read()

        # Can optimize with bitarray extend function
        bits = ''.join(list(map(lambda x: self.coding_func[x], src)))
        with open(tgt_file_path, 'wb') as f:
            bitarray(bits).tofile(f)

    def decode(self, bin_file_path):
        bit_stream = bitarray()
        with open(bin_file_path, 'rb') as f:
            bit_stream.fromfile(f)

        decode_str = []
        start = 0
        for i in range(len(bit_stream)):
            code = bit_stream[start:i].to01()
            if code in self.decoding_func:
                decode_str.append(self.decoding_func[code])
                start = i

        decode_str = ''.join(decode_str)
        return decode_str

    def _estimate_probabilities(self, corpus):
        total_count = len(corpus)
        c = collections.Counter(corpus)
        for k, v in c.items():
            c[k] = round(v / total_count, 10)
        return c
