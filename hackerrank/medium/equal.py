def min_operations(diff):
    operations = 0
    operations += diff // 5
    diff %= 5
    operations += diff // 2
    diff %= 2
    operations += diff // 1
    return operations
def equal(arr):
    min_val = min(arr)
    min_ops = sys.maxsize
    for target in range(min_val-4, min_val+1):
        curr_ops = 0
        for num in arr:
            curr_ops += min_operations(num-target)
        min_ops = min(curr_ops, min_ops)
    return min_ops
