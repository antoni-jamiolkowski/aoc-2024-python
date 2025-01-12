from itertools import product
# from collections import defaultdict
from copy import copy, deepcopy


file_path = "input.txt"

# register_blocks_0 = defaultdict(list)
# register_blocks_1 = defaultdict(list)

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
            # elif el == "#":
            #     register_blocks_0[i].append(j)
            #     register_blocks_1[j].append(i)
        
        mapa_original.append(mapa_h)

mapa_original[guard_pos_original[0]][guard_pos_original[1]] = "|"

# mapa_original[3][4] = "#"


def print_mapa(mapa, ogpos, last_pos, the_thing):
    print("===" * 4)
    
    if ogpos is not None:
        dfsdf = deepcopy(mapa[ogpos[0]][ogpos[1]])
        mapa[ogpos[0]][ogpos[1]] = "^"

    
    if last_pos is not None:
        fdgdf = deepcopy(mapa[last_pos[0]][last_pos[1]])
        mapa[last_pos[0]][last_pos[1]] = "X"
    if the_thing is not None:
        mapa[the_thing[0]][the_thing[1]] = "H"
    for line in mapa:
        print("".join(line))
    print("===" * 4)
    if ogpos is not None:
        mapa[ogpos[0]][ogpos[1]] = dfsdf
    if last_pos is not None:
        mapa[last_pos[0]][last_pos[1]] = fdgdf

def any_dot_or_opposite(mapa, g_dir, current_pos):
    if g_dir == "^":
        for i in reversed(range(current_pos[0])):
            if mapa[i][current_pos[1]] in {".", "-"}:
                return True
            elif mapa[i][current_pos[1]] in {"#", "O"}:
                return False
    elif g_dir == ">":
        for j in range(current_pos[1] + 1, len(mapa[0])):
            if mapa[current_pos[0]][j] in {".", "|"}:
                return True
            elif mapa[current_pos[0]][j] in {"#", "O"}:
                return False
    elif g_dir == "v":
        for i in range(current_pos[0] + 1, len(mapa)):
            if mapa[i][current_pos[1]] in {".", "-"}:
                return True
            elif mapa[i][current_pos[1]] in {"#", "O"}:
                return False
    elif g_dir == "<":
        for j in reversed(range(current_pos[1])):
            if mapa[current_pos[0]][j] in {".", "|"}:
                return True
            elif mapa[current_pos[0]][j] in {"#", "O"}:
                return False
    else:
        raise ValueError("sdfsdf")
    
    return False
    

# rb1, rb0, guard_val, guard_pos
# def is_block_ahead(rb_a, rb_b, g_val, g_pos) -> bool:
#     print(g_val, g_pos)
#     print(rb_a, rb_b)
#     if g_val == "^":
#         print("tu1")
#         for v in rb_b[g_pos[1]]:
#             print(v, g_pos[0], v < g_pos[0])
#         return any(v < g_pos[0] for v in rb_b[g_pos[1]])
#     elif g_val == ">":
#         print("tu2")
#         for v in rb_a[g_pos[0]]:
#             print(v, g_pos[1], v > g_pos[1])
#         return any(v > g_pos[1] for v in rb_a[g_pos[0]])
#     elif g_val == "v":
#         print("tu3")
#         for v in rb_b[g_pos[1]]:
#             print(v, g_pos[0], v > g_pos[0])
#         return any(v > g_pos[0] for v in rb_b[g_pos[1]])
#     elif g_val == "<":
#         print("tu4")
        
#         for v in rb_a[g_pos[0]]:
#             print(v, g_pos[1], v < g_pos[1])
#         return any(v < g_pos[1] for v in rb_a[g_pos[0]])
#     else:
#         raise ValueError("sdfsdf")

# def get_number_of_path_elemenents(mapa) -> int:
#     result = defaultdict(int)
#     for row in mapa:
#         for el in row:
#             if el in {"-", "|", "+"}:
#                 result[el] += 1
#     return result

# def compare(a, b) -> bool:
#     for el in ["-", "|", "+"]:
#         if a[el] != b[el]:
#             return False
        
#     return True

# def each_visited_point_twice(a) -> bool:
#     for v in a.values():
#         if v < 2:
#             return False
        
#     return True

# def strb(a):
#     if a:
#         return "T"
#     else:
#         return "F"

# def is_more_to_explore(mapa, current_pos, current_val, i) -> bool:
#     if current_val == "^":
#         explore_start_indx = current_pos[0]
#         to_check = range(explore_start_indx)
#         if i == 87:
#             print(to_check)
        
#         search_party = []
#         for indx in to_check:
#             if i == 87:
#                 print(mapa[indx][current_pos[1]])
#             # search_party.append(mapa[indx][current_pos[1]] == ".")
#             search_party.append(mapa[indx][current_pos[1]])
#     elif current_val == "v":
#         explore_start_indx = current_pos[0]
#         to_check = range(explore_start_indx + 1, len(mapa))
#         if i == 87:
#             print(to_check)
#         search_party = []
#         for indx in to_check:
#             if i == 87:
#                 print(mapa[indx][current_pos[1]])
#             # search_party.append(mapa[indx][current_pos[1]] == ".")
#             search_party.append(mapa[indx][current_pos[1]])
#     elif current_val == ">":
#         explore_start_indx = current_pos[1]
#         to_check = range(explore_start_indx + 1, len(mapa[0]))
#         if i == 87:
#             print(to_check)
#         search_party = []
#         for indx in to_check:
#             if i == 87:
#                 print(mapa[current_pos[0]][indx])
#             # search_party.append(mapa[current_pos[0]][indx] == ".")
#             search_party.append(mapa[current_pos[0]][indx])
#     elif current_val == "<":
#         explore_start_indx = current_pos[1]
#         to_check = range(explore_start_indx)
#         if i == 87:
#             print(to_check)
#         search_party = []
#         for indx in to_check:
#             if i == 87:
#                 print("it should be here...")
#                 print(mapa[current_pos[0]][indx])
#             # search_party.append(mapa[current_pos[0]][indx] == ".")
#             search_party.append(mapa[current_pos[0]][indx])
#     else:
#         raise ValueError("Bad guard icon.")
    
#     if i == 87:
#         print(search_party, current_pos, current_val)

#     return "." in search_party and "#" not in search_party


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


# # we have to add the new obstackle ...
# OG_is_block_ahead = {}
# # for direction in ["^", ">", "v", "<"]:
# for p in product(range(len(mapa_original)), range(len(mapa_original[0]))):
#     # edges
#     # the empty list case
#     OG_is_block_ahead[("^", p)] = any(mapa_original[i][p[1]] == "#" for i in range(p[0]))

# for p in product(range(len(mapa_original)), range(len(mapa_original[0]))):
#     OG_is_block_ahead[("v", p)] = any(mapa_original[i][p[1]] == "#" for i in range(p[0] + 1, len(mapa_original)))

# for p in product(range(len(mapa_original)), range(len(mapa_original[0]))):
#     OG_is_block_ahead[("<", p)] = any(mapa_original[p[0]][i] == "#" for i in range(p[1]))

# for p in product(range(len(mapa_original)), range(len(mapa_original[0]))):
#     OG_is_block_ahead[(">", p)] = any(mapa_original[p[0]][i] == "#" for i in range(p[1] + 1, len(mapa_original[0])))

import pickle

# with open('input.txt-OG_is_block_ahead.pkl', 'wb') as f:
#     pickle.dump(OG_is_block_ahead, f)
        
with open('input.txt-OG_is_block_ahead.pkl', 'rb') as f:
    OG_is_block_ahead = pickle.load(f)

# print(mapa_original)
# print(is_block_ahead)
# mapa = deepcopy(mapa_original)
# print("===" * 4)
# print("^^^ " * 3)
# mapa[guard_pos_original[0]][guard_pos_original[1]] = "."
# for p in product(range(len(mapa_original)), range(len(mapa_original[0]))):
#     if mapa[p[0]][p[1]] == "#":
#         continue
#     else:
#         mapa[p[0]][p[1]] = strb(is_block_ahead[("^", p)])
# for line in mapa:
#     print("".join(line))
# print("^^^ " * 3)
# print("===" * 4)

# mapa = deepcopy(mapa_original)
# print("===" * 4)
# print(">>> " * 3)
# mapa[guard_pos_original[0]][guard_pos_original[1]] = "."
# for p in product(range(len(mapa_original)), range(len(mapa_original[0]))):
#     if mapa[p[0]][p[1]] == "#":
#         continue
#     else:
#         mapa[p[0]][p[1]] = strb(is_block_ahead[(">", p)])
# for line in mapa:
#     print("".join(line))
# print(">>> " * 3)
# print("===" * 4)

# mapa = deepcopy(mapa_original)
# print("===" * 4)
# print("vvv " * 3)
# mapa[guard_pos_original[0]][guard_pos_original[1]] = "."
# for p in product(range(len(mapa_original)), range(len(mapa_original[0]))):
#     if mapa[p[0]][p[1]] == "#":
#         continue
#     else:
#         mapa[p[0]][p[1]] = strb(is_block_ahead[("v", p)])
# for line in mapa:
#     print("".join(line))
# print("vvv " * 3)
# print("===" * 4)

# mapa = deepcopy(mapa_original)
# print("===" * 4)
# print("<<< " * 3)
# mapa[guard_pos_original[0]][guard_pos_original[1]] = "."
# for p in product(range(len(mapa_original)), range(len(mapa_original[0]))):
#     if mapa[p[0]][p[1]] == "#":
#         continue
#     else:
#         mapa[p[0]][p[1]] = strb(is_block_ahead[("<", p)])
# for line in mapa:
#     print("".join(line))
# print("<<< " * 3)
# print("===" * 4)

# mapa = deepcopy(mapa_original)
# print_mapa(mapa, guard_pos_original)

# print("\n\n")
# print("##" * 10)
# print("## " * 2, "Add new obstackle...", " ## " * 2)
# print("##" * 10)

# mapa = deepcopy(mapa_original)
# t, y = 3, 4
# mapa_original[t][y] = "O"
def update_the_block_dict(is_block_ahead, p, mapa):
    t, y = p
    for i in range(t + 1, len(mapa)):
        is_block_ahead[("^", (i, y))] = True
    for j in range(y):
        is_block_ahead[(">", (t, j))] = True
    for i in range(t):
        is_block_ahead[("v", (i, y))] = True
    for j in range(y + 1, len(mapa[0])):
        is_block_ahead[("<", (t, j))] = True

#####

# mapa = deepcopy(mapa_original)
# print("===" * 4)
# print("^^^ " * 3)
# mapa[guard_pos_original[0]][guard_pos_original[1]] = "."
# for p in product(range(len(mapa_original)), range(len(mapa_original[0]))):
#     if mapa[p[0]][p[1]] in {"#", "O"}:
#         continue
#     else:
#         mapa[p[0]][p[1]] = strb(is_block_ahead[("^", p)])
# for line in mapa:
#     print("".join(line))
# print("^^^ " * 3)
# print("===" * 4)

# mapa = deepcopy(mapa_original)
# print("===" * 4)
# print(">>> " * 3)
# mapa[guard_pos_original[0]][guard_pos_original[1]] = "."
# for p in product(range(len(mapa_original)), range(len(mapa_original[0]))):
#     if mapa[p[0]][p[1]] in {"#", "O"}:
#         continue
#     else:
#         mapa[p[0]][p[1]] = strb(is_block_ahead[(">", p)])
# for line in mapa:
#     print("".join(line))
# print(">>> " * 3)
# print("===" * 4)

# mapa = deepcopy(mapa_original)
# print("===" * 4)
# print("vvv " * 3)
# mapa[guard_pos_original[0]][guard_pos_original[1]] = "."
# for p in product(range(len(mapa_original)), range(len(mapa_original[0]))):
#     if mapa[p[0]][p[1]] in {"#", "O"}:
#         continue
#     else:
#         mapa[p[0]][p[1]] = strb(is_block_ahead[("v", p)])
# for line in mapa:
#     print("".join(line))
# print("vvv " * 3)
# print("===" * 4)

# mapa = deepcopy(mapa_original)
# print("===" * 4)
# print("<<< " * 3)
# mapa[guard_pos_original[0]][guard_pos_original[1]] = "."
# for p in product(range(len(mapa_original)), range(len(mapa_original[0]))):
#     if mapa[p[0]][p[1]] in {"#", "O"}:
#         continue
#     else:
#         mapa[p[0]][p[1]] = strb(is_block_ahead[("<", p)])
# for line in mapa:
#     print("".join(line))
# print("<<< " * 3)
# print("===" * 4)

# mapa = deepcopy(mapa_original)
# print_mapa(mapa, guard_pos_original)

# raise AssertionError


final_result = 0

se = input("Give me range...")
se = tuple(int(i) for i in se.split(","))

posss = list(posss)[se[0]:se[1]]
for i, mapa_pos in enumerate(posss):
# for i, mapa_pos in enumerate(posss[:5]):

# for mapa_pos in [posss[7]]:
    print(i, " / ", len(posss))

    mapa = deepcopy(mapa_original)
    mapa[mapa_pos[0]][mapa_pos[1]] = "O"

    is_block_ahead = deepcopy(OG_is_block_ahead)
    update_the_block_dict(is_block_ahead, mapa_pos, mapa)

    guard_pos = copy(guard_pos_original)
    guard_val = copy(guard_val_original)

    # rb0 = deepcopy(register_blocks_0)
    # rb1 = deepcopy(register_blocks_1)
    # rb0[mapa_pos[0]].append(mapa_pos[1])
    # rb1[mapa_pos[1]].append(mapa_pos[0])


    # pos_history = defaultdict(int)

    guard_on_mapa = True
    rotation_recently = False
    while guard_on_mapa:
        # print_mapa(mapa, None, None, None)
        # print("===" * 4)
        # mapa[guard_pos_original[0]][guard_pos_original[1]] = "^"
        # for line in mapa:
        #     print("".join(line))
        # print("===" * 4)

        # before = get_number_of_path_elemenents(mapa)
        
        if guard_val == "^":

            explore_start_indx = guard_pos[0]
            to_check = reversed(range(explore_start_indx))
            
            for indx in to_check:                
                val = mapa[indx][guard_pos[1]]
                if indx == 0 and val not in {"#", "O"}:
                    guard_on_mapa = False
                    break

                if val == "|":
                    if not is_block_ahead[(guard_val, guard_pos)]:
                        guard_on_mapa = False
                        # print_mapa(mapa, guard_pos_original)
                        break
                    elif any_dot_or_opposite(mapa, guard_val, (indx, guard_pos[1])):
                        continue
                    else:
                        # print("TUTAJ JEST PETLA", "!!" * 4)
                        final_result += 1
                        guard_on_mapa = False
                        # print_mapa(mapa, guard_pos_original, guard_pos, (indx, guard_pos[1]))
                        # print(guard_val, guard_pos)
                        # print(val, (indx, guard_pos[1]))
                        break
                elif val == ".":
                    mapa[indx][guard_pos[1]] = "|"
                elif val == "-":
                    mapa[indx][guard_pos[1]] = "+"
                elif val == "+": #FIXME: Moze tutaj z patrzeniem na wlasne slady?
                    # Do nothing...
                    pass
                elif val in {"#", "O"}:
                    mapa[indx + 1][guard_pos[1]] = "+"
                    guard_pos = (indx + 1, guard_pos[1])
                    guard_val = ">"
                    break
                else:
                    raise ValueError(f"Bad map icon: {val}")

        elif guard_val == ">":

            explore_start_indx = guard_pos[1]
            to_check = range(explore_start_indx + 1, len(mapa[0]))
            
            for indx in to_check:                
                val = mapa[guard_pos[0]][indx]
                if indx == (len(mapa[0]) - 1) and val not in {"#", "O"}:
                    guard_on_mapa = False
                    break


                if val == "-":
                    if not is_block_ahead[(guard_val, guard_pos)]:
                        guard_on_mapa = False
                        # print_mapa(mapa, guard_pos_original)
                        break
                    elif any_dot_or_opposite(mapa, guard_val, (guard_pos[0], indx)):
                        continue
                    else:
                        # print("TUTAJ JEST PETLA", "!!" * 4)
                        final_result += 1
                        guard_on_mapa = False
                        # print_mapa(mapa, guard_pos_original)
                        # print_mapa(mapa, guard_pos_original, guard_pos, (guard_pos[0], indx))
                        # print(guard_val, guard_pos)
                        # print(val, (indx, guard_pos[1]))
                        break
                elif val == ".":
                    mapa[guard_pos[0]][indx] = "-"
                elif val == "|":
                    mapa[guard_pos[0]][indx] = "+"
                elif val == "+":
                    # Do nothing...
                    pass
                elif val in {"#", "O"}:
                    mapa[guard_pos[0]][indx - 1] = "+"
                    guard_pos = (guard_pos[0], indx - 1)
                    guard_val = "v"
                    break
                else:
                    raise ValueError(f"Bad map icon: {val}")

        elif guard_val == "v":

            explore_start_indx = guard_pos[0]
            to_check = range(explore_start_indx + 1, len(mapa))
            
            for indx in to_check:                
                val = mapa[indx][guard_pos[1]]
                if indx == (len(mapa) - 1) and val not in {"#", "O"}:
                    guard_on_mapa = False
                    break


                if val == "|":
                    if not is_block_ahead[(guard_val, guard_pos)]:
                        guard_on_mapa = False
                        # print_mapa(mapa, guard_pos_original)
                        # print(guard_val, guard_pos)
                        # print(val, (indx, guard_pos[1]))
                        break
                    elif any_dot_or_opposite(mapa, guard_val, (indx, guard_pos[1])):
                        continue
                    else:
                        # print("TUTAJ JEST PETLA", "!!" * 4)
                        final_result += 1
                        guard_on_mapa = False
                        # print_mapa(mapa, guard_pos_original)
                        # print_mapa(mapa, guard_pos_original, guard_pos, (indx, guard_pos[1]))
                        # print(guard_val, guard_pos)
                        # print(val, (indx, guard_pos[1]))
                        break
                elif val == ".":
                    mapa[indx][guard_pos[1]] = "|"
                elif val == "-":
                    mapa[indx][guard_pos[1]] = "+"
                elif val == "+":
                    # Do nothing...
                    pass
                elif val in {"#", "O"}:
                    mapa[indx - 1][guard_pos[1]] = "+"
                    guard_pos = (indx - 1, guard_pos[1])
                    guard_val = "<"
                    break
                else:
                    raise ValueError(f"Bad map icon: {val}")

        elif guard_val == "<":

            explore_start_indx = guard_pos[1]
            to_check = reversed(range(explore_start_indx))
            
            for indx in to_check:                
                val = mapa[guard_pos[0]][indx]
                if indx == 0 and val not in {"#", "O"}:
                    guard_on_mapa = False
                    break


                if val == "-":
                    if not is_block_ahead[(guard_val, guard_pos)]:
                        guard_on_mapa = False
                        # print_mapa(mapa, guard_pos_original)
                        break
                    elif any_dot_or_opposite(mapa, guard_val, (guard_pos[0], indx)):
                        continue
                    else:
                        # print("TUTAJ JEST PETLA", "!!" * 4)
                        final_result += 1
                        guard_on_mapa = False
                        # print_mapa(mapa, guard_pos_original)
                        # print_mapa(mapa, guard_pos_original, guard_pos, (guard_pos[0], indx))
                        # print(guard_val, guard_pos)
                        # print(val, (indx, guard_pos[1]))
                        break
                elif val == ".":
                    mapa[guard_pos[0]][indx] = "-"
                elif val == "|":
                    mapa[guard_pos[0]][indx] = "+"
                elif val == "+":
                    # Do nothing...
                    pass
                elif val in {"#", "O"}:
                    mapa[guard_pos[0]][indx + 1] = "+"
                    guard_pos = (guard_pos[0], indx + 1)
                    guard_val = "^"
                    break
                else:
                    raise ValueError(f"Bad map icon: {val}")
        
        else:
            raise ValueError("Bad guard icon.")

print(final_result)