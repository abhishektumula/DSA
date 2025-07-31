def sumOfDiffBits (bit1 : str, bit2 : str) -> list :
    if len(bit1) == len(bit2):
        ctr = 0
        i = j = 0 
        while i < len(bit1):
            if bit1[i] != bit2[j]:
                ctr += 1 

            i += 1
            j += 1 
        return ctr 
    
    else:
        n = len(bit1)
        combs = [bit2[i:i +n] for i in range(len(bit2) - n + 1)]
        result = 0
        for each in combs:
            for i in range(len(each)):
                if each[i] != bit1[i]:
                    result += 1 
        return result

    

print(sumOfDiffBits("01", '00111'))
print(sumOfDiffBits("101", '010'))