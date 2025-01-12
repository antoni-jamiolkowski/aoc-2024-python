import re

file_path = "input.txt"

def get_diagonal(horizontal):
    diagonal = []

    k = 0
    l = 1

    g = 0 
    h = 1
    while k < len(horizontal[0]) or l < len(horizontal[0]):
        semi = []
        for i, j in zip(range(g, h), reversed(range(k, l))):
            semi.append(horizontal[i][j])
        diagonal.append("".join(semi))
        
        if h != len(horizontal) + 1:
            h += 1
        
        if h == len(horizontal[0]) + 1:
            g += 1
        elif h == len(horizontal) + 1:
            g -= 1
        
        if l != len(horizontal[0]):
            l += 1

        if h == len(horizontal) + 1:
            k += 1

    return diagonal

def find_all(patterns, source):
    result = 0
    for line in source:
        for p in patterns:
            result += len(re.findall(p, line))

    return result


with open(file_path) as file:
    horizontal = [line.strip() for line in file]
    vertical = ["".join([line[i] for line in horizontal]) for i in range(len(horizontal))]
    diagonal_h = get_diagonal(horizontal)
    diagonal_v = get_diagonal([line for line in reversed(vertical)])

pattern = r"XMAS"
pattern_back = r"SAMX"

final_result = 0
for source in [horizontal, vertical, diagonal_h, diagonal_v]:
    final_result += find_all((pattern, pattern_back), source)

print(final_result)