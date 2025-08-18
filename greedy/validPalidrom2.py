# check if given str is palindrome or by deleting atmost 1 char 
#

class Palindrome:
    def isPalindrome(self, s: str, i : int, j : int) -> bool:
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1 

        return True

    def isPalindrome2(self, s : str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)

            left += 1
            right -= 1 

        return True 
cl = Palindrome()
print(cl.isPalindrome2("abebsba"))
