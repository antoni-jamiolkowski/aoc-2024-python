# file_path = "short_input.txt"
file_path = "input.txt"

MAPA = []
trailheads = []
with open(file_path) as file:
    for i, line in enumerate(file):
        partial_map = []
        for j, el in enumerate(line.strip()):
            el = int(el)
            partial_map.append(el)
            if el == 0:
                trailheads.append((i, j))
        MAPA.append(partial_map)

EDGE_1 = len(MAPA)
EDGE_2 = len(MAPA[0])

def in_bounds(x1, x2) -> bool:
    return (0 <= x1 < EDGE_1) and (0 <= x2 < EDGE_2)

def find_trails(i, j) -> list[tuple[int, int]]:
    here = MAPA[i][j]
    if here == 9:
        return [(i, j)]
    
    trails = []
    for (n, m) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if in_bounds(n, m) and here + 1 == MAPA[n][m]:
            trails.extend(find_trails(n,m))

    return trails


final_result = 0
for (i, j) in trailheads:
    all_trail_paths = find_trails(i, j)
    trailhead_score = len(all_trail_paths)
    final_result += trailhead_score

print(final_result)
