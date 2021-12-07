num1 = int(input())

num = num1
count = 0

while True:
    a = num//10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c

    count = count +1
    if num == num1:
        break
        
    
print(count)