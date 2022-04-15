# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/4/14 23:44


"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

 

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        used = [0] * len(nums)

        def dfs(current_depth, max_depth, indexes_lst, used):
            if current_depth == max_depth:
                ans.append([nums[i] for i in indexes_lst])
                return
            for i in range(len(nums)):
                if i in indexes_lst:
                    continue
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == 0:
                    continue
                used[i] = 1
                dfs(current_depth+1, max_depth, indexes_lst+[i], used)
                used[i] = 0

        dfs(0, len(nums), [], used)
        return ans


s = Solution()
print(s.permuteUnique([1, 1, 2]))
