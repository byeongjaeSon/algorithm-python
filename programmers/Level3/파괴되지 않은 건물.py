# Navie 풀이, O(N * M * K(skill의 행의 길이)) -> 당연하게도 효율성 테스트 통과 실패.
# def solution(board, skill):
#     answer = 0
#     for s in skill:
#         type, r1, c1, r2, c2, degree = s[0], s[1], s[2], s[3], s[4], s[5]
#         for r in range(r1, r2+1):
#             for c in range(c1, c2+1):
#                 if type == 1:
#                     board[r][c] -= degree
#                 else:
#                     board[r][c] += degree
#     for b in board:
#         for e in b:
#             if e > 0:
#                 answer += 1
#     return answer


# K는 고정된 값이므로 변경할 수 없고 O(N*M)의 시간복잡도를 log 혹은 상수시간으로 줄여야한다.
# -> 누적합 이용????

def solution(board, skill):
    answer = 0
    prefix_sum = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for s in skill:
        type, r1, c1, r2, c2, degree = s[0], s[1], s[2], s[3], s[4], s[5]
        if type == 1:            
            prefix_sum[r1][c1] -= degree
            prefix_sum[r2+1][c1] += degree
            prefix_sum[r1][c2+1] += degree
            prefix_sum[r2+1][c2+1] -= degree
        else:
            prefix_sum[r1][c1] += degree
            prefix_sum[r2+1][c1] -= degree
            prefix_sum[r1][c2+1] -= degree
            prefix_sum[r2+1][c2+1] += degree
    
    for x in range(len(prefix_sum[0])):
        for y in range(1, len(prefix_sum)):
            prefix_sum[y][x] += prefix_sum[y-1][x]
    
    for y in range(len(prefix_sum)):
        for x in range(1, len(prefix_sum[0])): 
            prefix_sum[y][x] += prefix_sum[y][x-1]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] + prefix_sum[i][j]) > 0 :
                answer += 1
    
    return answer
