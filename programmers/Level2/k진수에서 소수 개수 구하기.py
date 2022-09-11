def is_prime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def conv(n, k):
    tmp = ''
    while n:
        tmp = str(n%k) + tmp
        n //= k
    return tmp

def solution(n, k):
    answer = 0
    s = conv(n, k)
    nums = s.split('0')
    for num in nums:
        if num and is_prime(int(num)):
            answer += 1
    return answer
