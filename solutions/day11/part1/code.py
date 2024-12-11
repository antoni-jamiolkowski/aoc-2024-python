# line = "125 17"
line = "6563348 67 395 0 6 4425 89567 739318"

lst = [el for el in line.split()]

N_BLINK = 75

stones = len(lst)
for i in range(N_BLINK):
    print("Blink: ", i + 1)
    ind = 0
    stones = len(lst)

    while ind < stones:
        if lst[ind] == "0":
            lst[ind] = "1"
            ind += 1
        elif len(lst[ind]) % 2 == 0:
            l = len(lst[ind])
            m = int(l / 2)
            left, right = str(int(lst[ind][:m])), str(int(lst[ind][m:]))
            lst.insert(ind+1, right)
            lst[ind] = left
            ind += 2
            stones = len(lst)
        else:
            lst[ind] = str(int(lst[ind]) * 2024)
            ind += 1


print(len(lst))