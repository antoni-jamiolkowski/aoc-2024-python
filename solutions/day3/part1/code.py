import re


file_path = "input.txt"

result = 0
with open(file_path) as file:
    for row in file:
        muls = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", row)
        result += sum(int(ln) * int(rn) for ln, rn in muls)

print(result)