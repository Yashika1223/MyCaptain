def fib(limit):
    fib_sequence = [0, 1]  #initializing with first 2 Fibonacci numbers

    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > limit:
            break
        fib_sequence.append(next_fib)

    return fib_sequence

#input the limit for Fibonacci numbers(till which you want to display the series)
limit = int(input("Enter the limit for Fibonacci numbers: "))

if limit < 0:
    print("Please enter a non-negative limit.")
else:
    fib_numbers = fib(limit)
    print("Fibonacci numbers up to", limit, "are:", fib_numbers)
