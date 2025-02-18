### A Python-based solution for generating valid discount codes under specific constraints.

## 📝 Problem Statement

Given a binary string `T` (composed of 0s and 1s), determine:
1. The number of distinct sets of codes `X` that satisfy predefined conditions.
2. The total number of valid mappings from `T` to the codes in `X`.

### Input
- A binary string `T`.

### Output
Two integers:
1. Number of valid code sets `X`.
2. Total distinct mappings for all valid `X`.

## 🔍 Conditions for Valid Codes (`X`)
1. **Uniqueness**: No duplicate codes allowed.
2. **Binary Format**: Codes must only contain `0`/`1`.
3. **Length Limit**: Each code ≤ 3 digits.
4. **No Prefixes**: No code can be a prefix of another.
5. **Mapping**: Each code must map to a unique English letter in a string `S`.

## 🛠️ Solution Overview
1. **Generate Valid Code Sets**: Identify all code sets `X` that satisfy conditions 1-4.
2. **Validate Mappings**: Check if `T` can be converted to `X` while respecting all conditions.
3. **Calculate Mappings**: Compute the total distinct mappings for valid code sets.
