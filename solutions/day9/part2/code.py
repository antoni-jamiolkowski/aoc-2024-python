file_path = "short_input.txt"
# file_path = "input.txt"

# MAPA = []
dense_format: list[int] = []
with open(file_path) as file:
    for i, line in enumerate(file):
        for j, el in enumerate(line.strip()):
            dense_format.append(int(el))


sparse_format: list[str] = []
id_ = 0
for i, el in enumerate(dense_format):
    if i % 2 == 0:
        sparse_format.extend([str(id_) for _ in range(el)])
        id_ += 1
    else:
        sparse_format.extend(["." for _ in range(el)])

print(sparse_format)

# def free_spot(memory_map, current_ind = 0) -> int:
#     for i in range(current_ind, len(memory_map)):
#         if memory_map[i] == ".":
#             return i
#     else:
#         raise Exception("No free space left.")
    

def free_spot(memory_map, space_needed) -> int:
    spot_candidate_space = 0
    for i in range(len(memory_map)):
        if memory_map[i] == ".":
            spot_candidate_space += 1
        else:
            spot_candidate_space = 0
            continue
        
        if spot_candidate_space == space_needed:
            return i
    else:
        raise ValueError("No free space for such file.")
    
def free_spot(memory_map, space_needed) -> int:
    memorando = 0
    for i in range(len(memory_map)):
        if memory_map[i] == ".":
            memorando += 1
        else:
            memorando = 0
            continue

        if memorando == space_needed:
            return i
        
    raise ValueError("No free space for such file.")
    
        



# front_ind = free_spot(sparse_format)
# back_ind = len(sparse_format) - 1
# print("".join(sparse_format))
id_ -= 1
while id_ >= 0:
    
    # print("".join(sparse_format))
    space_needed = 0

    locs = []
    for i, x in enumerate(sparse_format):
        if x == str(id_):
            print("HEE")
            space_needed += 1
            locs.append(i)

    id_ -= 1
    # print(space_needed)

    try:
        back_ind_free_spot = free_spot(sparse_format, space_needed)
    except ValueError as e:
        print("ID: ", id_ + 1)
        # print(e)
        continue

    
    for (n, m) in zip(reversed(locs), reversed(range(back_ind_free_spot - space_needed + 1, back_ind_free_spot + 1))):
        sparse_format[m] = sparse_format[n]
        sparse_format[n] = "."

print("".join(sparse_format))

filesystem_checksum = 0
for i, el in enumerate(sparse_format):
    if el == ".":
        break

    filesystem_checksum += i * int(el)

print(filesystem_checksum)