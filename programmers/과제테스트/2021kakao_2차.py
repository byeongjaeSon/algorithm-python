import requests
import random
import json

'''
문제 풀이 전략

우선적으로 API들을 먼저 구현하고 테스트 했습니다.
API를 구현하면서 어떻게 자전거들을 옮길지 고민을 했습니다.

2번 문제에서는 추가적인 조건을 주고 최적화할 부분을 제시해줬지만, 이에 대해서 생각하지 않고
1번 문제만 잘 풀자고 생각했습니다.

1번 문제는 맵이 좁고 트럭들 5대로 20개씩 자전거를 옮기므로 충분히 맵 전체를 커버할 수 있을거라 생각했습니다.

자전거를 유지시키는 방법은
매우 단순하게 그냥 트럭들을 랜덤으로 이동시키면서 해당 장소에 자전거가 많이 남으면 여분의 자전거들을 트럭에 올리고, 
해당 장소에 자전거가 부족해 보이면 트럭이 가진 자전거를 내리는 방식으로 문제를 풀었습니다.
해당 장소에 자전거가 많은가, 많지 않은가는 기준값인 mean값을 정했으며,
mean값은 단순하게 프로그램을 직접 실행해서 바꿔가며 결과 score값을 비교했습니다.

단, 마지막에 자전거가 0개인 위치, 자전거가 제일 많이 남는 위치, 자전거가 제일 적게 남는 위치 3개가 가장 우선적으로 방문해야 하는 
지점이라고 생각해서 해당 지점에 먼저 방문하도록 코드를 작성했습니다.
(크게 효과가 있지는 않았던걸로 기억합니다.)

대략 코드는 score 부분에서 70등 정도 했고,
1번에 대한 점수가 생각보다 상위권이었고,
2번에 대한 최적화는 안되어 있기 때문에 굉장히 낮은 점수였습니다.
(1번 점수 + 2번 점수로 계산했을 때 70등 정도)
'''

# in: 자전거 상차, out: 자전거 하차
scom = ['not', 'up', 'right', 'down', 'left', 'in', 'out']
dr = [0, -1, 0, 1, 0, 0, 0]
dc = [0, 0, 1, 0, -1, 0, 0]
tcommand = {scom[i] : i for i in range(7)}

class truck:
# p: 트럭의 위치
# load: 가지고있는 자전거의 양
    def __init__(self):
        self.p = 0
        self.load = 0

# 디버깅용
    def __str__(self):
        return str(self.p) + ' ' + str(self.load)

    def __repr__(self):
        return '(' + str(self.p) + ' ' + str(self.load) + ')'

#=============================API 들 구현=============================

# 자전거들의 개수를 bycycle에 담아놓음
def getlocation(url, headers, bycycle):
    path = 'locations'
    req = requests.get('/'.join([url, path]), headers=headers)

    j = req.json()

    for id, cnt in [(i['id'], i['located_bikes_count']) for i in j['locations']]:
        bycycle[id] = cnt

    return bycycle

# Truck API
def gettrucks(url, headers, trucks):
    path = 'trucks'
    req = requests.get('/'.join([url, path]), headers=headers)

    j = req.json()
    for id, p, cnt in [(i['id'], i['location_id'], i['loaded_bikes_count']) for i in j['trucks']]:
        trucks[id].p = p
        trucks[id].load = cnt

    return trucks

# Simulate API
def simulate(url, headers, data):
    path = 'simulate'
    req = requests.put('/'.join([url, path]), headers=headers, data=data)

    return req.json()

#=============================API 들 구현=============================

# A에서 B까지 이동하려면 어떻게 이동해야하는지 기록합니다. -> map의 ID기준.
# ex) 문제 1 기준
# ID 0 = (4,0)
# ID 6 = (3,1)
# ID 0 -> ID 6 = [up, right] = [1, 2]
# 따라서 dcom = [1, 2]
def getdist(loc, f, t):
    dcom = [tcommand['up'] for i in range(abs(loc[f][0] - loc[t][0])) if loc[f][0] > loc[t][0]]
    dcom.extend([tcommand['down'] for i in range(abs(loc[f][0] - loc[t][0])) if loc[f][0] < loc[t][0]])
    dcom.extend([tcommand['right'] for i in range(abs(loc[f][1] - loc[t][1])) if loc[f][1] < loc[t][1]])
    dcom.extend([tcommand['left'] for i in range(abs(loc[f][1] - loc[t][1])) if loc[f][1] > loc[t][1]])
    return (abs(loc[f][0] - loc[t][0]) + abs(loc[f][1] - loc[t][1]), dcom)

# t: truck, bnum, bycycles, map: ID X의 (x,y) 좌표 저장, mmap: 지도에서 (x,y)에 있는 ID 저장,

# 트럭을 맵의 랜덤 방향으로 이동시키면서, 자전거의 개수가 평균보다 크면 트럭에 자전거를 담고,
# 자전거의 개수가 평균보다 작으면 자전거를 내련준다.
def truckmove(t, bnum, map, mmap, mean, comm, dest, all = 'not'):
    x, y = map[t.p][0], map[t.p][1]
    retcomm = []

    if all == 'out' or all == 'in':
        mean = 1

    for i in comm:
        if len(retcomm) >= 10: break
        id = mmap[x][y]

        if id == dest and all == 'out':
            need = t.load
            retcomm.extend([tcommand['out'] for i in range(need) if need > 0])
            bnum[id] += need
        elif id == dest and all == 'in':
            need = min(bnum[id] - mean, 20 - t.load)
            retcomm.extend([tcommand['in'] for i in range(need) if need > 0])
            bnum[id] -= need
        elif all == 'out':
            need = min(bnum[id] - mean, 20 - t.load)
            retcomm.extend([tcommand['in'] for i in range(need) if need > 0])
            bnum[id] -= need
        elif all == 'in':
            need = min(mean - bnum[id], t.load)
            retcomm.extend([tcommand['out'] for i in range(need) if need > 0])
            bnum[id] += need
        else:
            # ID X에 있는 자전거의 개수가 평균보다 작으면 트럭이 가진 자전거를 내려줌
            if bnum[id] < mean:
                need = min(mean - bnum[id], t.load)
                retcomm.extend([tcommand['out'] for i in range(need) if need > 0])
                bnum[id] += need

            # ID X에 있는 자전거의 개수가 평균보다 많으면 트럭이 자전거를 가져감
            elif bnum[id] > mean:
                need = min(bnum[id] - mean, 20 - t.load)
                retcomm.extend([tcommand['in'] for i in range(need) if need > 0])
                bnum[id] -= need

        retcomm.append(i)
        x += dr[i]
        y += dc[i]

    return retcomm

def kakaotaxi(qid=1):
    #restapi를 위한 정보들
    url = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
    path = 'start'
    token = "5277b9760cd7e27d584d3c1d84b5eaf9"
    param = {'problem':qid}
    headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}

    msize = 0
    mean = 15
    # 문제 1번과 2번에 따라서 값을 정해놓음
    # msize: map 크기
    # mean: 모든 좌표의 자전거들을 평균값으로 두려고 함. ID X에 mean보다 자전거가 많을 수록 우선 방문..
    if qid == 1:
        msize = 5
        mean = 2
    else:
        msize = 60
        mean = 3

    mymap = [[msize-i-1 + msize*j for j in range(msize)] for i in range(msize)]

    pos = { mymap[i][j]: (i, j) for i in range(msize) for j in range(msize)}

    # 자전거들의 정보를 담기 위한 2차원 리스트
    bycycles = [0 for i in range(msize*msize)]
    # 문제에 따라 트럭 수를 저장해놓음 1번 문제: 트럭 5개, 2번 문제 트럭 10개
    tnum = [0, 5, 10]
    # 트럭 객체를 만들어 놓음
    trucks = [truck() for i in range(tnum[qid])]
    req = requests.post('/'.join([url,path]), headers=headers, data=json.dumps(param))
    j = req.json()
    auth_key = j['auth_key']
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}

    # simulate에 넣을 트럭의 명령들
    next_command = [[] for i in range(len(trucks))]
    bnum = [0, 4, 3]
    # 자전거들의 초기 값
    prev_bycycle = [bnum[qid] for i in range(msize*msize)]

    for i in range(720):
        # 트럭의 목적지를 "랜덤"으로 만듦
        trucksdes = [int(random.uniform(0, msize*msize)) for i in range(len(trucks))]
        bycycles = getlocation(url, headers, bycycle=bycycles)
        mmin = 100000000
        mini = 0
        mmax = -100000000
        maxi = 0

        # 자전거수가 가장 많은 위치와 가장 적은 위치를 구함
        # 자전거수가 많은 곳은 반납이 많은 곳이고, 자전거 수가 적은 곳은 소비가 많은 곳이라고 생각
        # (즉, 두 곳 모두 트럭이 우선적으로 이동해야하는 장소)

        for i, j in enumerate([prev_bycycle[i] - bycycles[i] for i in range(len(bycycles))]):
            if mmin > j:
                mmin, mini = j, i
            if mmax < j:
                mmax, maxi = j, i

        trucks = gettrucks(url, headers, trucks)
        # 자전거 개수가 0개 이므로, 트럭들을 가장 우선적으로 빠르게 이동해야 하는 곳 (매우 긴급)
        emergen = [i[0] for i in enumerate(bycycles) if i[1] == 0]

        i = 0
        # 트럭 하나에 20개씩 옮길 수 있기 때문에 개수 나누기
        while i < min(int(mmin/20), tnum[qid]):
            trucksdes[i] = mini
            i += 1
        while i < min(int(mmax/20), tnum[qid]):
            trucksdes[i] = maxi
            i += 1

        for i in range(tnum[qid]):
            t = trucks[i]
            # 만약 매우 긴급하게 자전거를 하차해야하는 곳이 있다면, 해당 위치로 트럭을 우선 이동한다.
            if len(emergen) > 0:
                trucksdes[i] = emergen.pop()
            idx, next_command[i] = getdist(pos, t.p, trucksdes[i])

        nextcommand = []

        for i in range(tnum[qid]):
            t = trucks[i]
            print(i, t)
            ncom = truckmove(t, bycycles, pos, mymap, mean, next_command[i], -1, 'not')

            nextcommand.append({'truck_id':i, 'command': ncom})

        # Simulate API
        j = simulate(url, headers=headers, data=json.dumps({'commands':nextcommand}))
        print(j['time'])
        prev_bycycle = [i for i in bycycles]

    req = requests.get(url + '/score', headers=headers)
    print(req.json()['score']) # 268.1871638655462
kakaotaxi(1)