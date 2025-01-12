sep = " "
file_path = "short_input.txt"
bad_levels_tolerated = 1


def difference(a, b):
    if a <= b:
        return b - a
    else:
        return a - b
    

def get_monotonicity(a: int, b: int) -> int:
    if a > b:
        return -1
    elif b > a:
        return 1
    else:
        return 0
    

def is_line_safe(line: str) -> bool:
    levels = [int(level) for level in line.strip().split(sep)]
    pairs = list(zip(range(len(levels) - 1), range(1, len(levels))))
    bad_levels = 0
    
    a, b = levels[0], levels[1]
    monotonicity = get_monotonicity(a, b)
    left_edge_diff = difference(a, b)

    print(a,b)
    print("Target: ", "None")
    print("Source: ", monotonicity)
    print("Diff: ", left_edge_diff)

    if not (1 <= left_edge_diff <= 3):
        bad_levels += 1
    
    for i, (i_a, i_b) in enumerate(pairs[1:]): # FIXME: what about right edge?
        a, b = levels[i_a], levels[i_b]
        mono = get_monotonicity(a, b)
        diff = difference(a, b)
        print(a,b)
        print("Target: ", monotonicity)
        print("Source: ", mono)
        print("Diff: ", diff)

        if mono != monotonicity:
            if bad_levels < bad_levels_tolerated:
                if i == 0:
                    try:
                        next_mono = get_monotonicity(levels[i_a + 1], levels[i_b + 1])
                    except Exception:
                        pass
                    if mono == next_mono:
                        monotonicity = mono
                    elif monotonicity == next_mono:
                        pass
                    else:
                        return False
                bad_levels += 1
                continue
            return False
        
        if not (1 <= diff <= 3):
            if bad_levels < bad_levels_tolerated:
                bad_levels += 1
                continue
            return False        
        
    return True


result = 0
with open(file_path) as file:
    for i, line in enumerate(file):
        print("--- " * 3)
        print(line)
        if is_line_safe(line):
            result += 1
        print("--- " * 3)
        print("\n")

print(result)