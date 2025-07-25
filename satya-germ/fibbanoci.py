def fibbanoci (n : int ) -> list:
    if n <= 1:
        return n
    result = [0, 1]
    while len(result) != n :
        result.append(result[-1] + result[-2])
    print(result)
    return result[-1]


print(fibbanoci(10))


