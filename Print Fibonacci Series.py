# Print Fibonacci Series


def fibonacci(n):
    series = []
    a, b = 0, 1

    series.append(a)
    series.append(b)

    for i in range(2, n):
        c = a + b
        series.append(c)
        a, b = b, c

    return series


num = int(input("Enter the number of terms in the Fibonacci series: "))

if num <= 0:
    print("Number of terms should be a positive integer.")
else:
    result = fibonacci(num)
    print("The Fibonacci series is:", result)
