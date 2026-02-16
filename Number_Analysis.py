numbers = []

print("Enter numbers (type 0 to stop):")

while True:
    num = int(input("Enter number: "))
    
    if num == 0:
        break
    
    numbers.append(num)

even = odd = 0
largest = smallest = numbers[0]

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

    if n > largest:
        largest = n

    if n < smallest:
        smallest = n

print("\n--- Analysis Result ---")
print("Numbers Entered:", numbers)
print("Even Count:", even)
print("Odd Count:", odd)
print("Largest Number:", largest)
print("Smallest Number:", smallest)
