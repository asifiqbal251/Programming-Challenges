def licenseKeyFormatting(S, K):
    """ (str, int) -> str
    Returns the formatted license key
    >>> licenseKeyFormatting('5F3Z-2e-9-w', 3)
    '5F-3Z2-E9W'
    >>> licenseKeyFormatting("2-5g-3-J", 2)
    '2-5G-3J'
    """
    # Remove '-' and convert lowercase to uppercases
    SNoDash = S.replace('-','')
    SNoDashUpper = SNoDash.upper()
    lenOfHead = len(SNoDashUpper)%K
    idx, DLFormatted = 0, []
    if lenOfHead != 0:
        idx = lenOfHead
        DLFormatted.append(SNoDashUpper[: idx])
    while idx < len(SNoDashUpper):
        DLFormatted.append(SNoDashUpper[idx : idx+K])
        idx += K
    return '-'.join(DLFormatted)

if __name__ == '__main':
    import doctest
    doctes.testmod()
