# Program to print the average of n numbers

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

n = int(input("Enter the value of n: "))

numbers = []
for i in range(n):
    num = float(input("Enter number {}: ".format(i+1)))
    numbers.append(num)

average = calculate_average(numbers)
print("The average of the {} numbers is: {}".format(n, average))
