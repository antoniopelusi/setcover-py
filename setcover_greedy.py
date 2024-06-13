def set_cover(universe, subsets):
    covered = set()
    cover = []

    while covered != universe:
        subset = max(subsets, key=lambda s: len(s - covered))
        cover.append(subset)
        covered.update(subset)
    return cover

universe = {1, 2, 3, 4, 5}
subsets = [{1, 2, 3}, {2, 4}, {3, 4, 5}, {5}]

solution = set_cover(universe, subsets)

print("Greedy set cover:")
for s in solution:
    print(s)
