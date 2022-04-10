# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/4/10 23:09

"""
无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。

示例1:

 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
示例2:

 输入：S = "ab"
 输出：["ab", "ba"]
提示:

字符都是英文字母。
字符串长度在[1, 9]之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-i-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def permutation(self, S: str) -> List[str]:
        length = len(S)
        ans = []

        def dfs(current_depth, max_depth, indexes_lst):
            if current_depth == max_depth:
                ans.append("".join([S[j] for j in indexes_lst]))
                return
            for m in range(length):
                if m in indexes_lst:
                    continue
                else:
                    dfs(current_depth+1, max_depth, indexes_lst + [m])

        for i in range(length):
            dfs(1, length, [i])

        return ans


s = Solution()
print(s.permutation("abc"))

