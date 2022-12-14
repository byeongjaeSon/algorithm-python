import string

number = string.digits + string.ascii_uppercase

# https://joyjangs.tistory.com/35
def convert_recur(num, base):
    q, r = divmod(num, base)
    return convert_recur(q, base) + number[r] if q else number[r]
    
def solution(n, t, m, p):
    seq = ""
    num = 0
    while len(seq) <= t * m:
        seq += convert_recur(num, n)
        num += 1
    
    return ''.join(seq[p-1 : (m * t + p)-1 : m])
