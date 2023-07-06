# Program to print the sum digits.

def calculate_sum_of_digits(num):

    num_str = str(num)

    digit_sum = 0

    for digit in num_str:
        digit_sum += int(digit)

    return digit_sum

num = int(input("Enter a number: "))

digit_sum = calculate_sum_of_digits(num)
print("The sum of digits in the number", num, "is:", digit_sum)
