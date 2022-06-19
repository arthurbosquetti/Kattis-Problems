
n=int(input())
words=list(map(str,input().split()))
b=True
for i in range(1,len(words)+1):
    if not(words[i-1]=="mumble") and not(str(i)==words[i-1]):
        b=False
if b:
    print("makes sense")
else:
    print("something is fishy")
