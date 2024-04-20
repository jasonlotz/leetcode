package main

func mergeAlternately(word1 string, word2 string) string {
  var result string 
  maxLen := max(len(word1), len(word2))

  for i := 0; i < maxLen; i++ {
    if i < len(word1) {
      result += string(word1[i])
    }
    if i < len(word2) {
      result += string(word2[i])
    }
  }

  return result
}
