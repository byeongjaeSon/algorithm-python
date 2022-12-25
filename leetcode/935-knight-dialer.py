class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        curr = [0 if i == 5 else 1 for i in range(10)]
        mod = (10 ** 9 + 7)

        for i in range(1, n):
            next = [0 for _ in range(10)]
            next[0] = curr[4] + curr[6] % mod
            next[1] = curr[6] + curr[8] % mod
            next[2] = curr[7] + curr[9] % mod
            next[3] = curr[4] + curr[8] % mod
            next[4] = curr[3] + curr[9] + curr[0] % mod
            next[6] = curr[1] + curr[7] + curr[0] % mod
            next[7] = curr[2] + curr[6] % mod
            next[8] = curr[1] + curr[3] % mod
            next[9] = curr[2] + curr[4] % mod
            curr = next

        return sum(curr) % mod
