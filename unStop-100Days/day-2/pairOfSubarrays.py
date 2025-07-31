from collections import defaultdict

# Your existing subarray generator
def subArrays(n: list) -> list:
    return [n[i:j+1] for i in range(len(n)) for j in range(i, len(n))]

# Main logic
def pairOfSubarrays(numbers: list) -> int:
    subCounter = defaultdict(list)

    # Need to re-generate indices for overlap checks
    res = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            sub = numbers[i:j+1]
            res.append(sub)
            subCounter[sum(sub)].append((i, j))  # Store indices
        
    print(res)
    print(subCounter)

    total_pairs = 0

    for k, v in subCounter.items():
        # print(f"{k}: {v} : {len(v)}")
        for va in range(len(v)):
            L1, R1 = v[va]
            for ka in range(va):
                L2, R2 = v[ka]
                if R1 < L2 or R2 < L1:
                    total_pairs += 1
                    # print(f"Non-overlapping pair found: {v[ka]} and {v[va]}")

    return None

# Test case
print(pairOfSubarrays([1, -1, 2, -2]))  # Should output: 2
print(subArrays([1,-1,2,-2]))