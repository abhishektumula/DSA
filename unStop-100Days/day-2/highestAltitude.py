def highestAltitude(n, arr):
    result = 0 
    sub = 0
    for each in arr :
        sub += each 
        result = max(sub, result)

    return result  # Placeholder return

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = highestAltitude(n, arr)
    print(result)