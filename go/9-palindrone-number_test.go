package main

import "testing"

func TestIsPalindrome(t *testing.T) {
	tests := []struct {
		x        int
		expected bool
	}{
		{121, true},
		{-121, false},
		{10, false},
		{-101, false},
	}
	for _, test := range tests {
		if result := isPalindrome(test.x); result != test.expected {
			t.Errorf("isPalindrome(%v) = %v, want %v", test.x, result, test.expected)
		}
	}
}
