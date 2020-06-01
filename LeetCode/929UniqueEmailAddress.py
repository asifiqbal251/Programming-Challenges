def numUniqueEmails(emails):
    """ (list) -> int
    returns 
    """
    L = len(emails)
    for i in range(L):
        # split the email on '+' and only take the first split
        local_before_plus = emails[i].split('+')[0]
        # remove every . in local address
        local_without_dot = local_before_plus.replace('.','')
        # split the local on '@' and only take the first split as the local may contain '@'
        local_without_dot_at = local_without_dot.split('@')[0]
        domain = emails[i].split('@')[1]
        emails[i] = local_without_dot_at+'@'+domain
    return len(set(emails))
            
lis=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com",\
     "testemail+david@lee.tcode.com"]

print(lis)
print(numUniqueEmails(lis))
        
        
