def minimumSwaps(arr):
    n = len(arr)
    swaps = 0
    i = 0 
    while i<n:
        correct_idx = i+1
        if arr[i]!=correct_idx:
            swap_idx = arr[i]-1
            arr[i], arr[swap_idx] = arr[swap_idx], arr[i]
            swaps+=1
        else:
            i+=1
    return swaps
