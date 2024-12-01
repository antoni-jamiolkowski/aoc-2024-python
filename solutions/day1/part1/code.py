def argmin(a):
    return min(range(len(a)), key=lambda x : a[x])

def difference(a, b):
    if a <= b:
        return b - a
    else:
        return a - b

file_path = "input.txt"
sep = " " * 3

leftList = []
rightList = []
n_lines = 0
with open(file_path) as file:
    for row in file:
        leftId, rightId = row.strip().split(sep)
        leftList.append(int(leftId))
        rightList.append(int(rightId))
        n_lines += 1

result = 0
for _ in range(n_lines):
    lMinId = argmin(leftList)
    rMinId = argmin(rightList)
    result += difference(leftList[lMinId], rightList[rMinId])
    del leftList[lMinId]
    del rightList[rMinId]

print(result)
