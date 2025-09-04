year = int(input())

result = 0
if year % 400 == 0:
    result = 1
    print(result)
elif year % 4 == 0 and year % 100 != 0:
    result = 1
    print(result)
else:
    result = 0
    print(result)