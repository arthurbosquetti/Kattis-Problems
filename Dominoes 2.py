
class Domino:
    def __init__(self):
        self.adjacent = []
        self.knocked_down = False

def countDominoes(domino, counter):
    if not domino.knocked_down:
        domino.knocked_down = True
        counter+=1
        for d in domino.adjacent:
            counter = countDominoes(d, counter)
        return counter
    return counter

test_cases = int(input())

for _ in range(test_cases):
    n, m, l = map(int, input().split())

    dominoes = []
    for _ in range(n):
        dominoes.append(Domino())
    
    for _ in range(m):
        domino1, domino2 = map(int, input().split())
        dominoes[domino1-1].adjacent.append(dominoes[domino2-1])

    fallen = 0
    for _ in range(l):
        z = int(input())
        fallen = countDominoes(dominoes[z-1], fallen)
    
    print(fallen)
