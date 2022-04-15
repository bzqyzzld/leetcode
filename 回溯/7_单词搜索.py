# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/4/15 23:30


"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例 1：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
示例 3：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
 

提示：

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board 和 word 仅由大小写英文字母组成
 

进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        length = len(word)
        ans = []
        def dfs(current_depth, max_depth, strings, indexes_lst):
            if strings[current_depth-1] != word[current_depth-1]:
                return
            if current_depth == max_depth:
                ans.append(strings)
                return
            steps = self.get_possible_steps(indexes_lst, board)
            if not steps:
                return
            last_row = indexes_lst[-1][0]
            last_col = indexes_lst[-1][1]
            if "up" in steps:
                dfs(current_depth+1, max_depth, strings+board[last_row-1][last_col], indexes_lst+[(last_row-1, last_col)])

            if "down" in steps:
                dfs(current_depth+1, max_depth, strings+board[last_row+1][last_col], indexes_lst+[(last_row+1, last_col)])

            if "left" in steps:
                dfs(current_depth+1, max_depth, strings+board[last_row][last_col-1], indexes_lst+[(last_row, last_col-1)])

            if "right" in steps:
                dfs(current_depth+1, max_depth, strings+board[last_row][last_col+1], indexes_lst+[(last_row, last_col+1)])


        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(1, length, board[i][j], [(i, j)])

        return word in ans

    def get_possible_steps(self, indexes, board):
        rets = []
        max_rows = len(board)
        max_cols = len(board[0])
        last_row = indexes[-1][0]
        last_col = indexes[-1][1]
        # up
        if last_row - 1 >= 0:
            up_position = (last_row-1, last_col)
            if up_position not in indexes:
                rets.append("up")

        # down
        if last_row + 1 < max_rows:
            down_position = (last_row+1, last_col)
            if down_position not in indexes:
                rets.append("down")

        # left
        if last_col - 1 >= 0:
            left_position = (last_row, last_col - 1)
            if left_position not in indexes:
                rets.append("left")

        # right
        if last_col + 1 < max_cols:
            right_position = (last_row, last_col + 1)
            if right_position not in indexes:
                rets.append("right")

        return rets


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

s = Solution()
print(s.exist(board, word))
