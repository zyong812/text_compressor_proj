from bitarray import bitarray
import numpy as np

class LZTreeCompressor:
    def __init__(self):
        self.name = 'lz_tree'

    def encode(self, tgt_file_path, src_file_path=None, src_str=''):
        src_bin = bitarray(src_str)
        if src_file_path != None:
            with open(src_file_path, 'rb') as f:
                src_bin.fromfile(f)

        N = len(src_bin)
        sub_seuqences = {} # use hash for efficiency
        sub_seuqences[src_bin[:1].to01()] = 1
        pointer_bit_array = [('', src_bin[:1].to01())]

        i = 1
        while i < N:
            for j in range(i, N):
                current_s = src_bin[i:j+1].to01()
                if current_s in sub_seuqences:
                    if j == N - 1: 
                        break
                else:
                    break

            pointer_bits  = int(np.ceil(np.log2(len(sub_seuqences) + 1)))
            if current_s[:-1] in sub_seuqences:
                pointer_value = sub_seuqences[current_s[:-1]]
            else: 
                pointer_value = 0
            pointer = ("{0:{fill}" + str(pointer_bits) + "b}").format(pointer_value, fill='0')

            sub_seuqences[current_s] = len(sub_seuqences) + 1
            pointer_bit_array.append((pointer, current_s[-1]))
            i = j + 1

        # print(pointer_bit_array[:20])
        encoded_seq = ''.join(list(map(lambda x: x[0] + x[1], pointer_bit_array)))
        with open(tgt_file_path, 'wb') as f:
            bitarray(encoded_seq).tofile(f)


    def decode(self, bin_file_path=None, tgt_file_path=None):
        encoded_bin = bitarray('')
        if bin_file_path != None:
            with open(bin_file_path, 'rb') as f:
                encoded_bin.fromfile(f)

        sub_seuqences = [encoded_bin[:1].to01()]
        pointer_bit_array = []
        pointer_bit_array.append(('', encoded_bin[:1].to01()))

        i = 1
        encoded_N = len(encoded_bin)
        while i < encoded_N:
            step1 = int(np.ceil(np.log2(len(pointer_bit_array) + 1))) + 1
            if i+step1 > encoded_N: break
            s = encoded_bin[i:i+step1].to01()
            pointer_bit_array.append((s[:-1], s[-1]))
            i = i + step1

        for pb in pointer_bit_array[1:]:
            pointer = int(pb[0], 2)
            if pointer == 0:
                s = pb[1]
            else:
                s = sub_seuqences[pointer-1] + pb[1]
            sub_seuqences.append(s)

        # print(pointer_bit_array[:20])
        decoded_seq = ''.join(sub_seuqences)
        if tgt_file_path != None:
            with open(tgt_file_path, 'wb') as f:
                bitarray(decoded_seq).tofile(f)

        return decoded_seq
