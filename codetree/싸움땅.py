class Player:
    def __init__(self, y, x, d, s):
        self.initial_state = s
        self.y = y
        self.x = x
        self.d = d
        self.point = 0
        self.gun_state = 0


delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
n, m, k = map(int, input().split())
board = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n)]
players = []


def init():
    for y in range(n):
        line = list(map(int, input().split()))
        for x in range(n):
            if line[x] != 0:
                board[y][x][0] = [line[x]]
            else:
                board[y][x][0] = []
            board[y][x][1] = -1
    players.clear()
    for player_num in range(m):
        y, x, d, s = list(map(int, input().split()))
        players.append(Player(y - 1, x - 1, d, s))
        board[y - 1][x - 1][1] = player_num


def out_of_bound(y, x):
    return y < 0 or y >= n or x < 0 or x >= n


def get_strongest_gun(y, x, player_num):
    if len(board[y][x][0]) > 0:
        strongest_gun_stat = max(board[y][x][0])
        # 플레이어가 이미 총을 가지고 있는 경우에는
        if players[player_num].gun_state != 0:
            # 놓여있는 총들과 플레이어가 가지고 있는 총 가운데 공격력이 더 쎈 총을 획득하고, 나머지 총들은 해당 격자에 둡니다.
            if strongest_gun_stat > players[player_num].gun_state:
                board[y][x][0].remove(strongest_gun_stat)
                board[y][x][0].append(players[player_num].gun_state)
                players[player_num].gun_state = strongest_gun_stat
        else:
            board[y][x][0].remove(strongest_gun_stat)
            players[player_num].gun_state = strongest_gun_stat


def simulate():
    for player_num in range(m):
        # 1-1.
        cy, cx = players[player_num].y, players[player_num].x
        dy, dx = delta[players[player_num].d]
        ny, nx = cy + dy, cx + dx

        # 첫 번째 플레이어부터 순차적으로 본인이 향하고 있는 방향대로 한 칸만큼 이동합니다.
        # 만약 해당 방향으로 나갈 때 격자를 벗어나는 경우에는
        if out_of_bound(ny, nx):
            # 정반대 방향으로 방향을 바꾸어서
            if players[player_num].d < 2:
                players[player_num].d += 2
            else:
                players[player_num].d -= 2

            dy, dx = delta[players[player_num].d]
            ny, nx = cy + dy, cx + dx
        #  1만큼 이동합니다.
        # player 업데이트
        players[player_num].y = ny
        players[player_num].x = nx
        y, x = players[player_num].y, players[player_num].x

        # player 이동했으므로 이전 위치 board도 업데이트
        board[cy][cx][1] = -1

        another_player_num = board[ny][nx][1]
        # 2-1. 만약 이동한 방향에 플레이어가 없다면 해당 칸에 총이 있는지 확인합니다
        # 총이 있는 경우, 해당 플레이어는 총을 획득합니다.
        if another_player_num == -1:
            get_strongest_gun(y, x, player_num)
            # 다음 위치 board도 업데이트
            board[ny][nx][1] = player_num
            continue

        # 2-2-1. 만약 이동한 방향에 플레이어가 있는 경우에는 두 플레이어가 싸우게 됩니다
        my_stat = players[player_num].initial_state + players[player_num].gun_state
        your_stat = players[another_player_num].initial_state + players[another_player_num].gun_state

        # 해당 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합을 비교하여 더 큰 플레이어가 이기게 됩니다.
        winner, loser = -1, -1
        if my_stat < your_stat:
            winner, loser = another_player_num, player_num
        elif my_stat > your_stat:
            winner, loser = player_num, another_player_num
        # 만일 이 수치가 같은 경우에는 플레이어의 초기 능력치가 높은 플레이어가 승리하게 됩니다.
        else:
            if players[player_num].initial_state < players[another_player_num].initial_state:
                winner, loser = another_player_num, player_num
            else:
                winner, loser = player_num, another_player_num

        # 이긴 플레이어는 각 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합의 차이만큼을 포인트로 획득하게 됩니다.
        players[winner].point += abs(my_stat - your_stat)

        # 2-2-2.
        # 진 플레이어는 본인이 가지고 있는 총을 해당 격자에 내려놓고,
        if players[loser].gun_state != 0:
            board[y][x][0].append(players[loser].gun_state)
        players[loser].gun_state = 0
        #  해당 플레이어가 원래 가지고 있던 방향대로 한 칸 이동합니다.
        # 만약 이동하려는 칸에 다른 플레이어가 있거나 격자 범위 밖인 경우에는 오른쪽으로 90도씩 회전하여
        for i in range(4):
            d = (players[loser].d + i) % 4
            dy, dx = delta[d]
            ny, nx = y + dy, x + dx

            if out_of_bound(ny, nx) or board[ny][nx][1] != -1:
                continue

            # 빈 칸이 보이는 순간 이동합니다.
            board[players[loser].y][players[loser].x][1] = -1

            players[loser].y = ny
            players[loser].x = nx
            players[loser].d = d

            board[ny][nx][1] = loser

            # 만약 해당 칸에 총이 있다면, 해당 플레이어는 가장 공격력이 높은 총을 획득하고 나머지 총들은 해당 격자에 내려 놓습니다.
            get_strongest_gun(ny, nx, loser)
            break

        # 2-2-3.
        # 이긴 플레이어는 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려 놓습니다.
        get_strongest_gun(y, x, winner)

        # 다음 위치 board도 업데이트
        board[players[winner].y][players[winner].x][1] = winner


if __name__ == '__main__':
    init()
    for _ in range(k):
        simulate()

    for player in players:
        print(player.point, end=" ")
