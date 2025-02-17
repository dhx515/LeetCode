class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # 소수 판별을 위해 에라토스테네스의 체 사용
        def count_primes(n):
            if n < 2:
                return 0
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            
            return sum(is_prime)  # 소수의 개수 반환

        p_count = count_primes(n)  # 소수 개수
        np_count = n - p_count  # 비소수 개수

        # (p_count! * np_count!) % MOD 계산
        return (math.factorial(p_count) * math.factorial(np_count)) % MOD
