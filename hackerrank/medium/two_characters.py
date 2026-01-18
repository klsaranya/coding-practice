def alternate(s):
    unique_chars = set(s)
    max_len = 0
    visit = set()
    for c1 in unique_chars:
        for c2 in unique_chars:
            if c1==c2:
                continue
            ch = "".join(sorted(c1+c2))
            if ch in visit:
                continue
            new_str = removeAllCharsExcpet(s, c1, c2)
            if checkifAlternate(new_str):
                max_len = max(max_len, len(new_str))
            visit.add(ch)
    return max_len

def removeAllCharsExcpet(s, char1, char2):
    res = ""
    for c in s:
        if c==char1 or c==char2:
            res+=c
    return res
    
def checkifAlternate(s):
    # Assumption: only 2 chars exist in s
    is_valid = True
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            is_valid = False
            break
    return is_valid

