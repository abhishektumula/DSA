#NOTE: create a string from each nodevalues,
#NOTE: check if the generated string is palindrome or not 
#NOTE: if palindrome return True or return False 
#NOTE: to check palindrome, use two-pointer approcah or ::-1 
#NOTE: Don't fuck this ThePrimeab

def palindromeLL(head ) :
#    These are not specifically needed, you can consider these as the edgecases
#    if not head:
#        return True
#    if head and not head.next:
#        return True 
    s = ""
    while n:
        s += str(n.val)
        n = n.next 

    return s.strip() == s[::-1].strip()


