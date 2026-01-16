import string
def sherlockAndAnagrams(s):
    # hashmap to store signatures
    signatures = {}
    ALPHABET = string.ascii_lowercase
    signature = [0 for _ in ALPHABET]
    for l in s:
        signature[ord(l)-ord(ALPHABET[0])] += 1
    
    # For all substrings
    for start in range(len(s)):
        for end in range(start, len(s)):
            signature = [0 for _ in ALPHABET]
            for l in s[start:end+1]:
                signature[ord(l)-ord(ALPHABET[0])] += 1 
            signature = tuple(signature)
            signatures[signature] = signatures.get(signature, 0) + 1
    count = 0
    for n in signatures.values():
        count += n*(n-1)/2
    return int(count)
