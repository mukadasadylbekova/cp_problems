def find_digit(k):
    length = 1  # Length of the numbers in this range (1-digit, 2-digit, ...)
    count = 9   # How many numbers exist in this range
    start = 1   # First number in this range
    
    while k > length * count:
        k -= length * count  # Skip the whole range
        length += 1  # Move to next digit group
        count *= 10  # Numbers grow by a factor of 10
        start *= 10  # Update first number in this range
    
    # Find the exact number where k-th digit is located
    number = start + (k - 1) // length
    digit_index = (k - 1) % length
    return str(number)[digit_index]

# Read input
q = int(input())
queries = [int(input()) for _ in range(q)]

# Process and print results
for k in queries:
    print(find_digit(k))
