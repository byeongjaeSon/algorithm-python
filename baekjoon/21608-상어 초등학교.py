from collections import defaultdict

n = int(input())
student_to_favorite = defaultdict(set)
seat_map = [[0] * n for _ in range(n)]
delta = [(-1,0), (1,0), (0,-1), (0,1)]

def filter_by_first_condition(student_number):
    positions = []
    max_favorite_student_cnt = -1
    for i in range(n):
        for j in range(n):
            if seat_map[i][j] != 0:
                continue
            favorite_student_cnt = 0
            for d in delta:
                ny = i + d[0]
                nx = j + d[1]
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue
                if seat_map[ny][nx] in student_to_favorite[student_number]:
                    favorite_student_cnt += 1

            positions.append((favorite_student_cnt, (i,j)))
            max_favorite_student_cnt = max(max_favorite_student_cnt, favorite_student_cnt)

    positions_by_first_condition = filter(lambda x : x[0] == max_favorite_student_cnt, positions)
    return list(map(lambda x : x[1], positions_by_first_condition))

def filter_by_second_condition(positions_by_first_condition):    
    if len(positions_by_first_condition) <= 1:
        return positions_by_first_condition

    max_blank_cnt = 0
    positions = []
    for position in positions_by_first_condition:
        blank_cnt = 0
        for d in delta:
            ny = position[0] + d[0]
            nx = position[1] + d[1]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if seat_map[ny][nx] == 0:
                blank_cnt += 1

        positions.append((blank_cnt, position))
        max_blank_cnt = max(max_blank_cnt, blank_cnt)

    positions_by_second_condition = filter(lambda x : x[0] == max_blank_cnt, positions)
    return list(map(lambda x : x[1], positions_by_second_condition))

def filter_by_third_condition(positions_by_second_condition):
    return positions_by_second_condition[0]

def get_best_position(student_number):
    positions_by_first_condition = filter_by_first_condition(student_number)
    positions_by_second_condition = filter_by_second_condition(positions_by_first_condition)
    positions_by_third_condition = filter_by_third_condition(positions_by_second_condition)
    return positions_by_third_condition

def calculate_total_satisfaction():
    total_satisfaction = 0
    for i in range(n):
        for j in range(n):
            student_number = seat_map[i][j]
            nearby_favorite_student_cnt = 0
            for d in delta:
                ny = i + d[0]
                nx = j + d[1]
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue
                if seat_map[ny][nx] in student_to_favorite[student_number]:
                    nearby_favorite_student_cnt += 1

            if nearby_favorite_student_cnt != 0:
                total_satisfaction += 1 * pow(10, nearby_favorite_student_cnt-1)

    return total_satisfaction

def main():
    for _ in range(n*n):
        student_number, *favorites = list(map(int, input().split()))
        student_to_favorite[student_number].update(favorites)

    for student_number in student_to_favorite.keys():
        best_position = get_best_position(student_number)
        seat_map[best_position[0]][best_position[1]] = student_number

    total_satisfaction = calculate_total_satisfaction()
    print(total_satisfaction)

if __name__ == '__main__':
    main()
