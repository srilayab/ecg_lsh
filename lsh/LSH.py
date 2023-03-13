import math
class LSH:

    '''
    hash_family: LSH hash family
    k: number of neighbors
    L: number of hash_functions
    '''
    def __init__(self, data, hash_family, k):
        self.data = data
        self.hash_family = hash_family(data)
        self.k = k
        self.L = 5
        self.hash_tables = self.hash_family.get_hash_tables()


    def query(self, q):
        q_hash = self.hash_family.hash(q)
        candidate_set = set()
        for l in range(self.L):
            q_feature = q_hash[l]
            if q_feature == math.inf:
                continue
            hash_table = self.hash_tables[l]
            if q_feature not in hash_table:
                continue
            matching_candidates = hash_table[q_feature]
            candidate_set.update(candidate[0] for candidate in matching_candidates)
        k_nearest = self.closest_neighbors(q, candidate_set)
        return k_nearest

    def closest_neighbors(self, q, candidate_set):
        q = q[0].tolist()
        distances = []
        for i in candidate_set:
            candidate = self.data[i][0].tolist()
            distance = self.euclidean(q, candidate)
            distances.append((distance, i))
        distances.sort()
        return [distances[i][1] for i in range(self.k)]

    def euclidean(self, list1, list2):
        inside_squares = [(a-b) ** 2 for a, b in zip(list1, list2)]
        return sum(inside_squares) ** .5



