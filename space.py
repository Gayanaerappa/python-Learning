text = input("Enter a string: ")

result = ""

for ch in text:
    if ch != " ":
        result += ch

print("Without spaces:", result)
