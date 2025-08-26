
def isPalindrome(s : str ) -> bool:
    if not s:
        return True 
    i, j = 0, len(s) - 1
    while i <= j :
        if s[i] != s[j]:
            return False 
        else:
            i += 1 
            j -= 1
    return True 

def solution():
    n = input()
    if isPalindrome(n):
        return True 
    return False 
print(solution())

