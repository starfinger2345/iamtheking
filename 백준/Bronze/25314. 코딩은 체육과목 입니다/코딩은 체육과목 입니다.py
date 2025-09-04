N = int(input())
ans = "int"

for i in range(N//4):
    ans = "long " + ans
print(ans)