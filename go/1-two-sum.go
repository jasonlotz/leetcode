package main

/*
Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Link: https://leetcode.com/problems/two-sum/

Solution:
Use hashmap

Time complexity: O(n)
Space complexity: O(n)
*/
func twoSum(nums []int, target int) []int {
	// Create a map to store the index of the number
	indexMap := make(map[int]int)

	// Iterate through the array
	for currIndex, currNum := range nums {
		// If the required complement is present in the map, return the index
		if requiredIdx, isPresent := indexMap[target-currNum]; isPresent {
			return []int{requiredIdx, currIndex}
		}
		// Else, store the index of the current number
		indexMap[currNum] = currIndex
	}
	// If no solution is found, return an empty array
	return []int{}
}
