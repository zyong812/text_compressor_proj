import pickle
import os.path
from bitarray import bitarray
from huffman_code import HuffmanCode

class HuffmanWordComperessor:
    def __init__(self, corpus):
        self.name = 'hfm_word'
        self._load_coding_func(corpus)

    def _load_coding_func(self, corpus):
        dict_file_path = '../data/dict/hfm_word_code_dict.pkl'
        if os.path.isfile(dict_file_path):
            with open(dict_file_path, 'rb') as f:
                self.coding_func = pickle.load(f)
        else:
            prob_dict = self._word_prob_dict(corpus)
            hfm_tree  = HuffmanCode(prob_dict)
            self.coding_func = hfm_tree.assign_codes()
            with open(dict_file_path, 'wb') as f:
                pickle.dump(self.coding_func, f)
        self.decoding_func  = dict(map(lambda kv: (kv[1], kv[0]), self.coding_func.items()))

    def encode(self, tgt_file_path, src_file_path=None, src_str=''):
        if src_file_path == None:
            src = src_str
        else:
            with open(src_file_path, 'r') as f:
                src = f.read()

        # Can optimize with bitarray extend function
        seg_words = self.word_segmentation(src)
        bits = ''.join(list(map(lambda x: self.coding_func[x], seg_words)))
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

    def word_segmentation(self, text):
        N = len(text)
        words = []
        # Segment to English words and other characters
        i = 0
        while i < N:
            char = text[i]
            word = char

            if i == N-1:
                i = i + 1
            elif (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
                for j in range(i+1, N):
                    next_char = text[j]
                    if (next_char >= 'a' and next_char <= 'z') or (next_char >= 'A' and next_char <= 'Z'):
                        word += next_char
                    else:
                        i = j
                        break
            else:
                i = i + 1

            words.append(word)
        return words

    def _word_prob_dict(self, corpus):
        word_stats = {}
        words = self.word_segmentation(corpus)

        for word in words:
            if word in word_stats:
                word_stats[word] = word_stats[word] + 1
            else: 
                word_stats[word] = 1

        prob_dict = dict(map(lambda kv: (kv[0], len(kv[0])*kv[1]/len(corpus)), word_stats.items()))
        return prob_dict