#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        result = []

        def backtrack(left, right):
            if left == right == n:
                result.append("".join(stack))
                return

            if left < n:
                stack.append("(")
                backtrack(left + 1, right)
                stack.pop()

            if right < left:
                stack.append(")")
                backtrack(left, right + 1)
                stack.pop()

        backtrack(0, 0)

        return result
# @lc code=end
