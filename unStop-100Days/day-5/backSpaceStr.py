def backSpaceString (word1 : str, word2 : str ) -> bool:
    act1, act2 = [], []
    i, j = 0,0 
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            if word1[i] == "#":
                if act1:
                    act1.pop()
            else:
                act1.append(word1[i]) 
        i += 1

        if j < len(word2):
            if word2[j] == "#":
                if act2:
                    act2.pop()
            else:
                act2.append(word2[j])

        j += 1

    return act1 == act2

print(backSpaceString("ab#c", "ad#b#c"))
    