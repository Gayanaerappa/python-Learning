nums = [0, 1, 0, 3, 12]

result = []

for n in nums:
    if n != 0:
        result.append(n)

for n in nums:
    if n == 0:
        result.append(n)

print(result)
