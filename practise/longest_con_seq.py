def longest_sequence(numbers : list) -> int:
    numbers.sort()
    ans = 0
    for each in numbers:
        count = 1
        each += 1
        while each in numbers:
            each += 1
            count += 1
        
        ans = max(ans, count)

    return ans 

print(longest_sequence([1,2,3,4,5,6,7,9,10,11,12,16,19,18,17,20]))


