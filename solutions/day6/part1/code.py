file_path = "input.txt"

guard_pos = None
guard_val = None
mapa = []
with open(file_path) as file:
    for i, row in enumerate(file):
        mapa_h = []
        for j, el in enumerate(row.strip()):
            mapa_h.append(el)
            if el in {"<", ">", "^", "v"}:
                guard_pos = (i, j)
                guard_val = el
        mapa.append(mapa_h)


guard_on_mapa = True
while guard_on_mapa:
    if guard_val == "^":
        vi = guard_pos[0] - 1
        hi = guard_pos[1]

        if vi < 0:
            mapa[guard_pos[0]][guard_pos[1]] = "X"
            break

        if mapa[vi][hi] == "#":
            guard_val = ">"
            continue
        else:
            mapa[guard_pos[0]][guard_pos[1]] = "X"
            guard_pos = (vi, hi)
            continue

    elif guard_val == ">":
        vi = guard_pos[0]
        hi = guard_pos[1] + 1

        if hi >= len(mapa[0]):
            mapa[guard_pos[0]][guard_pos[1]] = "X"
            break

        if mapa[vi][hi] == "#":
            guard_val = "v"
            continue
        else:
            mapa[guard_pos[0]][guard_pos[1]] = "X"
            guard_pos = (vi, hi)
            continue

    elif guard_val == "v":
        vi = guard_pos[0] + 1
        hi = guard_pos[1]

        if vi >= len(mapa):
            mapa[guard_pos[0]][guard_pos[1]] = "X"
            break

        if mapa[vi][hi] == "#":
            guard_val = "<"
            continue
        else:
            mapa[guard_pos[0]][guard_pos[1]] = "X"
            guard_pos = (vi, hi)
            continue

    elif guard_val == "<":
        vi = guard_pos[0]
        hi = guard_pos[1] - 1

        if hi < 0:
            mapa[guard_pos[0]][guard_pos[1]] = "X"
            break

        if mapa[vi][hi] == "#":
            guard_val = "^"
            continue
        else:
            mapa[guard_pos[0]][guard_pos[1]] = "X"
            guard_pos = (vi, hi)
            continue
    
    else:
        raise ValueError("Bad guard icon.")


final_result = 0
for row in mapa:
    for el in row:
        if el == "X":
            final_result += 1

print(final_result)