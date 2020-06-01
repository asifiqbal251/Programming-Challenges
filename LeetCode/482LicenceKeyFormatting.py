def licenseKeyFormatting(S, K):
    """ (str, int) -> str
    Returns the formatted license key
    >>> licenseKeyFormatting('5F3Z-2e-9-w', 3)
    '5F-3Z2-E9W'
    >>> licenseKeyFormatting("2-5g-3-J", 2)
    '2-5G-3J'
    """
    # remove '-' and convert lowercase letters to uppercase
    SNoDash = S.replace('-', '')
    SNoDashUpper = SNoDash.upper()
    # number of groups (K or K + 1)
    noOfGroups = len(SNoDashUpper)//K + 1*(len(SNoDashUpper)%K != 0)
    # length of the first term (<= K)
    lenOfHead = len(SNoDashUpper) - K*(noOfGroups-1)
    DL = SNoDashUpper[:lenOfHead]
    # rest of the terms (except the first term)
    for i in range(1, noOfGroups):
        DL = DL + '-' + SNoDashUpper[lenOfHead + (i-1)*K : lenOfHead + i*K]
    return DL

if __name__=='__main__':
    import doctest
    doctest.testmod()       
        
        
