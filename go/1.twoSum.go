/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 */

package main

// @lc code=start

// Solution 1: Use hashmap
// Time complexity: O(n)
// Space complexity: O(n)
func twoSum(nums []int, target int) []int {
	indexMap := make(map[int]int)
	for currIndex, currNum := range nums {
		if requiredIdx, isPresent := indexMap[target-currNum]; isPresent {
			return []int{requiredIdx, currIndex}
		}
		indexMap[currNum] = currIndex
	}
	return []int{}
}

// func main() {
// 	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
// 	fmt.Println(twoSum([]int{3, 2, 4}, 6))
// 	fmt.Println(twoSum([]int{3, 3}, 6))
// }

// @lc code=end
