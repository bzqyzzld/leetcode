# -*- coding: utf-8 -*-
# Author: LD
# CreateTime: 2022/4/26 23:44

"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

 

示例 1：



输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1
 

提示：

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        max_height = 0
        for i in range(len(height)-1):
            if i == 0:
                max_height = height[i]
            else:
                if height[i] < max_height:
                    continue
            for j in range(i, len(height)):
                width = j - i
                high = min((height[i], height[j]))
                ans = ans if ans > width * high else width * high

        return ans

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))


# 双指针的写法
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        ans = 0
        while left < right:
            area = (right - left) * min((height[left], height[right]))
            ans = max((area, ans))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans



s = Solution2()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))