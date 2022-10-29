from collections import defaultdict
import itertools

def isMatched(bid, uid):
    if len(bid) != len(uid): return False
    for i in range(len(bid)):
        if bid[i] == '*': continue
        if bid[i] != uid[i]: return False
    return True
    
def solution(user_id, banned_id):
    answer_set = set()
    uid_lists = []
    
    for bid in banned_id:
        uid_list = [uid for uid in user_id if isMatched(bid, uid)]
        uid_lists.append(uid_list)    
   
    product_result = itertools.product(*uid_lists)
    for result in product_result:
        result_set = frozenset(result)
        if len(result_set) != len(banned_id): continue
        answer_set.add(result_set)

    return len(answer_set)
