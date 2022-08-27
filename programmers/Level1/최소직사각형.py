# 프로그래머스 - 최소직사각형(86491)
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

# w, h중 큰 값을 모아서 그 중 큰 값과, w, h중 작은 값을 모아서 그 중 큰 값을 곱하기
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

