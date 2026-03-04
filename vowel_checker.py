# Vowel Checker Program

letter = input("Enter a letter: ")

if len(letter) == 1:
    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("It is a Vowel ✅")
    else:
        print("It is a Consonant ❌")
else:
    print("Please enter only one letter.")
