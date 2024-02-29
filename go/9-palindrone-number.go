package main

import "strconv"

/*
Description:
Given an integer x, return true if x is a palindrome , and false otherwise.

Link: https://leetcode.com/problems/palindrome-number/

Solution:

Time complexity:
Space complexity:
*/
func isPalindrome(x int) bool {
	stringX := strconv.Itoa(x)

	if len(stringX) == 1 {
		return true
	}

	if stringX[0] == '-' {
		return false
	}

	for i := 0; i < len(stringX)/2; i++ {
		if stringX[i] != stringX[len(stringX)-1-i] {
			return false
		}
	}

	return true
}
