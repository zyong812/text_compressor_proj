import numpy as np
import collections
import pandas as pd
from bitarray import bitarray

class HuffmanLetterComperessor:
    def __init__(self, corpus):
        prob_dict = self._estimate_probabilities(corpus)
        hfm_tree  = self._build_tree(prob_dict)

        self.symbol_count   = len(prob_dict.keys())
        self.coding_func    = self._assign_codes(hfm_tree)
        self.decoding_func  = dict(map(lambda kv: (kv[1], kv[0]), self.coding_func.items()))

    def encode(self, src, file_path):
        bits = ''.join(list(map(lambda x: self.coding_func[x], src)))
        with open(file_path, 'wb') as f:
            bitarray(bits).tofile(f)


    def decode(self, file_path):
        bit_stream = bitarray()
        with open(file_path, 'rb') as f:
            bit_stream.fromfile(f)

        # import ipdb; ipdb.set_trace()
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
            c[k] = round(v / total_count, 5)
        return c

    def _build_tree(self, prob_dict):
        tree = []
        columns=['name', 'prob', 'left_child', 'right_child', 'adopted']
        # init tree
        for name, prob in prob_dict.items():
            tree.append([name, prob, None, None, False])

        # build tree
        while(True):
            probs = []
            for i in range(len(tree)):
                if tree[i][-1] == False:
                    probs.append(tree[i][1])
                else:
                    probs.append(np.inf)
            min1 = np.argmin(probs)
            probs[min1] = np.inf
            min2 = np.argmin(probs)

            # merge
            min1_row = tree[min1]
            min2_row = tree[min2]
            tree.append([
                min1_row[0] + min2_row[0], 
                min1_row[1] + min2_row[1],
                min1, min2, False
                ])
            tree[min1][-1] = True
            tree[min2][-1] = True

            # check stop
            adopted_status = list(map(lambda x: x[-1], tree))
            if adopted_status.count(False) <= 1:
                break;

        return pd.DataFrame(tree, columns=columns)

    def _assign_codes(self, pd_tree):
        # assgin codes (using DFS)
        pd_tree['code'] = ''
        root = list(pd_tree[pd_tree['adopted'] == False].index)[0]
        nodes = [root]
        while True:
            current_node = nodes.pop()
            if not np.isnan(pd_tree.loc[current_node, 'left_child']):
                left_child = int(pd_tree.loc[current_node, 'left_child'])
                nodes.append(left_child)
                pd_tree.loc[left_child, 'code'] = pd_tree.loc[current_node, 'code'] + '0'
            if not np.isnan(pd_tree.loc[current_node, 'right_child']):
                right_child = int(pd_tree.loc[current_node, 'right_child'])
                nodes.append(right_child)
                pd_tree.loc[right_child, 'code'] = pd_tree.loc[current_node, 'code'] + '1'
            if len(nodes) == 0: break
        
        symbols = np.array(pd_tree.loc[:self.symbol_count, 'name'])
        codes = np.array(pd_tree.loc[:, 'code'])
        coding_func = dict(zip(symbols, codes))
        return coding_func
