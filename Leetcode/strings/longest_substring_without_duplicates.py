def longest_substring(word : str)->int :
    let = set()
    res = 0
    l = 0

    for i in range(len(word)):
        while word[i] in let:
            let.remove(word[l])
            l += 1

        let.add(word[i])
        res = max(res , i - l + 1)
    
    return res 

print(longest_substring("abcdefabcbdbb"))



            
