#approch - 1: brute force, by checking every possible combination
def two_sum(numbers : list, target : int ) ->  any:
    numbers.sort()
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return f"index values -->{[i,j]}"
            print(f"{numbers[i], numbers[j]} != {target}")
    return False
print(two_sum([1,2,3,4,5,6], 11))
