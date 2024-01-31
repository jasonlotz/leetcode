#
# @lc app=leetcode id=1758 lang=python3
#
# [1758] Minimum Changes To Make Alternating Binary String
#

# @lc code=start

# Solution 1: Count differences for both start with 0 and 1
# Time: O(n)
# Space: O(1)
class Solution:
    def minOperations(self, s: str) -> int:
        start_0_differences = 0
        start_1_differences = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    start_1_differences += 1
                else:
                    start_0_differences += 1
            else:
                if s[i] == "1":
                    start_1_differences += 1
                else:
                    start_0_differences += 1

        return min(start_1_differences, start_0_differences)


# Solution 2: Count differences for start with 0 and then
#   calculate the differences for start with 1
# Time complexity: O(n) - slightly more efficient than solution 1
# Space complexity: O(1)
# class Solution:
#   def minOperations(self, s: str) -> int:
#     start0 = 0

#     for i in range(len(s)):
#       if i % 2 == 0:
#         if s[i] == "1":
#           start0 += 1
#       else:
#         if s[i] == "0":
#           start0 += 1

#     return min(start0, len(s) - start0)
# @lc code=end
