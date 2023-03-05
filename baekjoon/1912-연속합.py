n = int(input())
arr = list(map(int, input().split()))

max_subseq_sum = subseq_sum = arr[0]
for i in range(1, len(arr)):
    subseq_sum = max(arr[i], subseq_sum + arr[i])
    max_subseq_sum = max(subseq_sum, max_subseq_sum)

print(max_subseq_sum)