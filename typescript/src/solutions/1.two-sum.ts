/*
 * @lc app=leetcode id=1 lang=typescript
 *
 * [1] Two Sum
 */

// @lc code=start

// Solution: Hashmap
// Time complexity: O(n)
// Space complexity: O(n)
function twoSum(nums: number[], target: number): number[] {
  const hashmap: Record<number, number> = {};

  for (let i = 0; i < nums.length; i++) {
    const value = nums[i];
    const complement = target - value;

    if (hashmap[complement] !== undefined) {
      return [hashmap[complement], i];
    }

    hashmap[value] = i;
  }

  return [];
}

// Test cases:
const test1 = twoSum([2, 7, 11, 15], 17);
console.log(test1);
// @lc code=end
