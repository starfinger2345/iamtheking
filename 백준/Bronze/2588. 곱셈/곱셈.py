num1 = int(input())
num2 = int(input())

#num1_100 = num1//100*100
#num1_10 = (num1-num1_100)//10*10
#num1_1 = (num1-num1_100-num1_10)

num2_100 = num2//100*100
num2_10 = (num2-num2_100)//10*10
num2_1 = (num2-num2_100-num2_10)

print(num1*num2_1)
print(int(num1*num2_10/10))
print(int(num1*num2_100/100))
print(num1*num2)