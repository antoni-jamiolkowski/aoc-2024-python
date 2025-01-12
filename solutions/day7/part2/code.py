from itertools import product

# file_path = "short_input.txt"
file_path = "input.txt"

cali_equations = []
with open(file_path) as file:
    for line in file:
        result, numbers = line.strip().split(":")
        numbers = list(numbers.strip().split(" "))
        cali_equations.append((result, numbers))

final_result = 0
for ce in cali_equations:
    variations = product("+*|", repeat=len(ce[1]) - 1)
    for var in variations:
        nuin = int(ce[1][0])
        for v, n in zip(var, ce[1][1:]):
            if v == "+":
                nuin += int(n)
            elif v == "*":
                nuin *= int(n)
            elif v == "|":
                nuin = int(str(nuin) + n)
            else:
                raise ValueError("Unexpected symbol.")
        # stin = f"{ce[1][0]}"
        # for v, n in zip(var, ce[1][1:]):
        #     stin += v
        #     stin += n

        # if eval(stin) == int(ce[0]):
        if nuin == int(ce[0]):
            final_result += int(ce[0])
            break

print(final_result)