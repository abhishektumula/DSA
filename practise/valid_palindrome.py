def valid_palindrome(sent : str) -> bool:
    return sent.strip().replace(" ","") == sent[::-1].strip().replace(" ","")

print(valid_palindrome("madam "))
print(valid_palindrome("aliens neil a"))
print(valid_palindrome("madam "))
print(valid_palindrome("madam "))
print(valid_palindrome("madam "))
print(valid_palindrome("madam "))
print(valid_palindrome("madam "))
print(valid_palindrome("madam "))
