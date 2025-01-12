import re


file_path = "input.txt"

result = 0
with open(file_path) as file:
    flag = True
    for row in file:
        muls = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", row)
        # print(muls)
        
        semi_result = 0
        for ln, rn, do, dont in muls:
            if len(do) != 0 and len(dont) != 0:
                raise ValueError("Both are in the group - do & don't")
            
            if len(do) != 0:
                flag = True
                continue
            elif len(dont) != 0:
                flag = False
                continue

            if flag:
                semi_result += int(ln) * int(rn)
        result += semi_result

print(result)