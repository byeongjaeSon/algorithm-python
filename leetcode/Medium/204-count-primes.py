class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for number in range(2, int(n**0.5)+1):
            if is_prime[number]:
                for multiple in range(number+number, n, number):
                    is_prime[multiple] = False
        return is_prime.count(True)
