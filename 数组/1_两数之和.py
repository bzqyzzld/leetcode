# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/4/23 0:14


"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 使用字典
        ans = []
        dic_tmp = dict()
        for index, val in enumerate(nums):
            if dic_tmp:
                diff = target - val
                if diff in dic_tmp:
                    ans.append(index)
                    ans.append(dic_tmp[diff])
                else:
                    dic_tmp[val] = index
            else:
                dic_tmp[val] = index

        return ans

s = Solution()
print(s.twoSum([3, 2, 4], 6))
