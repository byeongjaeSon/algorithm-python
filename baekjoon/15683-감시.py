import sys
from collections import defaultdict
from itertools import product
import copy

cctvNum_to_direction = {
    1 : [('U'), ('R'), ('D'), ('L')],
    2 : [('U', 'D'), ('L', 'R')],
    3 : [('U', 'R'), ('R', 'D'), ('D', 'L'), ('L', 'U')],
    4 : [('L', 'U', 'R'), ('U', 'R', 'D'), ('R', 'D', 'L'), ('D', 'L', 'U')],
    5 : [('L', 'U', 'R', 'D')],
}
n, m = map(int, input().split())
office = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cctvNum_and_pos = [ (office[i][j], (i,j)) for i in range(n) for j in range(m) if office[i][j] != 0 and office[i][j] != 6]
directions = [cctvNum_to_direction[cctvNum] for cctvNum, _ in cctvNum_and_pos]
direction_combi = list(product(*directions))
extended_cctv_and_pos = [tuple(cctvNum_and_pos) for _ in range(len(direction_combi))]

min_blind_spot_cnt = 10 ** 10
for cctv_and_poses, directions in zip(extended_cctv_and_pos, direction_combi):
    temp_office = copy.deepcopy(office)
    for (cctvNum, (cy, cx)), cctvDirections in zip(cctv_and_poses, directions):
        for direction in cctvDirections:
            if direction == 'U':
                ny = cy-1
                while ny >= 0 and temp_office[ny][cx] != 6:
                    if temp_office[ny][cx] == 0:
                        temp_office[ny][cx] = '#'
                    ny -= 1
            elif direction == 'R':
                nx = cx+1
                while nx < m and temp_office[cy][nx] != 6:
                    if temp_office[cy][nx] == 0:
                        temp_office[cy][nx] = '#'
                    nx += 1
            elif direction == 'D':
                ny = cy+1
                while ny < n and temp_office[ny][cx] != 6:
                    if temp_office[ny][cx] == 0:
                        temp_office[ny][cx] = '#'
                    ny += 1
            elif direction == 'L':
                nx = cx-1
                while nx >= 0 and temp_office[cy][nx] != 6:
                    if temp_office[cy][nx] == 0:
                        temp_office[cy][nx] = '#'
                    nx -= 1

    blind_spot_cnt = 0        
    for row in temp_office:
        blind_spot_cnt += row.count(0)
    min_blind_spot_cnt = min(min_blind_spot_cnt, blind_spot_cnt)
print(min_blind_spot_cnt)
