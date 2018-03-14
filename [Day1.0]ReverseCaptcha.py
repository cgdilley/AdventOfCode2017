
with open("inputs/[Day1]input.txt", "r") as f:
    code = f.read().strip()

runningSum = 0

for i in range(len(code)):
    char = code[i]

    nextChar = code[(i+1) % len(code)]

    if char == nextChar:
        runningSum += int(char)

print("TOTAL: " + str(runningSum))
