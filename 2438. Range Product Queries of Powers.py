class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        powers = []
        bit = 0
        x = n
        while x:
            if x & 1:
                powers.append(pow(2, bit, MOD))
            x >>= 1
            bit += 1
        if not powers:
            return [1] * len(queries)
        prefix = [0] * len(powers)
        prefix[0] = powers[0] % MOD
        for i in range(1, len(powers)):
            prefix[i] = (prefix[i - 1] * powers[i]) % MOD
        inv_prefix = [0] * len(prefix)
        for i in range(len(prefix)):
            inv_prefix[i] = pow(prefix[i], MOD - 2, MOD)
        res = []
        for l, r in queries:
            if l == 0:
                res.append(prefix[r])
            else:
                res.append((prefix[r] * inv_prefix[l - 1]) % MOD)
        return res
