num = int(input())
count = 0

if (num%5==0):
    count = num /5
else:
    while num >0:
        num = num -3
        count = count +1
        if(num % 5 == 0 and num != 0):
            count = count + num/5
            num = num%5
if num < 0:
    count = -1
print(int(count))


