N, A = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(N):
    if nums[i] < A:
        print(nums[i], end=" ")