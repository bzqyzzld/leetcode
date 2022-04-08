# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/4/9 0:35


"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(left, strings, right):
            if left == n:
                ans.append(strings + (n - right) * ")")
                return
            if left == 0:   # 如果没有左括号,必须第一个是左括号
                dfs(left+1, strings + "(", right)
            else:
                dfs(left+1, strings + "(", right)
                if right < left:
                    dfs(left, strings + ")", right+1)

        dfs(0, "", 0)
        return ans


solution = Solution()
print(solution.generateParenthesis(3))


