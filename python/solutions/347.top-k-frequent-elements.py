#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start

# Solution #1: Map + sort
# Time Complexity: O (nlogn)
# Space Complexity: O(n)
# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         num_map = {}

#         for i in range(len(nums)):
#             num_map[nums[i]] = 1 + num_map.get(nums[i], 0)

#         sorted_nums = sorted(num_map.items(), key=lambda x: x[1], reverse=True)
#         print(sorted_nums)

#         return ([sorted_nums[i][0] for i in range(k)])

# Solution #2: Bucket sort using array of size = len(nums) + 1 where index = frequency and value = list of numbers
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for num, count in counts.items():
            frequency[count].append(num)

        result = []
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result


sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))

# @lc code=end
