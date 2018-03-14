
spreadsheet = []
with open("inputs/[Day2]input.txt", "r") as f:
    for line in f.readlines():
        spreadsheet.append([int(x) for x in line.split("\t")])


def check_row(row):
    _min = -1
    _max = -1

    for elem in row:
        if elem < _min or _min == -1:
            _min = elem
        elif elem > _max or _max == -1:
            _max = elem

    return _max - _min

runningSum = 0
for row in spreadsheet:
    runningSum += check_row(row)

print(runningSum)
