#
# @lc app=leetcode id=2706 lang=python3
#
# [2706] Buy Two Chocolates
#

# @lc code=start

# Solution 1: Sort the list of prices and use the top two prices to buy two chocolates
# Time Complexity: O(nlogn) for sorting
# Space Complexity: O(n) for sorting
class Solution:
  def buyChoco(self, prices: list[int], money: int) -> int:
    prices.sort()
    one, two, = prices[0], prices[1]

    min_cost = one + two
    if min_cost > money:
      return money
    else:
      return money - min_cost


# @lc code=end
