import ast

from lsh.LSH import LSH
from lsh.LSH_families import E2LSHFamily
import numpy as np

data = np.load("../data/X_feature_data.npy", allow_pickle=True)
LSH_family = E2LSHFamily
k = 5
distance_metric = np.linalg.norm
lsh = LSH(data, LSH_family, k)

q = data[498]
k_nearest = lsh.query(q)

Y = np.load("../data/loaded_data/Y.npy", allow_pickle=True)

# Check for any abnormaliites in neighbors
def check_abnormalities(k_nearest):
    abn_indices = set()
    for k in k_nearest:
        y = Y[k]
        arr = y.tolist()

        #string to dictionary
        res = ''
        for a in arr:
            if "{" in str(a):
                res = a
        dic = ast.literal_eval(res)

        dic_keys = dic.keys()
        for key in dic_keys:
            if key != 'NORM':
                if dic[key] > 0.0:
                    abn_indices.add(k)
    return abn_indices

actual_signals = np.load("../data/loaded_data/X_test.npy", allow_pickle=True)
q_index = 498

def euclidean(list1, list2):
    inside_squares = [(a-b) ** 2 for a, b in zip(list1, list2)]
    return sum(inside_squares) ** .5
def euclidean_neighbors(q_index):
    nearest_sorted = []
    q = actual_signals[q_index][:, 0].tolist()
    for (i, sig) in enumerate(actual_signals):
        sig = sig[:, 0].tolist()
        dist = euclidean(q, sig)
        nearest_sorted.append((dist, i))
        nearest_sorted.sort()
    return nearest_sorted

print(k_nearest)
abn = check_abnormalities(k_nearest)
print(abn)
en = euclidean_neighbors(q_index)
print(en)