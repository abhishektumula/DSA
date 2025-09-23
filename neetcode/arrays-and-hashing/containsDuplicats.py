
from typing import List


def containsDuplicates(nums : List) -> bool:
    hashing = set()
    for eh in nums:
        if eh in hashing:
            return True 
        hashing.add(eh)
    return False 









