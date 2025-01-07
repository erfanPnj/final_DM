T = input() # Binary String T


# Create all possible code candidates (1, 2 or 3 digit)
def generate_candidates(T):
    candidates = set()
    n = len(T)
    for i in range(n):
        for length in range(1, 4):  # Lengths 1, 2, and 3
            if i + length <= n:
                candidates.add(T[i:i + length])
    return candidates

candidate_codes = generate_candidates(T)

# print("candidate codes")
# print(candidate_codes)


# Check if one code is a prefix for another code
# def is_prefix(codes):
#     for code in codes:
#         for other in codes:
#             if code != other and other.startswith(code):
#                 return True
#     return False


def is_prefix(codes):
    sorted_codes = sorted(codes)
    for i in range(len(sorted_codes) - 1):
        if sorted_codes[i + 1].startswith(sorted_codes[i]):
            return True
    return False


# Create subsets
# def valid_subsets(candidates):
#     from itertools import combinations
#     valid_subsets = []
#     candidates = list(candidates)
    
#     # Check all combinations of candidates
#     for r in range(1, len(candidates) + 1):
#         for subset in combinations(candidates, r):
#             if not is_prefix(subset):
#                 valid_subsets.append(set(subset))
#     return valid_subsets

def valid_subsets(candidates):
    from itertools import combinations
    valid_subsets = []
    candidates = list(candidates)

    for r in range(1, len(candidates) + 1):
        for subset in combinations(candidates, r):
            if not is_prefix(subset):
                valid_subsets.append(set(sorted(subset)))
    return valid_subsets


valid_subsets = valid_subsets(candidate_codes)

# print("valid subsets")
# print(valid_subsets)



# def check_transform_condition(T, subset):
#     from itertools import permutations
#     if T == "":
#         return True

#     # Flag to track if any valid transformation is found
#     transformation_possible = False

#     # Iterate through all permutations of the subset
#     for sbset_tuple in permutations(subset):
#         sbset = set(sbset_tuple)
#         for code in sbset:
#             if code in T:
#                 # Create a new subset without modifying the original
#                 if T.count(code) == 1:
#                     new_subset = sbset - {code}
#                     new_T = T.replace(code, "")
#                     if new_T == "" and len(new_subset) != 0:
#                         continue  # Skip this permutation as it's invalid
#                     # Recursively check the remaining part of T
#                     if check_transform_condition(new_T, new_subset):
#                         transformation_possible = True
#                 else:
#                     new_T = T.replace(code, "", 1)
#                     if new_T == "" and len(sbset) != 0:
#                         continue  # Skip this permutation as it's invalid
#                     # Recursively check the remaining part of T
#                     if check_transform_condition(new_T, sbset):
#                         transformation_possible = True

#     # Return only after checking all permutations
#     return transformation_possible

# def check_transform_condition(T, subset):
#     """
#     Checks if T can be constructed using all permutations of the subset.
#     """
#     from itertools import permutations

#     if T == "" and len(subset) == 0:
#         return True

#     # Iterate through all permutations of the subset
#     for sbset_tuple in permutations(subset):
#         sbset = set(sbset_tuple)  # Convert tuple to set

#         # Iterate through each code in the current permutation
#         for code in sbset:
#             if code in T:
#                 # Handle the case where the code appears only once
#                 if T.count(code) == 1:
#                     new_subset = sbset - {code}
#                     new_T = T.replace(code, "")
                    
#                     if check_transform_condition(new_T, new_subset):
#                         return True

#                 # Handle the case where the code appears multiple times
#                 else:
#                     new_T = T.replace(code, "", 1)
#                     if check_transform_condition(new_T, sbset):
#                         return True

#     return False  # Exhausted all permutations without finding a valid transformation






def check_transform_condition(T, subset):
    if T == "":
        return True
    
    for code in subset:
        if code in T:
            # Create a new subset without modifying the original
            new_subset = subset - {code}
            T = T.replace(code, "")
            if (T == "" and len(new_subset) != 0):
                return False
            # Check the remaining part of T
            if check_transform_condition(T, new_subset):
                return True
    return False
'''
def check_transform_condition(T, subset):
    if T == "":
        return True

    subset = sorted(subset)
    for code in subset:
        if code in T:
            if T.count(code) == 1:
                new_subset = [x for x in subset if x != code]
                new_T = T.replace(code, "")
                if new_T == "" and new_subset:
                    continue
                if check_transform_condition(new_T, new_subset):
                    return True
            else:
                new_T = T.replace(code, "", 1)
                if new_T == "" and subset:
                    continue
                if check_transform_condition(new_T, subset):
                    return True

    return False

'''

'''
def check_transform_condition(T, subset):
    """
    Checks if T can be reduced using the subset without recursion.
    Optimized to handle larger inputs efficiently.
    """
    from collections import deque

    # Stack/queue to hold states (remaining_T, current_subset)
    queue = deque([(T, subset)])
    visited = set()  # Memoization to track visited states

    while queue:
        current_T, current_subset = queue.popleft()

        # Check if we've reduced T completely
        if current_T == "":
            return True
# def check_transform_condition(T, subset):
#     if T == "":
#         return True

#     subset = sorted(subset)
#     for code in subset:
#         if code in T:
#             if T.count(code) == 1:
#                 new_subset = [x for x in subset if x != code]
#                 new_T = T.replace(code, "")
#                 if new_T == "" and new_subset:
#                     continue
#                 if check_transform_condition(new_T, new_subset):
#                     return True
#             else:
#                 new_T = T.replace(code, "", 1)
#                 if new_T == "" and subset:
#                     continue
#                 if check_transform_condition(new_T, subset):
#                     return True

#     return False


        # Avoid reprocessing the same state
        state = (current_T, frozenset(current_subset))
        if state in visited:
            continue
        visited.add(state)

        # Process the current subset in a fixed order (e.g., sorted)
        for code in sorted(current_subset):
            if code in current_T:
                # Case 1: Code appears once
                if current_T.count(code) == 1:
                    new_subset = current_subset - {code}
                    new_T = current_T.replace(code, "")
                    if not (new_T == "" and len(new_subset) != 0):  # Valid state
                        queue.append((new_T, new_subset))

                # Case 2: Code appears multiple times
                else:
                    new_T = current_T.replace(code, "", 1)
                    if not (new_T == "" and len(current_subset) != 0):  # Valid state
                        queue.append((new_T, current_subset))

    return False  # Exhausted all possibilities without reducing T

'''


def store_subsets_with_transform(valid_subsets, T):
    valid_subsets_with_transform = []
    for subset in valid_subsets:
        if check_transform_condition(T, subset):
            valid_subsets_with_transform.append(subset)
    return valid_subsets_with_transform

valid_with_transform = store_subsets_with_transform(valid_subsets, T)

# print("valid subsets with transform condition")
print(valid_with_transform)
        


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

# is_prefix = is_prefix({'101', '01'})
# print(is_prefix)


