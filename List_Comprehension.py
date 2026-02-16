n = int(input("How many numbers? "))

numbers = [int(input("Enter number: ")) for _ in range(n)]

even_count = len([x for x in numbers if x % 2 == 0])
odd_count = len([x for x in numbers if x % 2 != 0])

largest = max(numbers)
smallest = min(numbers)

print("\n--- Analysis Result ---")
print("Numbers Entered:", numbers)
print("Even Count:", even_count)
print("Odd Count:", odd_count)
print("Largest Number:", largest)
print("Smallest Number:", smallest)
