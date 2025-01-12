# from itertools import product
from collections import defaultdict
from copy import copy, deepcopy


file_path = "input.txt"

guard_pos_original = None
guard_val_original = None
mapa_original = []
with open(file_path) as file:
    for i, row in enumerate(file):
        mapa_h = []
        for j, el in enumerate(row.strip()):
            # mapa_h.append("o" if el == "." else el)
            mapa_h.append(el)
            if el in {"<", ">", "^", "v"}:
                guard_pos_original = (i, j)
                guard_val_original = el
        mapa_original.append(mapa_h)


def get_number_of_path_elemenents(mapa) -> int:
    result = defaultdict(int)
    for row in mapa:
        for el in row:
            if el in {"-", "|", "+"}:
                result[el] += 1
    return result

def compare(a, b) -> bool:
    for el in ["-", "|", "+"]:
        if a[el] != b[el]:
            return False
        
    return True

def each_visited_point_twice(a) -> bool:
    for v in a.values():
        if v < 2:
            return False
        
    return True

def is_more_to_explore(mapa, current_pos, current_val, i) -> bool:
    if current_val == "^":
        explore_start_indx = current_pos[0]
        to_check = range(explore_start_indx)
        if i == 87:
            print(to_check)
        
        search_party = []
        for indx in to_check:
            if i == 87:
                print(mapa[indx][current_pos[1]])
            # search_party.append(mapa[indx][current_pos[1]] == ".")
            search_party.append(mapa[indx][current_pos[1]])
    elif current_val == "v":
        explore_start_indx = current_pos[0]
        to_check = range(explore_start_indx + 1, len(mapa))
        if i == 87:
            print(to_check)
        search_party = []
        for indx in to_check:
            if i == 87:
                print(mapa[indx][current_pos[1]])
            # search_party.append(mapa[indx][current_pos[1]] == ".")
            search_party.append(mapa[indx][current_pos[1]])
    elif current_val == ">":
        explore_start_indx = current_pos[1]
        to_check = range(explore_start_indx + 1, len(mapa[0]))
        if i == 87:
            print(to_check)
        search_party = []
        for indx in to_check:
            if i == 87:
                print(mapa[current_pos[0]][indx])
            # search_party.append(mapa[current_pos[0]][indx] == ".")
            search_party.append(mapa[current_pos[0]][indx])
    elif current_val == "<":
        explore_start_indx = current_pos[1]
        to_check = range(explore_start_indx)
        if i == 87:
            print(to_check)
        search_party = []
        for indx in to_check:
            if i == 87:
                print("it should be here...")
                print(mapa[current_pos[0]][indx])
            # search_party.append(mapa[current_pos[0]][indx] == ".")
            search_party.append(mapa[current_pos[0]][indx])
    else:
        raise ValueError("Bad guard icon.")
    
    if i == 87:
        print(search_party, current_pos, current_val)

    return "." in search_party and "#" not in search_party


def guard_visited_here():
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


    posss = set()
    for i, row in enumerate(mapa):
        for j, el in enumerate(row):
            if el == "X":
                posss.add((i,j))

    return posss



posss = guard_visited_here()
print(len(posss))

# all_mapa_pos = set(product(range(len(mapa_original)), range(len(mapa_original[0]))))
posss.remove(guard_pos_original)

# print(len(all_mapa_pos))

# all_mapa_pos = all_mapa_pos - posss
# print(len(all_mapa_pos))


final_result = 0

for i, mapa_pos in enumerate(posss):
    print(i, " / ", len(posss))
    # if mapa_original[mapa_pos[0]][mapa_pos[1]] == "#":
    #     continue

    mapa = deepcopy(mapa_original)
    mapa[mapa_pos[0]][mapa_pos[1]] = "O"

    guard_pos = copy(guard_pos_original)
    guard_val = copy(guard_val_original)

    pos_history = defaultdict(int)

    guard_on_mapa = True
    rotation_recently = False
    while guard_on_mapa:
        # if i == 87:
        #     print("===" * 4)
        #     mapa[guard_pos_original[0]][guard_pos_original[1]] = "^"
        #     for line in mapa:
        #         print("".join(line))
        #     print("===" * 4)
        
        if guard_val == "^":
            explore_start_indx = guard_pos[0]
            to_check = range(explore_start_indx)
            
            search_party = []
            for indx in to_check:
                val = mapa[indx][guard_pos[1]]
                if val in {".", "|", "-"}:
                    mapa[indx][guard_pos[1]] = "|"
                elif val == "+":
                    # Do nothing...
                    pass
                elif val in {"#", "O"}:
                    mapa[...][...] == "+"
                    guard_pos = (..., ...)
                    break
                else:
                    raise ValueError("Bad map icon.")
            
            vi = guard_pos[0] - 1
            hi = guard_pos[1]

            if vi < 0:
                mapa[guard_pos[0]][guard_pos[1]] = "|"
                break

            if mapa[vi][hi] in {"#", "O"}:
                mapa[guard_pos[0]][guard_pos[1]] = "+"
                guard_val = ">"
                rotation_recently = True
                continue
            else:
                before = get_number_of_path_elemenents(mapa)

                if not rotation_recently:
                    mapa[guard_pos[0]][guard_pos[1]] = "|"

                after = get_number_of_path_elemenents(mapa)

                pos_history[guard_pos] += 1

                if compare(before, after) and not rotation_recently and not is_more_to_explore(mapa, guard_pos, guard_val, i):# and each_visited_point_twice(pos_history):
                    # print("===" * 4)
                    # mapa[guard_pos_original[0]][guard_pos_original[1]] = "^"
                    # for line in mapa:
                    #     print("".join(line))
                    # print("===" * 4)
                    # print(pos_history)
                    final_result += 1
                    break

                guard_pos = (vi, hi)
                rotation_recently = False
                continue

        elif guard_val == ">":
            vi = guard_pos[0]
            hi = guard_pos[1] + 1

            if hi >= len(mapa[0]):
                mapa[guard_pos[0]][guard_pos[1]] = "-"
                break

            if mapa[vi][hi] in {"#", "O"}:
                mapa[guard_pos[0]][guard_pos[1]] = "+"
                guard_val = "v"
                rotation_recently = True
                continue
            else:
                before = get_number_of_path_elemenents(mapa)

                if not rotation_recently:
                    mapa[guard_pos[0]][guard_pos[1]] = "-"

                after = get_number_of_path_elemenents(mapa)

                # pos_history[guard_pos] += 1

                if compare(before, after) and not rotation_recently and not is_more_to_explore(mapa, guard_pos, guard_val, i):# and each_visited_point_twice(pos_history):
                    # print("===" * 4)
                    # mapa[guard_pos_original[0]][guard_pos_original[1]] = "^"
                    # for line in mapa:
                    #     print("".join(line))
                    # print("===" * 4)
                    # print(pos_history)
                    final_result += 1
                    break


                guard_pos = (vi, hi)
                rotation_recently = False
                continue

        elif guard_val == "v":
            vi = guard_pos[0] + 1
            hi = guard_pos[1]

            if vi >= len(mapa):
                mapa[guard_pos[0]][guard_pos[1]] = "|"
                break

            if mapa[vi][hi] in {"#", "O"}:
                mapa[guard_pos[0]][guard_pos[1]] = "+"
                guard_val = "<"
                rotation_recently = True
                continue
            else:
                before = get_number_of_path_elemenents(mapa)

                if not rotation_recently:
                    mapa[guard_pos[0]][guard_pos[1]] = "|"

                after = get_number_of_path_elemenents(mapa)

                # pos_history[guard_pos] += 1

                if compare(before, after) and not rotation_recently and not is_more_to_explore(mapa, guard_pos, guard_val, i):# and each_visited_point_twice(pos_history):
                    # print("===" * 4)
                    # mapa[guard_pos_original[0]][guard_pos_original[1]] = "^"
                    # for line in mapa:
                    #     print("".join(line))
                    # print("===" * 4)
                    # print(pos_history)
                    final_result += 1
                    break

                guard_pos = (vi, hi)
                rotation_recently = False
                continue

        elif guard_val == "<":
            vi = guard_pos[0]
            hi = guard_pos[1] - 1

            if hi < 0:
                mapa[guard_pos[0]][guard_pos[1]] = "-"
                break

            if mapa[vi][hi] in {"#", "O"}:
                mapa[guard_pos[0]][guard_pos[1]] = "+"
                guard_val = "^"
                rotation_recently = True
                continue
            else:
                
                before = get_number_of_path_elemenents(mapa)

                if not rotation_recently:
                    mapa[guard_pos[0]][guard_pos[1]] = "-"

                after = get_number_of_path_elemenents(mapa)

                # pos_history[guard_pos] += 1

                if compare(before, after) and not rotation_recently and not is_more_to_explore(mapa, guard_pos, guard_val, i):# and each_visited_point_twice(pos_history):
                    # print("===" * 4)
                    # mapa[guard_pos_original[0]][guard_pos_original[1]] = "^"
                    # for line in mapa:
                    #     print("".join(line))
                    # print("===" * 4)
                    # print(pos_history)
                    final_result += 1
                    break

    
                guard_pos = (vi, hi)
                rotation_recently = False
                continue
        
        else:
            raise ValueError("Bad guard icon.")

print(final_result)