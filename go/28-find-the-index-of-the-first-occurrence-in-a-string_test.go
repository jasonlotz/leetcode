package main

import "testing"

func TestStrStr(t *testing.T) {
	tests := []struct {
		haystack string
		needle   string
		expected int
	}{
		{"leetcode", "leeto", -1},
		{"sadbutsad", "sad", 0},
	}
	for _, test := range tests {
		if result := strStr(test.haystack, test.needle); result != test.expected {
			t.Errorf("strStr(%v, %v) = %v, want %v", test.haystack, test.needle, result, test.expected)
		}
	}
}
