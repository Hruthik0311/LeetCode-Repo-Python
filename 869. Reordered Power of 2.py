class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def sort_digits(x):
            return ''.join(sorted(str(x)))
        power_set = {sort_digits(1 << i) for i in range(31)}
        return sort_digits(n) in power_set
