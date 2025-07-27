from typing import List, Union
import math
from functools import reduce
def lcm (a : int, b : int) -> int:
    return abs(a*b) // math.gcd(a, b)


def canbeSame (numbers : List[int]) -> Union[List, bool]:
    if 0 in numbers:
        return False
    
    target = reduce(lcm , numbers)

    return all(target % x == 0 for x in numbers)
    
print(canbeSame([50, 75, 100]))

