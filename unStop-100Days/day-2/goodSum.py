import time
# optimal solution using stack..
def goodSumStack (nums : list) -> list:
    stack = []
    for each in nums:
        if each>= 0 :
            stack.append(each)
        else:
            target = abs(each)
            currentSum = 0 
            temp = []

            while stack and currentSum < target:
                rem = stack.pop()
                currentSum += rem 
                temp.append(rem)

            if currentSum >= target:
                pass
            else:
                temp.clear()

            stack.append(target)
    return sum(stack)

print(goodSumStack([1,2,-3, 4,5,-6]))            
print(goodSumStack([-4, -3]))            
                


def goodSum (nums : list) -> list:
    negativeIndexs = [i for i in range(len(nums)) if nums[i] < 0]
    for j in negativeIndexs:
        target = abs(nums[j])
        j -= 1
        currentSum = 0
        idx = []
        found = False
        while j >= 0:
            currentSum += nums[j]
            idx.append(j)
            if currentSum >= target:
                # idx.append(j)
                found = True
                break 
            j -= 1

        if found:
            for j in idx:
                nums[j] = 0 

    return nums


def goodSums (nums : int) -> list:
    print(nums)
    for i in range(len(nums)):
        if nums[i] < 0:
            j , idx = i - 1, []
            currentSum = 0
            while j >= 0 and currentSum < abs(nums[i]):
                currentSum += nums[j]
                j -= 1
            if currentSum >= abs(nums[i]):
                for f in range(j + 1, i ):
                    nums[f] = 0
                
                nums[i] = abs(nums[i])
        
          
    return (nums)



# print(goodSum([4,2,2,3,-6]))
print(goodSums([1,2,-3,4,5,-6]))
