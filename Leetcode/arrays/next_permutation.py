def next_permutation(original : list ) -> list:
    pivot = -1
    for i in range(len(original)-2, -1, -1):
        if original[i] < original[i + 1]:
            pivot = i 
            break

    if pivot == -1:
        return original[::-1]
    
    for i in range(len(original)-1, pivot, -1):
        if original[i] > original[pivot]:
            original[i], original[pivot] = original[pivot], original[i]
            break

    i, j = pivot + 1, len(original) - 1 
    while i <= j:
        original[i], original[j] = original[j], original[i]
        i += 1
        j -= 1

    return original

print(next_permutation([3,2,1]))
print(next_permutation([1,2,3]))
print(next_permutation([1,2,4,6,5,3]))

