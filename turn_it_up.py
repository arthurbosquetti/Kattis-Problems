
n=int(input())
volume=7
for i in range(n):
    change=input()
    if change=="Skru op!" and volume<10:
        volume+=1
    elif change=="Skru ned!" and volume>0:
        volume-=1
print(volume)
