n = int(input())
person = [i for i in range(1, n+1)]

t = 1
idx = 0
while len(person) >= 2:
  idx += pow(t, 3) -1
  idx %= len(person)
  person.pop(idx)
  t += 1

print(person[0])