n=int(input())
numbers=[]
for i in range(n):
    number=int(input())
    numbers.append(number)
init=numbers[0]
b=False
for i in range(1,n-1):
    if b:
        init=numbers[i]
        b=False
    elif numbers[i]%init==0:
        print(numbers[i])
        b=True