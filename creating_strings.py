from itertools import permutations

def generate_permutations(s):
    unique_permutations = sorted(set("".join(p) for p in permutations(s)))
    print(len(unique_permutations))
    for perm in unique_permutations:
        print(perm)

# Read input
s = input().strip()
generate_permutations(s)