
n=int(input())
for i in range(n):
    lst=list(map(int,input().split()))
    print(sum(lst)-lst[0]-len(lst)+2) #+2 to not acknowledge 1st and last items of lst
