
from typing import List 
from collections import Counter

class Solutiom:
    def majoryElement(self, nums : List) :
        ctr = Counter(nums)
        ctr = sorted(ctr.items() , key=lambda x: x[1], reverse= True )
        return ctr[0][1]
        

cl = Solutiom() 
print(cl.majoryElement([1,4,2,5,3,3,6,3,7,4,8,9,5,1,3]))
print(cl.majoryElement([3,2,3]))
