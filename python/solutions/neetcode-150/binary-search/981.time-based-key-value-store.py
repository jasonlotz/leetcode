#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
# Solution: Binary search
# Time complexity: O(1) for set, O(logn) for get
# Space complexity: O(n)
from collections import defaultdict


class TimeMap:

  def __init__(self):
    self.data = defaultdict(list)

  def set(self, key: str, value: str, timestamp: int) -> None:
    self.data[key].append((value, timestamp))

  def get(self, key: str, timestamp: int) -> str:
    result = ""
    values = self.data.get(key, [])

    left, right = 0, len(values) - 1

    while left <= right:
      mid = (left + right) // 2
      if values[mid][1] <= timestamp:
        result = values[mid][0]
        left = mid + 1
      else:
        right = mid - 1
    return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
