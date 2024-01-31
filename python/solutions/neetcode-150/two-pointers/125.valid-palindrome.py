#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start

# Solution 1: Use two pointers
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        lowerString = s.lower()

        while left < right:
            if not lowerString[left].isalnum():
                left += 1
                continue

            if not lowerString[right].isalnum():
                right -= 1
                continue

            if lowerString[left] != lowerString[right]:
                return False

            left += 1
            right -= 1

        return True


# Solution 2: Compare two filtered lists
# Space complexity: O(n)
# Time complexity: O(n)
# def isPalindrome(self, s: str) -> bool:
#     filtered_chars = filter(lambda ch: ch.isalnum(), s)
#     lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

#     filtered_chars_list = list(lowercase_filtered_chars)
#     reversed_chars_list = filtered_chars_list[::-1]

#     return filtered_chars_list == reversed_chars_list

# @lc code=end
