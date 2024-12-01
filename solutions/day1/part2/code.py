from collections import Counter

file_path = "input.txt"
sep = " " * 3

leftList = []
rightList = []
with open(file_path) as file:
    for row in file:
        leftId, rightId = row.strip().split(sep)
        leftList.append(int(leftId))
        rightList.append(int(rightId))


counter = Counter(rightList)
result = 0
for val in leftList:
    result += val * counter.get(val, 0)

print(result)
