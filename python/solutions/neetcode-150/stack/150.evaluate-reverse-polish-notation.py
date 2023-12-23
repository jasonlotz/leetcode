#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start

# Solution: Use stack to store the numbers and pop them when we encounter an operator.
#   For division and substraction, we need to be careful about the order of the numbers.
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
  def evalRPN(self, tokens: list[str]) -> int:
    stack = []

    for token in tokens:
      if token == '+':
        stack.append(stack.pop() + stack.pop())
      elif token == '-':
        a, b = stack.pop(), stack.pop()
        stack.append(b - a)
      elif token == '*':
        stack.append(stack.pop() * stack.pop())
      elif token == '/':
        a, b = stack.pop(), stack.pop()
        stack.append(int(b / a))
      else:
        stack.append(int(token))

    return stack.pop()
# @lc code=end


sol = Solution()
print(sol.evalRPN(["10", "6", "9", "3", "+", "-11",
                   "*", "/", "*", "17", "+", "5", "+"]))
