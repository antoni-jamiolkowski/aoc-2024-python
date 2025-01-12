sep = " "
file_path = "input.txt"
bad_levels_tolerated = 1

def difference(a, b):
    if a <= b:
        return b - a
    else:
        return a - b

def is_line_safe(line: str) -> bool:
    levels = [int(level) for level in line.strip().split(sep)]
    safe_lst = [_inner_is_line_safe(levels)]
    for i in range(len(levels)):
        if any(safe_lst):
            return True
        
        cpy_levels = levels.copy()
        del cpy_levels[i]
        safe_lst.append(_inner_is_line_safe(cpy_levels))

    return any(safe_lst)

def _inner_is_line_safe(levels: list[int]) -> bool:
    # levels = line.strip().split(sep)
    a, b = levels[0], levels[1]
    monotonicity = get_monotonicity(a, b)
    diff = difference(a, b)
    if diff < 1 or diff > 3:
            return False

    for a, b in zip(levels[1:-1], levels[2:]):
        # a, b = int(a), int(b)
        mono = get_monotonicity(a, b)
        if mono != monotonicity:
            return False
        
        diff = difference(a, b)
        if diff < 1 or diff > 3:
            return False
        
    return True

def get_monotonicity(a: int, b: int) -> int:
    if a > b:
        return -1
    elif b > a:
        return 1
    else:
        return 0

result = 0
with open(file_path) as file:
    for line in file:
        if is_line_safe(line):
            result += 1

print(result)