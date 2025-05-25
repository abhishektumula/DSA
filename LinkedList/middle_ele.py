#NOTE: find the number of ele in the given ll using the any variable , probably count
#NOTE: find the center of the count-variable, if i have 2 values like median consider the second value 
#NOTE: then return the ll staring from the cneter or middle of the count variable
#NOTE: 
#NOTE: just do it NOW...

def middleEle(number) :
    count = 0
    if not head:
        return None 
    n = head
    while n:
        count += 1
        n = n.next 
    midValue =count//2

    for _ in range(midValue):
        head = head.next 

    return head
