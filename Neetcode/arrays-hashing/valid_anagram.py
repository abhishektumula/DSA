#approach 1 - manual count using dictionaries 
def valid_anagram(word1, word2) -> bool:
    dw1, dw2 = {}, {}
    word1, word2 = word1.replace(" ",""), word2.replace(" ", "")
    for each in word1:
        if each not in dw1:
            dw1[each] = 1
        else:
            dw1[each] += 1

    for each in word2:
        if each not in dw2:
            dw2[each] = 1
        else:
            dw2[each] += 1
#    print(sorted(dw1.items()) , sorted(dw2.items()))
    return sorted(dw1.items()) == sorted(dw2.items())

#approach 2 : comparing ele using set()

def valid_anagram_sets(word1, word2) -> bool:
    origin = set(word1)
    word1, word2 = word1.replace(" ",""), word2.replace(" ", "")
    for each in origin:
        if word1.count(each) != word2.count(each):
            return False
    
    if len(word1) == len(word2):
        return True
    return False
       
print(valid_anagram('xx','x' ))
print(valid_anagram_sets('xx', 'x'))

