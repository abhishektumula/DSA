#TODO: initialize a set to store all the seen values from the linkedlist
#TODO: if head is not given then return False as it doent contains any cycle in it 
#TODO: iterate throught the each node and check wheather if the node is in the seen set()
#TODO: if yes, then return True as there is a cycle detected
#TODO: else return False , as there is no cycle detected


def cycle_detectiona(head : number):
    mapset = set() # seen set 
    if not head:
        return False 
    
    n = head 
    while n:
        if n in mapset:
            return True
        else:
            mapset.add(n)
            n = n.ref 
    return False 


