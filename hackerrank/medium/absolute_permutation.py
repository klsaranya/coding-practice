def absolutePermutation(n, k):
    if k==0:
        return [c+1 for c in range(n)]
    if n%(2*k)!=0:
        return [-1]
    result = []
    for i in range(1, n + 1, 2 * k):
        # First half of the block: j + k
        for j in range(i, i + k):
            result.append(j + k)
        # Second half of the block: j - k
        for j in range(i + k, i + 2 * k):
            result.append(j - k)
            
    return result
