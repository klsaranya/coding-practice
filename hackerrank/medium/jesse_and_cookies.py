def cookies(k, A):
    heapq.heapify(A)
    count = 0
    while len(A)>1 and A[0]<k:
        val1 = heapq.heappop(A)
        val2 = heapq.heappop(A)
        new_val = val1 + 2*val2
        heapq.heappush(A, new_val)
        count+=1
    return count if A[0]>=k else -1
