# 프로그래머스 - 키패드 누르기(67256)
# https://school.programmers.co.kr/learn/courses/30/lessons/67256

from collections import defaultdict

def solution(numbers, hand):
    answer = []
    left_y, left_x, right_y, right_x = 3, 0, 3, 2
    
    digit_to_pos = defaultdict(list)
    for digit in range(0, 12):
        key = str(digit + 1) if digit < 10 else "0" if digit == 10 else "_"  
        digit_to_pos[key].append(digit//3)
        digit_to_pos[key].append(digit%3)
    
    for number in numbers:
        number_y, number_x = digit_to_pos[str(number)][0], digit_to_pos[str(number)][1]
        if number % 3 == 1:
            left_y, left_x = number_y, number_x
            answer.append("L")
            continue
            
        if number % 3 == 0 and number != 0:
            right_y, right_x = number_y, number_x
            answer.append("R")
            continue
            
        left_dist = abs(left_y - number_y) + abs(left_x - number_x)
        right_dist = abs(right_y - number_y) + abs(right_x - number_x)
        if (left_dist < right_dist or (left_dist == right_dist and hand == "left")):
            left_y, left_x = number_y, number_x
            answer.append("L")
        elif (left_dist > right_dist or (left_dist == right_dist and hand == "right")):
            right_y, right_x = number_y, number_x
            answer.append("R")

    return "".join(answer)
