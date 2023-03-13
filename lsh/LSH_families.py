import random
import sklearn
from sklearn.datasets import make_blobs
import numpy as np
class E2LSHFamily:
    def __init__(self, data, chosen_feature=0 , num_hash_functions=5):
        self.data = data
        self.w = num_hash_functions
        self.chosen_feature = chosen_feature
        self.dim_per_feature = len(data[0][chosen_feature])
        self.hash_tables, self.r, self.b = self.create_hash_tables()

    def get_hash_tables(self):
        return self.hash_tables

    def get_r(self):
        X,y = make_blobs(n_samples=self.dim_per_feature, cluster_std=1, random_state=1)
        r = []
        for d in range(self.dim_per_feature):
            feat = X[d]
            r.append(d)
        return r

    def get_b(self, w):
        return random.randint(0, w)

    def create_hash_tables(self):
        hash_tables = []
        r_vectors = []
        b_vectors = []
        for i in range(1, self.w+1):
            hash_function = {}
            r = self.get_r()
            b = self.get_b(self.w)
            r_vectors.append(r)
            b_vectors.append(b)
            for (j, data_point) in enumerate(self.data):
                feat_1 = data_point[self.chosen_feature]
                hash_value = round((np.dot(feat_1, r) + b)/i, -3)
                if hash_value in hash_function:
                    hash_function[hash_value].append((j, data_point))
                else:
                    hash_function[hash_value] = [(j, data_point)]
            hash_tables.append(hash_function)
        return hash_tables, r_vectors, b_vectors

    def hash(self, vector):
        feat = vector[self.chosen_feature]
        hash_keys = []
        for i in range(1, len(self.hash_tables)+1):
            r = self.r[i-1]
            b = self.b[i-1]
            w = i
            hash_key = (np.dot(feat, r) + b)/w
            hash_keys.append(round(hash_key, -3))
        return hash_keys






class L1HashFamily:
    def __init__(self, data, num_hash_functions, thresholds):
        self.num_hash_functions = num_hash_functions
        self.num_features = len(data[0])
        self.thresholds = thresholds
        self.hash_tables= [{} for i in range(num_hash_functions)]
        self.features, self.feature_thresholds = self.create_hash_tables(data)


    def get_random_features(self):
        features = random.sample(range(self.num_features), self.num_hash_functions)
        feature_thresholds = self.thresholds[features]
        return features, feature_thresholds

    def create_hash_tables(self, vectors):
        features, feature_thresholds = self.get_random_features()
        for vec in vectors:
            for (i, feature_index) in enumerate(features):
                hash_table = self.hash_tables[i]
                vec_feature = vec[feature_index]
                value = 1 if vec_feature > feature_thresholds[feature_index] else 0
                if value in hash_table:
                    hash_table[value].append(vec)
                else:
                    hash_table[value] = [vec]

    def hash(self, vector):
        vector_hash_keys = []
        for (i, feature_index) in enumerate(self.features):
            vec_feature = vector[feature_index]
            value = 1 if vec_feature > self.feature_thresholds[feature_index] else 0
            vector_hash_keys.append(value)
        return vector_hash_keys









