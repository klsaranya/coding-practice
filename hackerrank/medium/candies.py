def candies(n, arr):
    left = [1]*n
    right = [1]*n

    for i in range(1,n):
        if arr[i-1]<arr[i]:
            left[i] = left[i-1] + 1
    for j in range(n-2,-1,-1):
        if arr[j+1]<arr[j]:
            right[j] = right[j+1] + 1
    total = 0
    for i in range(n):
        total += max(left[i],right[i])
    return total
