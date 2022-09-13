def solution(new_id):
    new_id = new_id.lower()
    
    new_id = ''.join([ch for ch in new_id if ch.isalpha() or ch.isdigit() or ch in ['-', '_', '.']])
    
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    
    new_id = new_id.lstrip('.').rstrip('.')
    
    if not new_id : new_id = 'a'
    
    if len(new_id) >= 16: 
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    elif len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    
    return new_id
