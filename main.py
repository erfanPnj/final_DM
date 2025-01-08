import numpy as np

T = input() # Binary String T


# Create all possible code candidates (1, 2 or 3 digit)
def generate_candidates(T):
    candidates = set()
    n = len(T)
    for i in range(n):
        for length in range(1, 4):
            if i + length <= n:
                candidates.add(T[i:i + length])
    return candidates

candidate_codes = generate_candidates(T)

def is_prefix(codes):
    sorted_codes = sorted(codes)
    for i in range(len(sorted_codes) - 1):
        if sorted_codes[i + 1].startswith(sorted_codes[i]):
            return True
    return False


def valid_subsets(candidates):
    from itertools import combinations
    valid_subsets = []
    candidates = list(candidates)

    for r in range(1, len(candidates) + 1):
        for subset in combinations(candidates, r):
            if not is_prefix(subset):
                valid_subsets.append(subset)
    return valid_subsets


valid_subsets = valid_subsets(candidate_codes)


def check_transform_condition(T, subset):
    n = len(T)

    # Total length of all strings in the subset must not exceed T's length
    if sum(len(code) for code in subset) > n:
        return False

    store_progress = np.zeros(n, dtype=bool)

    subset = sorted(subset, key=len)
    used_strings = set()

    for i in range(n):
        if store_progress[i]:
            continue

        matched = False
        for code in subset:
            # Check if code matches T starting from index i and does not overlap
            if i + len(code) <= n and not store_progress[i:i + len(code)].any():
                if T[i:i + len(code)] == code:
                    store_progress[i:i + len(code)] = True
                    if code not in used_strings:
                        used_strings.add(code)
                    matched = True
                    break

        if not matched:
            return False

    # Check for gaps in coverage
    # Gaps mean there are `0`s between `1`s in `store_progress`
    gaps = np.diff(np.flatnonzero(store_progress))
    if len(gaps) > 0 and any(gaps > 1):
        return False

    return store_progress.all() and (len(subset) == len(used_strings))


    
def store_subsets_with_transform(valid_subsets, T):
    valid_subsets_with_transform = []
    for subset in valid_subsets:
        if check_transform_condition(T, subset):
            valid_subsets_with_transform.append(subset)
    return valid_subsets_with_transform

valid_with_transform = store_subsets_with_transform(valid_subsets, T)


# Output1
print(len(valid_with_transform))
# Output2
n = 0
for subset in valid_with_transform:
    m = 1
    for j in range(len(subset)):
        m *= (26-j)
    n += m
    
print(n%1000000007)

