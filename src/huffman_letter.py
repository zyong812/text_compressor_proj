import numpy as np
import collections
import pandas as pd


def estimate_probabilities(corpus):
    total_count = len(corpus)
    c = collections.Counter(corpus)

    for k, v in c.items():
        c[k] = round(v / total_count, 5)
    return c


def build_tree(p_dict):
    tree = []
    columns=['name', 'prob', 'left_child', 'right_child', 'adopted']
    # init tree
    for name, prob in p_dict.items():
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


def coding_func(pd_tree, N):
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
    
    symbols = np.array(pd_tree.loc[:N, 'name'])
    codes = np.array(pd_tree.loc[:, 'code'])
    coding_func = dict(zip(symbols, codes))
    return coding_func


