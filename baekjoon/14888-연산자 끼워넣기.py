import sys
from itertools import permutations

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
op_nums = list(map(int, sys.stdin.readline().split()))
operator = "+-*/"
operator_seq = []
for i in range(len(op_nums)):
  operator_seq.extend(operator[i] * op_nums[i])

op_permutes = list(permutations(operator_seq, N-1))

max_ans = -10**10
min_ans = 10**10

for op_seq in op_permutes:
  result = numbers[0]
  for i in range(N-1):
    if op_seq[i] == '+':
      result += numbers[i+1]
    elif op_seq[i] == '-':
      result -= numbers[i+1]
    elif op_seq[i] == '*':
      result *= numbers[i+1]
    else:
      if result < 0 and numbers[i+1] > 0:
        result = -((-result) // numbers[i+1])
      else:
        result //= numbers[i+1]

  if result < min_ans:
    min_ans = result
  if result > max_ans:
    max_ans = result

print(max_ans)
print(min_ans)
