def minimal_difference(n, weights):
    total_weight = sum(weights)
    min_diff = float('inf')
    
    # Iterate through all subsets using bitmasking
    for mask in range(1 << n):  # 2^n subsets
        subset_sum = sum(weights[i] for i in range(n) if mask & (1 << i))
        complement_sum = total_weight - subset_sum
        min_diff = min(min_diff, abs(subset_sum - complement_sum))
    
    print(min_diff)

# Read input
n = int(input())
weights = list(map(int, input().split()))
minimal_difference(n, weights)