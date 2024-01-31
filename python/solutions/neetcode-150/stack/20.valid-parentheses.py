#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

# Solution #1: Using stack
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpenMap = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in closeToOpenMap:
                if stack and stack[-1] == closeToOpenMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False


sol = Solution()
print(sol.isValid("()[]{}"))

# @lc code=end
