def is_even(number):
    return number % 2 == 0


def number_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


def is_armstrong(number):
    total = 0
    temp = abs(number)
    digits = len(str(temp))

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == abs(number)


def main():
    num = int(input("Enter a number: "))

    print("\n===== Analysis Result =====")

    if is_even(num):
        print("Even/Odd :", "Even")
    else:
        print("Even/Odd :", "Odd")

    print("Sign     :", number_sign(num))

    if is_armstrong(num):
        print("Armstrong:", "Yes")
    else:
        print("Armstrong:", "No")


main()
