
n, k = map(int, input().split())

commands = input().split()

child = 0
positions = [0]
skip = False

for i in range(len(commands)):
    if skip:
        skip = False
        continue
    if commands[i] == "undo":
        for _ in range(int(commands[i+1])):
            positions.pop()
            child = positions[-1]
        skip = True
    else:
        command = int(commands[i])
        child = (child+command)%n
        positions.append(child)

print(child)