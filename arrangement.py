
N=int(input())  #number of rooms
M=int(input())  #number of teams

t=M//N          #min. teams per room
r=M%N           #extra teams (remainder)

string = "*" * t

#for number of rooms without an extra team...
for j in range(N-r): 
    print(string)

#for number of rooms with an extra team...
while r>0:
    print(string+"*") 
    r-=1
