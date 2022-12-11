def solution(a):
    answer = 0
    left_min_val = right_min_val = 10**10
    left_min = [0] * len(a)
    right_min = [0] * len(a)

    for i in range(len(a)):
        if left_min_val > a[i]:
            left_min_val = a[i]
        left_min[i] = left_min_val
    
    for i in range(len(a)-1, -1, -1):
        if right_min_val > a[i]:
            right_min_val = a[i]
        right_min[i] = right_min_val

    for i in range(len(a)):
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            answer += 1
        
    return answer
