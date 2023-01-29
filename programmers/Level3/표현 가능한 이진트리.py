def solution(numbers):
    def make_full_binary_number(number):
        reverseBinaryNumber = []
        while number != 1:
            reverseBinaryNumber.append(str(number % 2))
            number //= 2
        reverseBinaryNumber.append("1")
        binaryNumber = ''.join(reverseBinaryNumber[::-1])
        binaryTreeSize = 1
        while binaryTreeSize < len(binaryNumber):
            binaryTreeSize = (binaryTreeSize + 1) * 2 - 1
        binaryNumber = "0" * (binaryTreeSize - len(binaryNumber)) + binaryNumber
        return binaryNumber
    
        
    def is_valid(start, end, binary_number):
        if start == end:
            return binary_number[start]
        
        mid = (start + end) // 2
        root_node = binary_number[mid]
        left_subtree = is_valid(start, mid-1, binary_number)
        if not left_subtree or (root_node == '0' and left_subtree == '1'):
            return False
        
        right_subtree = is_valid(mid+1, end, binary_number)
        if not right_subtree or (root_node == '0' and right_subtree == '1'):
            return False
        
        if root_node == '0' and left_subtree == '0' and right_subtree == '0':
            return '0'
        return '1'
    
    answer = []
    for num in numbers:
        binary_number = make_full_binary_number(num)
        answer.append(int(is_valid(0, len(binary_number)-1, binary_number)))
    return answer
