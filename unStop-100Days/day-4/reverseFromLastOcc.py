def reverseFromLastOcc (word : str, target : str) -> str:
    reverse = ""
    for i in range(len(word)-1, -1, -1):
        ele = word[i]
        reverse += ele
        word = word[:-1]
        if ele == target:
            word += reverse 
            return word
        
    return word

# print(reverseFromLastOcc("abc", "c"))
print(reverseFromLastOcc("abxcced", "c"))
