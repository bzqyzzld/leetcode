# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/4/16 1:16


"""
n 位格雷码序列 是一个由 2n 个整数组成的序列，其中：
每个整数都在范围 [0, 2n - 1] 内（含 0 和 2n - 1）
第一个整数是 0
一个整数在序列中出现 不超过一次
每对 相邻 整数的二进制表示 恰好一位不同 ，且
第一个 和 最后一个 整数的二进制表示 恰好一位不同
给你一个整数 n ，返回任一有效的 n 位格雷码序列 。

 

示例 1：

输入：n = 2
输出：[0,1,3,2]
解释：
[0,1,3,2] 的二进制表示是 [00,01,11,10] 。
- 00 和 01 有一位不同
- 01 和 11 有一位不同
- 11 和 10 有一位不同
- 10 和 00 有一位不同
[0,2,3,1] 也是一个有效的格雷码序列，其二进制表示是 [00,10,11,01] 。
- 00 和 10 有一位不同
- 10 和 11 有一位不同
- 11 和 01 有一位不同
- 01 和 00 有一位不同
示例 2：

输入：n = 1
输出：[0,1]
 

提示：

1 <= n <= 16

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gray-code
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 0, 1, 3, 2
from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        length = 2 ** n
        ans = []
        def dfs(current_depth, max_depth, nums):
            if ans:     # 已经有答案了
                return
            if current_depth == max_depth:
                if self.check_one_diff(nums[0], nums[-1]):
                    ans.append(nums)
                return
            possible_nums = self.get_possible_nums(nums[-1], length-1)
            for i in possible_nums:
                if i in nums:
                    continue
                dfs(current_depth+1, max_depth, nums+[i])
        dfs(1, length, [0])
        return ans[0]

    def check_one_diff(self, num1, num2):
        first = bin(num1)[2:]
        second = bin(num2)[2:]
        diff = 0
        if len(first) <= len(second):
            first = abs(len(second) - len(first)) * "0" + first
        else:
            second = abs(len(second) - len(first)) * "0" + second
        for i in range(len(first)):
            if first[i] != second[i]:
                diff += 1
        return diff == 1

    def get_possible_nums(self, num, max_num):
        rets = []
        m = bin(max_num)[2:]
        length_m = len(m)
        current_num_binary = bin(num)[2:]
        current_num_binary_with_zero = abs(len(current_num_binary) - length_m) * "0" + current_num_binary
        for i in range(len(current_num_binary_with_zero)):
            if current_num_binary_with_zero[i] == "0":
                n = int(current_num_binary_with_zero[:i] + "1" + current_num_binary_with_zero[i+1:], base=2)
            else:
                n = int(current_num_binary_with_zero[:i] + "0" + current_num_binary_with_zero[i+1:], base=2)
            if n <= max_num:
                rets.append(n)
        return rets


s = Solution()
print(s.grayCode(10))

