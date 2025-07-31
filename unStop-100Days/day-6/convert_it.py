
def convert_it (nums : list) -> list:
    currentMax = float('-inf')
    for i in range(len(nums)):
        current = nums[i]
        currentMax = max(currentMax, current )
        nums[i] += currentMax 

    return nums



print(convert_it([1,2,3]))
        
