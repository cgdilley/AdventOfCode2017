
with open("inputs/[Day1]input.txt", "r") as f:
    code = f.read().strip()

runningSum = 0

l = len(code)
step = int(l / 2)

for i in range(l):
    char = code[i]

    nextChar = code[(i + step) % l]

    if char == nextChar:
        runningSum += int(char)

print("TOTAL: " + str(runningSum))
