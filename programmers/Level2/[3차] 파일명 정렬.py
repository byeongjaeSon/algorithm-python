# 프로그래머스 - [3차] 파일명 정렬(17686)
# https://school.programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    tmp = []
    
    for file in files:
        converted_file = file.lower()
        for l in range(len(converted_file)):
            if converted_file[l].isdigit():
                r = l+1 
                while r < len(file):
                    if converted_file[r].isdigit():
                        r += 1
                        continue
                    else:
                        break
                head = converted_file[:l]
                number = int(converted_file[l:r])
                tmp.append((head, number, file))
                break
    
    tmp.sort(key = lambda x : (x[0], x[1]))
    answer = [t[2] for t in tmp]
        
    return answer
