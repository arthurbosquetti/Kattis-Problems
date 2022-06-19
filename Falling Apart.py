
n = int(input())
pieces = list(map(int, input().split()))
pieces.sort(reverse = True)

A = 0
B = 0
isAlice = True

for piece in pieces:
    if isAlice:
        A+=piece
        isAlice = False
    else:
        B+= piece
        isAlice = True

print(A, B)
