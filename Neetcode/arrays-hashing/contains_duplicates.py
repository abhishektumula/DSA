# approach 1 :  this method uses arrays which takes more time 
# complexity with more number of elements
def contains_duplicates(numbers : list ) -> bool:
    map = []
    for each in numbers:
        if each in map:
            return True
        map.append(each)
    return False

#approach 2 - using sets which have constant time complexity

def contains_duplicates_sets(numbers : list) -> bool:
    map = set()
    for each in numbers:
        if each in map:
            return True
        map.add(each)
    return False

#approach -3 : using len() function...
def contains_duplicates_len(numbers : list) -> bool:
    return len(set(numbers)) != len(numbers)

print(contains_duplicates([1,2,3,3]))
print(contains_duplicates([1,2,3,4]))
print(contains_duplicates([1,2,3,4,4,5]))
print("-> -> -> ->")
print(contains_duplicates_sets([1,2,3,3]))
print(contains_duplicates_sets([1,2,3,4]))
print(contains_duplicates_sets([1,2,3,4,4,5]))
print("-> -> -> ->")
print(contains_duplicates_len([1,2,3,3]))
print(contains_duplicates_len([1,2,3,4]))
print(contains_duplicates_len([1,2,3,4,4,5]))
print("-> -> -> ->")

