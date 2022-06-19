
n, m = map(int,input().split())
can_sizes = []

for line in range(n):
    can_sizes.append(int(input()))
can_sizes.sort()

#binarySearch to find the successor of x
def binarySearchSuccessor(A, i, j, x):
    if j<=i:
        return A[i]
    m = (i+j)//2
    if m==0:
        return A[m]
    if x<=A[m]:
        if A[m-1]<x:
            return A[m]
        return binarySearchSuccessor(A, i, m-1, x)
    return binarySearchSuccessor(A, m+1, j, x)

waste = 0

for line in range(m):
    color_needs = int(input())
    waste+=binarySearchSuccessor(can_sizes, 0, n, color_needs) - color_needs

print(waste)
