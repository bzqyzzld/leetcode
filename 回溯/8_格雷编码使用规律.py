# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/4/17 0:08


from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        rets = [0]
        head = 1
        for i in range(n):
            for j in range(len(rets)-1, -1, -1):
                rets.append(rets[j] + head)
            head <<= 1
        return rets

s = Solution()
print(s.grayCode(2))
