sep = " "
file_path = "input.txt"

def difference(a, b):
    if a <= b:
        return b - a
    else:
        return a - b

def is_line_safe(line: str) -> bool:
    levels = line.strip().split(sep)
    a, b = int(levels[0]), int(levels[1])
    monotonicity = _get_monotonicity(a, b)
    diff = difference(a, b)
    if diff < 1 or diff > 3:
            return False

    for a, b in zip(levels[1:-1], levels[2:]):
        a, b = int(a), int(b)
        mono = _get_monotonicity(a, b)
        if mono != monotonicity:
            return False
        
        diff = difference(a, b)
        if diff < 1 or diff > 3:
            return False
        
    return True

def _get_monotonicity(a: int, b: int) -> int:
    if a > b:
        return -1
    elif b > a:
        return 1
    else:
        return 0

result = 0
with open(file_path) as file:
    for i, line in enumerate(file):
        if is_line_safe(line):
            result += 1

print(result)