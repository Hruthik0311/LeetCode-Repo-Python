class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        prev = [False] * (m + 1)
        prev[0] = True
        for j in range(1, n + 1):
            curr = [False] * (m + 1)
            if p[j - 1] == '*':
                curr[0] = prev[0]
            for i in range(1, m + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    curr[i] = prev[i - 1]
                elif p[j - 1] == '*':
                    curr[i] = curr[i - 1] or prev[i]
            prev = curr
        return prev[m]
