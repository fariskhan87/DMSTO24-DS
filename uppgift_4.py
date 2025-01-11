def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_list = [0, 1]
    for i in range(2, n):
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)

    return fib_list

def main():
    n = 100
    print(f"De första {n} Fibonacci-talen är: {fibonacci(n)}")

if __name__ == "__main__":
    main()
