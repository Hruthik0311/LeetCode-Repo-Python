class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        length = 0
        for ch in reversed(s):
            if ch == " ":
                break
            length += 1
        return length
