#approach - using two pointer 
import time 
def validate_sting(x : str) -> str:
    ans = x.replace(" ","").lower()
    res = ""
    for each in ans:
        if each.isalpha():
            res += each

    return res

def valid_palindrome(sentense : str) -> bool:
    strat_time = time.time()
    strs = validate_sting(sentense)
    if strs == "":
        endtime = time.time()
        print(f"runtime:{(endtime - strat_time)*1000:.3f}ms")
        return True
    i, j = 0, len(strs) - 1
    while i <= j :
        if strs[i] != strs[j]:
            endtime = time.time()
            runtime = (endtime - strat_time) * 1000
            print(f"runtime:{runtime:.3f}ms")
            return False
        i += 1
        j -= 1
    endtime = time.time()
    runtime = (endtime - strat_time) * 1000
    print(f"runtime:{runtime:.3f}ms")
    return True

print(valid_palindrome('madam'))
print(valid_palindrome('abhishek'))
print(valid_palindrome('xx'))
print(valid_palindrome('x'))
print(valid_palindrome("."))
