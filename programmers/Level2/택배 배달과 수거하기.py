def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery_stack, pickup_stack = [], []
    for pos in range(n):
        if deliveries[pos] > 0:
            delivery_stack.append((pos, deliveries[pos]))
        if pickups[pos] > 0:
            pickup_stack.append((pos, pickups[pos]))
    
    while delivery_stack or pickup_stack:
        farthest_delivery_pos, farthest_pickup_pos = -1, -1
        if len(delivery_stack) > 0:
            farthest_delivery_pos = delivery_stack[-1][0]
        if len(pickup_stack) > 0:
            farthest_pickup_pos = pickup_stack[-1][0]
        
        answer += 2 * (max(farthest_delivery_pos, farthest_pickup_pos) + 1)
        
        can_delivery_cnt = cap
        while delivery_stack and can_delivery_cnt > 0:
            pos, box_cnt = delivery_stack.pop()
            if can_delivery_cnt - box_cnt >= 0:
                can_delivery_cnt -= box_cnt    
            else:
                box_cnt -= can_delivery_cnt
                can_delivery_cnt = 0
                delivery_stack.append((pos, box_cnt))
        
        can_pickup_cnt = cap
        while pickup_stack and can_pickup_cnt > 0:
            pos, box_cnt = pickup_stack.pop()
            if can_pickup_cnt - box_cnt >= 0:
                can_pickup_cnt -= box_cnt    
            else:
                box_cnt -= can_pickup_cnt
                can_pickup_cnt = 0
                pickup_stack.append((pos, box_cnt))
            
    return answer