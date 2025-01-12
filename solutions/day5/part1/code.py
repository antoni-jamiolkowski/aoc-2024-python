from collections import defaultdict
from statistics import mean

file_path = "input.txt"

final_result = 0
rules = defaultdict(list)
with open(file_path) as file:
    for line in file:
        if "|" in line:
            ln, rn = line.split("|")
            ln, rn = int(ln), int(rn)
            rules[ln].append(rn)
        elif "," in line:
            pages = [int(n) for n in line.split(",")]
            valid = []
            for indx, pn in enumerate(pages):
                rns = [rn for rn in rules[pn] if rn in pages]
                valid.append(all(rn in pages[indx:] for rn in rns))
                    
            if all(valid):        
                mid = mean(range(len(pages)))
                final_result += pages[mid]
        else:
            continue

print(final_result)
