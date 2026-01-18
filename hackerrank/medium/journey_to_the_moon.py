# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#
from collections import defaultdict
import sys

sys.setrecursionlimit(2000000) # Required for deep recursion in find operation

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Union by size (optimization)
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
def journeyToMoon(n, astronaut):
    uf = UnionFind(n)
    for a, b in astronaut:
        uf.union(a, b)

    # Collect the sizes of all country groups
    country_sizes = {}
    for i in range(n):
        root = uf.find(i)
        country_sizes[root] = uf.size[root]
    
    sizes = list(country_sizes.values())

    # Calculate pairs using the iterative summation method
    result = 0
    sum_sizes = 0
    for size in sizes:
        result += sum_sizes * size
        sum_sizes += size
        
    return result
