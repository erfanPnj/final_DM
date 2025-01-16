#import numpy as np

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


def combinations(iterable, r):
    pool = list(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


def valid_subsets(candidates):
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

    # T should be bigger than the sum of lengths of strings in subset
    if sum(len(code) for code in subset) > n:
        return False

    store_progress = [False] * n

    subset = sorted(subset, key=len)
    used_strings = set()

    for i in range(n):
        if store_progress[i]:
            continue

        matched = False
        for code in subset:
            if i + len(code) <= n and all(not store_progress[j] for j in range(i, i + len(code))):
                if T[i:i + len(code)] == code:
                    for j in range(i, i + len(code)):
                        store_progress[j] = True
                    if code not in used_strings:
                        used_strings.add(code)
                    matched = True
                    break

        if not matched:
            return False
        
    ''' example: if T='0101', you cannot first match a '10' and then
        match '0--1' with a '01'
    '''
    last_index = -1
    for i in range(n):
        if store_progress[i]:
            if last_index != -1 and i - last_index > 1:
                return False
            last_index = i

    return all(store_progress) and (len(subset) == len(used_strings))

    
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
    
print(n)

