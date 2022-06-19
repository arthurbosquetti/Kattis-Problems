
n=int(input())
bricks=list(map(int,input().split()))
c=1
for i in range(n-1):
    width=bricks[i]
    if width<bricks[i+1]:
        c+=1
print(c)