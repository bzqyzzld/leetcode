# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/4/7 23:55


# url https://leetcode-cn.com/problems/power-set-lcci/

"""
幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。

说明：解集不能包含重复的子集。

示例:

 输入： nums = [1,2,3]
 输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        ans = []

        def dfs(current_depth, max_depth, indexes_lst, current_index):
            if current_depth == max_depth:
                ans.append([nums[j] for j in indexes_lst])
                return
            for k in range(current_index, length):
                if k in indexes_lst:
                    continue
                else:
                    dfs(current_depth+1, max_depth, indexes_lst + [k], k)

        for i in range(length+1):
            dfs(0, i, [], 0)
        return ans


solution = Solution()
print(solution.subsets([1, 2, 3]))

