students = [78, 35, 90, 40, 22, 65]

pass_count = 0
fail_count = 0

for m in students:
    if m >= 40:
        pass_count += 1
    else:
        fail_count += 1

print("Pass:", pass_count)
print("Fail:", fail_count)
