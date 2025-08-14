def print_fibonacci(n):
    if n <= 0:
        print([])
        return
    elif n == 1:
        print([0])
        return
    elif n == 2:
        print([0, 1])
        return
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    print(fib_sequence)
if __name__ == "__main__":
    print_fibonacci(9)
