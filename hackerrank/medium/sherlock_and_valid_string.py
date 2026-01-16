def isValid(s):
    freq_map = list(Counter(s).values())
    freq_count = Counter(freq_map)
    if len(freq_count)==1:
        return "YES"
    if len(freq_count)>2:
        return "NO"
    if len(freq_count)==2:
        freq_values = list(freq_count.values())
        freq_keys = list(freq_count.keys())
        if (freq_values[0]==1 and freq_keys[0]==1) or (freq_values[1]==1 and freq_keys[1]==1):
            return "YES"
        if abs(freq_keys[0] - freq_keys[1]) == 1 and (freq_count[max(freq_keys[0], freq_keys[1])] == 1):
            return "YES"
    else:
        return "NO"
    return "NO"

