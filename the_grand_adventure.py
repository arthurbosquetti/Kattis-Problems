n=int(input())
adventures=[]
for i in range(n):
    adv=str(input())
    adventures.append(adv)

b=True

for i in range(n):
    adventure=adventures[i]
    backpack=["-"]
    for j in range(len(adventure)):
        if adventure[j]=="$" or adventure[j]=="|" or adventure[j]=="*":
            backpack.insert(0,adventure[j])
            #print("new item. backpack = ",backpack)
        elif adventure[j]=="b":
            try:
                pos=backpack.index("$")
                b=True
            except:
                b=False
                #print("met banker. couldn't pay :/")
                break
            backpack=backpack[pos+1:]
            #print("met banker. new backpack: ",backpack)
        elif adventure[j]=="t":
            try:
                pos=backpack.index("|")
                b=True
            except:
                b=False
                #print("met trader. couldn't pay :/")
                break
            backpack=backpack[pos+1:]
            #print("met trader. new backpack: ",backpack)
        elif adventure[j]=="j":
            try:
                pos=backpack.index("*")
                b=True
            except:
                b=False
                #print("met jeweler. couldn't pay :/")
                break
            backpack=backpack[pos+1:]
            #print("met jeweler. new backpack: ",backpack)
            if not(b):
                break
    if b and len(backpack)==1:
        print("YES")
    else:
        print("NO")