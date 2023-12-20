#
# @lc app=leetcode id=2706 lang=python3
#
# [2706] Buy Two Chocolates
#

# @lc code=start

# Solution 1: Sort the list of prices and use the top two prices to buy two chocolates
# Time Complexity: O(nlogn) for sorting
# Space Complexity: O(n) for sorting
# class Solution:
#   def buyChoco(self, prices: list[int], money: int) -> int:
#     prices.sort()
#     one, two, = prices[0], prices[1]

#     min_cost = one + two
#     if min_cost > money:
#       return money
#     else:
#       return money - min_cost


# Solution 2: Find the two minimum prices in one pass and use them to buy two chocolates
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
  def buyChoco(self, prices: list[int], money: int) -> int:
    minimum = min(prices[0], prices[1])
    second_minimum = max(prices[0], prices[1])

    for i in range(2, len(prices)):
      if prices[i] < minimum:
        second_minimum = minimum
        minimum = prices[i]
      elif prices[i] < second_minimum:
        second_minimum = prices[i]

    min_cost = minimum + second_minimum

    if min_cost <= money:
      return money - min_cost

    return money

# @lc code=end
