#Assume you are an awesome parent and want to give your children some cookies. 
#But, you should give each child at most one cookie.
#Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
#and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. 
#Your goal is to maximize the number of your content children and output the maximum number.

from typing import List


def assignCookies(greedFactor : List[int], cookies : List[int]) -> int:
    greedFactor.sort()
    cookies.sort()
    result = 0
    for each in cookies:
        for i in range(len(greedFactor)):
            # if greedvalue is less than or equal to the cookies, then they can be assigned with that cookie, 
            # btw remove the greedvalue from greedFactor, yeahh..?:
            if each >= greedFactor[i]:
                result += 1
                greedFactor.pop(i)
                break
            # if the greedvalue is greater than the cookie value,none of the upcoming greedFactor satisfy the value,
            # because it is sorted.. you know what i mean
            if each < greedFactor[i]:
                break

    return result


print(assignCookies([1,1,1], [1,2,3]))
