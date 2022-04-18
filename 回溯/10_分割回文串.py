# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/4/19 0:07


"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。

 

示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]
 

提示：

1 <= s.length <= 16
s 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def dfs(current_index, values_lst, left_length):
            if left_length == 0:
                ans.append(values_lst)
                return
            for i in range(1, left_length+1):
                tmp_string = s[current_index:current_index+i]
                if tmp_string == tmp_string[::-1]:
                    dfs(current_index+i, values_lst+[tmp_string], left_length-i)
                else:
                    continue
        dfs(0, [], len(s))
        return ans

s = Solution()
print(s.partition("aab"))