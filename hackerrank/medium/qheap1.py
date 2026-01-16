import sys
import heapq

class Heap:
    def __init__(self):
        self.min_heap = []
        self.counts = {}
        
    def insert(self, val):
        heapq.heappush(self.min_heap, val)
        self.counts[val] = self.counts.get(val, 0) + 1

    def delete(self, val):
        if self.counts[val]>0:
            self.counts[val]-=1
        while self.min_heap and self.counts.get(self.min_heap[0], 0) == 0:
            heapq.heappop(self.min_heap)
    
    def minimum(self):
        return str(self.min_heap[0]) if self.min_heap else None

if __name__ == '__main__':
    # the first line contains integer
    integer1 = int(input())

    # the second line contains the space separated list of integers
    int_lst = [list(map(int, input().split())) for _ in range(integer1)]
    heap = Heap()
    for query_parts in int_lst:
        if query_parts[0]==3:
            sys.stdout.write(f'{heap.minimum()}\n')
        elif query_parts[0]==1:
            heap.insert(query_parts[1])
        elif query_parts[0] == 2:
            heap.delete(query_parts[1])

