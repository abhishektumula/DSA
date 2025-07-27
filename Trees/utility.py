from typing import List,  Union
import random
def generateList (lenght : int, limits :List[int]) -> List:
    ele = [random.randint(limits[0], limits[1]) for _ in range(lenght)]
    return ele


def uniqueList (lenght : int, limits : List[int]) -> Union[List, bool]:
    ele = []
    if lenght > abs(limits[0] - limits[1]):
        return [i for i in range(1, 11)]

    while len(ele) != lenght:
        gen = random.randint(limits[0], limits[1])
        if gen not in ele:
            ele.append(gen)


    return ele

