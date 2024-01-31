#
# @lc app=leetcode id=1637 lang=python3
#
# [1637] Widest Vertical Area Between Two Points Containing No Points
#

# @lc code=start

# Solution: Sort the points by x coordinate and find the max difference between two consecutive points.
# Time complexity: O(nlogn) for sorting
# Space complexity: O(n) for sorting
class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        result = 0

        points.sort(key=lambda x: x[0])

        for i in range(len(points) - 1):
            width = points[i + 1][0] - points[i][0]
            result = max(result, width)

        return result


assert (Solution().maxWidthOfVerticalArea(
    [[8, 7], [9, 9], [7, 4], [9, 7]]) == 1)

assert (Solution().maxWidthOfVerticalArea(
    [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]) == 3)

# @lc code=end
