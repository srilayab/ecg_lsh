import random
class L1HashFamily:
    def __init__(self, num_hash_functions, num_features, thresholds):
        self.num_hash_functions = num_hash_functions
        self.num_features = num_features
        self.thresholds = thresholds
        self.hash_tables= [{} for i in range(num_features)]

    def get_random_features(self):
        features = random.sample(range(self.num_features), self.num_hash_functions)
        feature_thresholds = self.thresholds[features]
        return features, feature_thresholds

    def create_hash_tables(self, vectors):
        features, feature_thresholds = self.get_random_features()
        for vec in vectors:
            for feature_index in features:
                hash_table = self.hash_tables[feature_index]
                vec_feature = vec[feature_index]
                value = 1 if vec_feature > feature_thresholds[feature_index] else 0
                if value in hash_table:
                    hash_table[value].append(vec)
                else:
                    hash_table[value] = [vec]

    # def query(self, q_vector):









