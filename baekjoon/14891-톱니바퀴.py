import sys

CLOCKWISE, COUNTERCLOCKWISE = 1, -1
gear_status = []

for _ in range(4):
    statuses = sys.stdin.readline().strip()
    gear_status.append([int(status) for status in statuses])

k = int(sys.stdin.readline().strip())
actions = []
for _ in range(k):
    gear_num, rotation_direction = map(int, sys.stdin.readline().strip().split(' '))
    actions.append((gear_num-1, rotation_direction))

def rotate_gear(gear_num, rotation_direction):
    if rotation_direction == CLOCKWISE:
        gear_status[gear_num] = [gear_status[gear_num][-1]] + gear_status[gear_num][:-1]
    else:
        gear_status[gear_num] = gear_status[gear_num][1:] + [gear_status[gear_num][0]]

for gear_num, rotation_direction in actions:
    delayed_rotate_actions = [(gear_num, rotation_direction)]

    before_rotation_direction = -rotation_direction
    curr_gear_num = gear_num
    while (curr_gear_num != 0):
        curr_gear_left_status = gear_status[curr_gear_num][6]
        left_gear_right_status = gear_status[curr_gear_num - 1][2]
        if left_gear_right_status != curr_gear_left_status:
            delayed_rotate_actions.append((curr_gear_num - 1, before_rotation_direction))
            curr_gear_num -= 1
            before_rotation_direction *= -1
        else:
            break
    
    before_rotation_direction = -rotation_direction
    curr_gear_num = gear_num
    while (curr_gear_num != 3):
        curr_gear_right_status = gear_status[curr_gear_num][2]
        right_gear_left_status = gear_status[curr_gear_num + 1][6]
        if curr_gear_right_status != right_gear_left_status:
            delayed_rotate_actions.append((curr_gear_num + 1, before_rotation_direction))
            curr_gear_num += 1
            before_rotation_direction *= -1
        else:
            break
    
    for gear_num, rotation_direction in delayed_rotate_actions:
        rotate_gear(gear_num, rotation_direction)
    
print(sum([(1<<gear_num) for gear_num in range(4) if gear_status[gear_num][0] == 1]))
