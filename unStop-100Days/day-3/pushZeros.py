def pushZeros (nums : list) -> list :
    result = []
    count = 0 
    for each in nums:
        if each == 0:
            count += 1 
        else:
            result.append(each)

    result.extend([0] * count)

    return result


print(pushZeros([1,0,2,0,3,0,4]))