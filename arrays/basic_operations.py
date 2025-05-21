# basic operations of arrays are implemented in this file
# it includes:
# 1. append
# 2. insert
# 3. remove
# 4. pop
# 5. index
# 6. count
# 7. reverse
# 8. sort
# 9. extend
# 10. copy
# 11. clear
# 12. slice
# 13. concatenate
# 14. repeat
# 15. membership
# 16. length
# 17. min
# 18. max
# 19. sum
# 20. average
# 21. median
# 22. mode
# 23. standard deviation
# 24. variance
# 25. range
arr1, arr2 = [], []

def append_operation(arr1:list, values:int)-> list:
    # append operations adds the element to the end of the list
    arr1.append(values)
    return arr1

def pop_operation(arr1):
# pop operations remove the last element from the list
    if not arr1:
        return f"pop cannot be performed on empty list"

    return arr1.pop() 

def removeDuplicates(arr1 : list) -> list:
    result = []    
    for eachvalue in arr1:
        if eachvalue not in result:
            result = append_operation(result, eachvalue)

    return f"removed duplicates : {arr1} --> {result}"

def insertOperation(arr1 : list, position : int, values : int) -> list:
    if not arr1:
        print(f"enterd [if not arr1] condition")
        arr1 = append_operation(arr1, values)
    else:
        print(f"enterd [else] condition")
        arr1.insert(position, values)
    return arr1

def sum_operation(arr1) -> any:
    return sum(arr1)

def mean_operation(arr1):
    return sum_operation(arr1) / len(arr1)

def median_operation(arr1):
    if not arr1:
        return 0
    else:
        arr1.sort()
        n = len(arr1)
        if n % 2 != 0:
            return f"median of {arr1} is {arr1[n//2]}"
        ele = n // 2
        x, y = arr1[ele], arr1[ele - 1]
        return f"median of {arr1} is {(x+y)/2}"



print(append_operation(arr1, 10))
print(append_operation(arr1, 20))
print(append_operation(arr1, 30))
print(append_operation(arr1, 40))
print(append_operation(arr1, 50)) 
print(append_operation(arr1, 60))
print(append_operation(arr1, 10))
print(removeDuplicates(arr1))
print(insertOperation(arr2, 10, 10))
print(insertOperation(arr2, 0, 100))
print(sum_operation(arr1))
print(sum_operation(arr2))
print(mean_operation(arr1))
print(median_operation(arr1))













