from itertools import combinations

def optimal_set_cover(universe, subsets):
    for r in range(1, len(subsets) + 1):
        for combination in combinations(subsets, r):
            union = set().union(*combination)
            if union == universe:
                return list(combination)
    return []

universe = {1, 2, 3, 4, 5}
subsets = [{1, 2, 3}, {2, 4}, {3, 4, 5}, {5}]

solution = optimal_set_cover(universe, subsets)

print("Optimal set cover:")
for s in solution:
    print(s)
