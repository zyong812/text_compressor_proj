import numpy as np
import pandas as pd

class HuffmanCode:
    def __init__(self, prob_dict):
        self.prob_dict = prob_dict
        self.symbol_count = len(self.prob_dict.keys())
        self._build_tree()

    def assign_codes(self):
        # assgin codes (using DFS)
        self.pd_tree['code'] = ''
        root = list(self.pd_tree[self.pd_tree['adopted'] == False].index)[0]
        nodes = [root]
        while True:
            current_node = nodes.pop()
            if not np.isnan(self.pd_tree.loc[current_node, 'left_child']):
                left_child = int(self.pd_tree.loc[current_node, 'left_child'])
                nodes.append(left_child)
                self.pd_tree.loc[left_child, 'code'] = self.pd_tree.loc[current_node, 'code'] + '0'
            if not np.isnan(self.pd_tree.loc[current_node, 'right_child']):
                right_child = int(self.pd_tree.loc[current_node, 'right_child'])
                nodes.append(right_child)
                self.pd_tree.loc[right_child, 'code'] = self.pd_tree.loc[current_node, 'code'] + '1'
            if len(nodes) == 0: break

        symbols = np.array(self.pd_tree.loc[:(self.symbol_count-1), 'name'])
        codes = np.array(self.pd_tree.loc[:, 'code'])
        coding_func = dict(zip(symbols, codes))
        return coding_func

    def _build_tree(self):
        tree = []
        columns=['name', 'prob', 'left_child', 'right_child', 'adopted']
        # init tree
        for name, prob in self.prob_dict.items():
            tree.append([name, prob, None, None, False])
        # print(len(tree))

        # build tree
        while(True):
            # print(len(tree))
            # probs = []
            # for i in range(len(tree)):
            #     if tree[i][-1] == False:
            #         probs.append(tree[i][1])
            #     else:
            #         probs.append(np.inf)
            # min1 = np.argmin(probs)
            # probs[min1] = np.inf
            # min2 = np.argmin(probs)
            probs_with_index = [(i, x[1]) for i, x in enumerate(tree) if x[-1] == False]
            probs = list(map(lambda x: x[1], probs_with_index))
            prob_min1 = np.argmin(probs)
            min1  = probs_with_index[prob_min1][0]
            probs[prob_min1] = np.inf
            min2 = probs_with_index[np.argmin(probs)][0]

            # merge
            min1_row = tree[min1]
            min2_row = tree[min2]
            tree.append([
                'MiddleNode', 
                min1_row[1] + min2_row[1],
                min1, min2, False
                ])
            tree[min1][-1] = True
            tree[min2][-1] = True

            # check stop
            adopted_status = list(map(lambda x: x[-1], tree))
            if adopted_status.count(False) <= 1:
                break;

        self.pd_tree = pd.DataFrame(tree, columns=columns)
        return True
