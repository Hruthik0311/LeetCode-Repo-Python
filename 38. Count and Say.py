class Solution:
    def countAndSay(self, n: int) -> str:
        def rle_encode(s: str) -> str:
            result = []
            count = 1
            for i in range(1, len(s) + 1):
                if i < len(s) and s[i] == s[i - 1]:
                    count += 1
                else:
                    result.append(str(count))
                    result.append(s[i - 1])
                    count = 1
            return "".join(result)
        term = "1"
        for _ in range(1, n):
            term = rle_encode(term)
        return term
