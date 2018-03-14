
spreadsheet = []
with open("inputs/[Day2]input.txt", "r") as f:
    for line in f.readlines():
        spreadsheet.append([int(x) for x in line.split("\t")])


def check_row(row):

    for p in range(len(row)):
        v1 = row[p]
        for v2 in row[p+1:]:
            if v1 > v2:
                if v1 % v2 == 0:
                    return v1 / v2
            elif v2 % v1 == 0:
                return v2 / v1

    return 0

runningSum = 0
for row in spreadsheet:
    runningSum += check_row(row)

print(runningSum)
