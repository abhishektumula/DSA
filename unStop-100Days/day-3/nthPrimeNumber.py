import time 
def nthPrimeNumber (n : int) -> int:
    start_time = time.time()
    currentPrimes = [2]
    number = 3
    while number and len(currentPrimes) != n:
        flag = False
        for i in range(2, number):
            if number % i == 0:
                flag = True
                break 
        if not flag:
            currentPrimes.append(number)
            

        number += 1

    print(currentPrimes)
    _prime = currentPrimes[-1]
    cSum = 0
    while _prime:
        cSum += (_prime % 10)
        _prime //= 10 
    end_time = time.time()
    print(f"runtime : {(end_time - start_time) * 1000:3f}ms")
    return f"sum of {n}th prime Number is {cSum}"


print(nthPrimeNumber(10000))

            

        
