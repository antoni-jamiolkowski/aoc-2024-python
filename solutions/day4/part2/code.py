file_path = "input.txt"


with open(file_path) as file:
    horizontal = [list(line.strip()) for line in file]


if len(horizontal) != len(horizontal[0]):
    raise ValueError("The puzzle input is not a square.")

final_result = 0
ind = [[[0,0], [0,1], [0,2]],[[1,0], [1,1], [1,2]], [[2,0], [2,1], [2,2]]]


while ind[2][0][0] < len(horizontal) and ind[0][2][1] < len(horizontal):

    try:
        a_loc = ind[1][1]
        if horizontal[a_loc[0]][a_loc[1]] == "A":
            lui = ind[0][0]
            luv = horizontal[lui[0]][lui[1]]

            rdi = ind[2][2]
            rdv = horizontal[rdi[0]][rdi[1]]

            ldi = ind[2][0]
            ldv = horizontal[ldi[0]][ldi[1]]

            rui = ind[0][2]
            ruv = horizontal[rui[0]][rui[1]]
            if ((luv == "M" and rdv == "S") or (luv == "S" and rdv == "M")) and ((ldv == "M" and ruv == "S") or (ldv == "S" and ruv == "M")):
                final_result += 1

    except IndexError:
        continue

    finally:
        if ind[0][2][1] == (len(horizontal[0]) - 1):
            # reset and move down
            ind[0][0][0] += 1
            ind[0][1][0] += 1
            ind[0][2][0] += 1
            ind[1][0][0] += 1
            ind[1][1][0] += 1
            ind[1][2][0] += 1
            ind[2][0][0] += 1
            ind[2][1][0] += 1
            ind[2][2][0] += 1

            ind[0][0][1] = 0
            ind[0][1][1] = 1
            ind[0][2][1] = 2
            ind[1][0][1] = 0
            ind[1][1][1] = 1
            ind[1][2][1] = 2
            ind[2][0][1] = 0
            ind[2][1][1] = 1
            ind[2][2][1] = 2
        else:
            ind[0][0][1] += 1
            ind[0][1][1] += 1
            ind[0][2][1] += 1
            ind[1][0][1] += 1
            ind[1][1][1] += 1
            ind[1][2][1] += 1
            ind[2][0][1] += 1
            ind[2][1][1] += 1
            ind[2][2][1] += 1

print(final_result)
