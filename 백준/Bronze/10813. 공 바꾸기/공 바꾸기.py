N, M=map(int, input().split())
box = list(range(1, N+1))

for swap in range(M):
    i,j = map(int, input().split())
    box[i-1], box[j-1] = box[j-1], box[i-1]

for num in box:
    print(num, end=" ")