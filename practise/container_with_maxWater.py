def container_with_most_water(levels : list) -> int:
#Input: height = [1,7,2,5,4,7,3,6]
#Output: 36
    waterLevel = 0 
    i, j = 0, len(levels) - 1
    while i < j:
        ele = min(levels[i], levels[j]) * abs(i - j)
        waterLevel = max(ele, waterLevel)
        if levels[i] < levels[j]:
            i += 1 
        else:
            j -= 1

    return waterLevel

print(container_with_most_water([1,7,2,5,4,7,3,6]))
print(container_with_most_water([2,2,2]))
