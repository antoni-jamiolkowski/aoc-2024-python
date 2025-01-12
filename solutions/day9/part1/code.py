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

def free_spot(memory_map, current_ind = 0) -> int:
    for i in range(current_ind, len(memory_map)):
        if memory_map[i] == ".":
            return i
    else:
        raise Exception("No free space left.")


front_ind = free_spot(sparse_format)
back_ind = len(sparse_format) - 1
# print("".join(sparse_format))

while front_ind <= back_ind:
    # print("".join(sparse_format))
    val, sparse_format[back_ind] = sparse_format[back_ind], "."
    # print("".join(sparse_format), back_ind, val, front_ind, sparse_format[front_ind])
    back_ind -= 1
    if val == ".":
        continue
    # print("Past.")

    sparse_format[front_ind] = val
    # print("".join(sparse_format))

    front_ind = free_spot(sparse_format, front_ind)

# print("".join(sparse_format))

filesystem_checksum = 0
for i, el in enumerate(sparse_format):
    if el == ".":
        break

    filesystem_checksum += i * int(el)

print(filesystem_checksum)