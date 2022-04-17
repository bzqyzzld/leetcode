# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/4/17 0:41

"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

 

示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
 

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        use_status = 0
        def dfs(current_depth, max_depth, indexes_lst, current_index, status):
            if current_depth == max_depth:
                ans.append([nums[i] for i in indexes_lst])
                return

            for j in range(current_index, len(nums)):
                if j in indexes_lst:
                    continue
                if j > 0 and nums[j] == nums[j-1] and status == 0:
                    continue
                status = 1
                dfs(current_depth+1, max_depth, indexes_lst+[j], j, status)
                status = 0
        for m in range(len(nums)+1):
            dfs(0, m, [], 0, use_status)

        return ans

s = Solution()
print(s.subsetsWithDup([1, 2, 2, 3]))
