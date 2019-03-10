import heapq
nums = [4,1,3,2,16,9,10,14,8,7]
k = 2
heapq.heapify(nums)
res = float('inf')
for _ in range(k):
    res = heapq.heappop(nums)
print(res)
