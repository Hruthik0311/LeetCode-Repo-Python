class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        digits1 = [ord(c) - 48 for c in num1]
        digits2 = [ord(c) - 48 for c in num2]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = digits1[i] * digits2[j]
                sum_val = mul + res[i + j + 1]
                res[i + j + 1] = sum_val % 10
                res[i + j] += sum_val // 10
        start = 0
        while start < len(res) - 1 and res[start] == 0:
            start += 1
        return ''.join(map(str, res[start:]))
