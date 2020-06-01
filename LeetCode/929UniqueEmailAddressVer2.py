def numUniqueEmails(emails):
    """ (list) -> int
    Returns the number of unique and correctly formatted emails from a list of emails
    >>> numUniqueEmails(["test.email+alex@leetcode.com", "test.email@leetcode.com"])
    1
    >>> numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com", \
    "testemail+david@lee.tcode.com", "testemail+da@lee.tcode.com"])
    2
    """
    L = len(emails)
    
    for i in range(L):
        # split the  email on '@' and retrieve the domain
        domain = emails[i].split('@')[1]
        # split the email on '+' and only take the split before '+' (the first split)
        local_before_plus = emails[i].split('+')[0]
        # remove every '.' in the local address
        local_without_dot = local_before_plus.replace('.','')
        # split the local on '@' and only take the first split as the local may contain '@' if '+' doesn't exist
        local_without_dot_and_at = local_without_dot.split('@')[0]
        # construct the email address
        emails[i] = local_without_dot_and_at+'@'+domain
    return len(set(emails))

if __name__=='__main__':
    import doctest
    doctest.testmod()       
        
        
