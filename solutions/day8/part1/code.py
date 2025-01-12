from collections import defaultdict

# file_path = "short_input.txt"
file_path = "input.txt"

anntenas = set()
mapa = []
locations = defaultdict(list)
ANNTENA_LOCS = set()
with open(file_path) as file:
    for i, line in enumerate(file):
        mapa_h = []
        for j, el in enumerate(line.strip()):
            if el not in anntenas and el != ".":
                anntenas.add(el)
            if el != ".":
                locations[el].append((i, j))
                ANNTENA_LOCS.add((i,j))
            mapa_h.append(el)
        mapa.append(mapa_h)


EDGE_1 = len(mapa)
EDGE_2 = len(mapa[0])

def in_bounds(x1, x2) -> bool:
    return (0 <= x1 < EDGE_1) and (0 <= x2 < EDGE_2)

# def not_in_another_anntena(x1, x2) -> bool:
#     return (x1, x2) not in ANNTENA_LOCS


# final_result = 0
final_result = set()
# final_result = []

for an_type, an_locs in locations.items():
    # semi_result = set()
    for x_ind in range(len(an_locs) - 1):
        for y_ind in range(x_ind + 1, len(an_locs)):
            if an_locs[x_ind][0] != an_locs[y_ind][0] and an_locs[x_ind][1] < an_locs[y_ind][1]:
                a1, a2 = an_locs[x_ind]
                b1, b2 = an_locs[y_ind]
            elif an_locs[x_ind][0] != an_locs[y_ind][0] and an_locs[x_ind][1] > an_locs[y_ind][1]:
                a1, a2 = an_locs[y_ind]
                b1, b2 = an_locs[x_ind]
            else:
                raise ValueError(f"Unexpected arrangement of anntenas. Anntena type: {an_type}. Locations: {an_locs[x_ind]} and {an_locs[y_ind]}.")
            
            e1 = 2 * a1 - b1            
            e2 = 2 * a2 - b2

            if in_bounds(e1, e2):# and not_in_another_anntena(e1, e2):
                # final_result += 1
                # print((e1, e2), f"Anntena type: {an_type}. Locations: {an_locs[x_ind]} and {an_locs[y_ind]}.")
                # semi_result.add((e1, e2))
                final_result.add((e1, e2))
                mapa[e1][e2] = "#"
                # final_result.append((e1, e2))


            g1 = 2 * b1 - a1
            g2 = 2 * b2 - a2

            # FIXME: What about a weird case? ("non proper diagonal")
            if in_bounds(g1, g2):# and not_in_another_anntena(g1, g2):
                # final_result += 1
                # print((g1, g2), f"Anntena type: {an_type}. Locations: {an_locs[x_ind]} and {an_locs[y_ind]}.")
                # semi_result.add((g1, g2))
                final_result.add((g1, g2))
                mapa[g1][g2] = "#"
                # final_result.append((g1, g2))
    
    # final_result += len(semi_result)

print(len(final_result))
# print(len(final_result), final_result)
# print(len(set(final_result)), set(final_result))

# from collections import Counter
# print(Counter(final_result))

# print("===" * 4)
# for line in mapa:
#     print("".join(line))
# print("===" * 4)