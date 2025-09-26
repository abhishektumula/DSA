from typing import List


class Solution:
    def longestSubString(self, s: str) -> int:
        visited = set()
        currMax = 0
        i = 0
        for x in range(len(s)):
            while s[x] in visited:
                visited.remove(s[i])
                i += 1
            visited.add(s[x])
            currMax = max(currMax, x - i + 1)

        return currMax
        # this shit is not working, IDK why
        # for x in range(len(s)):
        #     while s[x] in visited:
        #         visited.remove(s[x])
        #         i += 1
        #     visited.add(s[x])
        #     currMax = max(currMax, x - i - 1)
        # return currMax


cl = Solution()
print(cl.longestSubString("zxyzxyz"))
