# line = "125 17"
line = "6563348 67 395 0 6 4425 89567 739318"

lst = [el for el in line.split()]

N_BLINK = 75

def stonlogic(el: str, depth: int):
    if el == "0":
        val = "1"
        if depth == N_BLINK:
            return val
        else:
            return stonlogic(el=val, depth=depth + 1)
    elif len(el) % 2 == 0:
        l = len(el)
        m = int(l / 2)
        left, right = str(int(el[:m])), str(int(el[m:]))
        
        val = [left, right]
        if depth == N_BLINK:
            return val
        else:
            semir = []
            for x in [left, right]:
                k = stonlogic(x, depth=depth + 1)
                if isinstance(k, str):
                    res.append(k)
                elif isinstance(k, list):
                    res.extend(k)
                else:
                    raise ValueError("INSIDE FFUN: it should reach here...")
            return semir
    else:
        val = str(int(el) * 2024)
        if depth == N_BLINK:
            return val
        else:
            return stonlogic(val, depth=depth + 1)
        

res = []
for y in lst:
    n = stonlogic(y, depth=1)
    if isinstance(n, str):
        res.append(n)
    elif isinstance(n, list):
        res.extend(n)
    else:
        raise ValueError("it should reach here...")



# print(res)
print(len(res))