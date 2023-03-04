import random
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









