
row=[".........","........."]
for i in range(5):
    row+=[".."+input()+".."]
row+=[".........",".........",]
c=0
valid=True
for i in range(2,7):
    if valid:
        for j in range(2,7):
            if row[i][j]=="k":
                c+=1
                if (row[i-1][j+2]=="k" or row[i-1][j-2]=="k" or 
                   row[i+1][j+2]=="k" or row[i+1][j-2]=="k" or  
                   row[i-2][j+1]=="k" or row[i-2][j+1]=="k" or 
                   row[i+2][j+1]=="k" or row[i+2][j-1]=="k"):
                    valid=False
                    break
print("valid" if (valid and c==9) else "invalid")

