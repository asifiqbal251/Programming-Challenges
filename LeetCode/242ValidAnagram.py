def isAnagram(s, t):
    """ (str, str) -> bool
    Returns if two strings are anagrams
    >>> isAnagram('anagram', 'nagaram')
    True
    >>> isAnagram('aacc', 'ccac')
    False
    >>> isAnagram('', '')
    True
    >>> isAnagram('a', 'a')
    True
    >>> isAnagram('a', 'aa')
    False
    """ 
    
    # lengths of the strings
    Ls = len(s)
    Lt = len(t)
    
    if Ls == 0 and Lt == 0:
        return True
    if Ls != Lt:
        return False
    
    dictS = {}
    for ch in s:
        if ch in dictS:
            dictS[ch] += 1
        else:
            dictS[ch] = 1 
            
    for ch in t:
        if ch not in dictS:
            return False
        else:
            dictS[ch] -= 1
            
    if max(dictS.values()) > 0:
        return False
    else:
        return True
if __name__ == '__main__':
    import doctest
    doctest.testmod()
