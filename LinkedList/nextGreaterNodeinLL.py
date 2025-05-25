#NOTE: convert the linked list into the array aka list
#NOTE: then iterare througth the values in the array/list and find next > value 
#NOTE: repeat the process,and store the values in the an array AKA list
#NOTE: return list when finished
#NOTE: functions expects list[int] btw..

def nextGreater(head) -> list[int]:
    numbers = []
    n = head
    while n:
        numbers.append(n.val) #n.data also used in some implementaions...
        n = n.next            #n.ref also used in some implementaions...
    res = []
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                res.append(numbers[j])
                break
    return res

    
