#Given an array of strings strs, group all anagrams together into sublists. 
#You may return the output in any order.An anagram is a string that contains 
#the exact same characters as another string, but the order of the characters can be different.
from collections import defaultdict
from collections import Counter
def group_anagrams(words : list)->list:
    result = []
    master = defaultdict(list)
    for eachvalue in words:
        origin = [0] * 26
        for each in eachvalue:
            origin[ord(each) - ord('a')] += 1
#        print(origin)
        master[tuple(origin)].append(eachvalue)
    for key, value in master.items():
        result.append(value)
    return result
print(group_anagrams(['act',"cat", 'stop','tops','hat','post']))

