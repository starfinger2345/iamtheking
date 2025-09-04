a, b, c = map(int, input().split(" "))

if a == b == c:
    win = 10000 + 1000 * a
elif a == b or c == a:
    win = 1000 + 100 * a
elif b == c:
    win = 1000 + 100 * b
else:
    win = 100 * max(a, b, c)

print(win)