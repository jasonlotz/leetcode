#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#

# @lc code=start

# Solution: Use a delimiter of count of characters in string + '#' + string
class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return result


codec = Codec()
input = ["hello", "world", "this", "is", "a", "test"]
encoded = codec.encode(input)
decoded = codec.decode(encoded)

print(encoded)
print(decoded)


# @lc code=end
