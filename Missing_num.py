nums = [1, 2, 3, 4, 6, 7, 8]

n = 8  # expected range 1 → 8
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

missing = expected_sum - actual_sum

print("Missing number:", missing)
