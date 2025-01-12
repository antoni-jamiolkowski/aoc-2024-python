from collections import defaultdict

file_path = "short_input.txt"
# file_path = "input.txt"

anntenas = set()
mapa = []
locations = defaultdict(list)
with open(file_path) as file:
    for i, line in enumerate(file):
        mapa_h = []
        for j, el in enumerate(line.strip()):
            if el not in anntenas and el != ".":
                anntenas.add(el)
            if el != ".":
                locations[el].append((i, j))
            mapa_h.append(el)
        mapa.append(mapa_h)


EDGE_1 = len(mapa)
EDGE_2 = len(mapa[0])

def in_bounds(x1, x2) -> bool:
    return (0 <= x1 < EDGE_1) and (0 <= x2 < EDGE_2)


final_result = 0
for an_type, an_locs in locations.items():
    for x_ind in range(len(an_locs - 1)):
        for y_ind in range(x_ind + 1, len(an_locs)):
            if an_locs[x_ind][0] > an_locs[y_ind][0] and an_locs[x_ind][1] < an_locs[y_ind][1]:
                a1, a2 = an_locs[x_ind]
                b1, b2 = an_locs[y_ind]
            elif an_locs[x_ind][0] < an_locs[y_ind][0] and an_locs[x_ind][1] > an_locs[y_ind][1]:
                a1, a2 = an_locs[y_ind]
                b1, b2 = an_locs[x_ind]
            else:
                raise ValueError(f"Unexpected arrangement of anntenas. Anntena type: {an_type}. Locations: {an_locs[x_ind]} and {an_locs[y_ind]}.")
            
            # a (bottom left) ... c ... b (top right)
            
            e1 = 2 * a1 - b1
            
            e2 = 2 * a2 - b2

            if in_bounds(e1, e2):
                final_result += 1

            # if e1, e2 in bounds then result += 1

            g1 = 2 * b1 - a1
            g2 = 2 * b2 - a2

            # FIXME: What about a weird case? ("non proper diagonal")
            if in_bounds(g1, g2):
                final_result += 1

            # if g1, g2 in bounds then result += 1

print(final_result)      