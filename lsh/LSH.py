class LSH:

    '''
    hash_family: LSH hash family
    k: number of neighbors
    L: number of hash_functions
    '''
    def __init__(self, data, hash_family, k, L, distance_metric, thresholds=None):
        self.hash_family = hash_family(data, L, )
        self.k = k
        self.L = L
        self.distance_metric = distance_metric
        self.hash_tables = self.hash_family.create_hash_tables(data, thresholds)

    def query(self, q):
        q_hash = self.hash_family.hash(q)
        candidate_set = set()
        for l in range(self.L):
            q_feature = q_hash[l]
            hash_table = self.hash_tables[l]
            matching_candidates = hash_table[q_feature]
            candidate_set.add(matching_candidates)
        k_nearest = self.closest_neighbors(q, candidate_set)

    def closest_neighbors(self, q, candidate_set):
        distances = []
        for candidate in candidate_set:
            distance = self.distance_metric(q, candidate)
            distances.append((distance, candidate))
        distances.sort()
        return [distances[i][1] for i in range(self.k)]



