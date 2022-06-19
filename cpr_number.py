
cpr=input()
lst=[]
for i in range(11):
    if i==6:
        continue
    else:
        lst.append(int(cpr[i]))
dot=0
coeff=[4,3,2,7,6,5,4,3,2,1]
for i in range(10):
    dot+=lst[i]*coeff[i]
if dot%11==0:
    print(1) 
else:
    print(0)