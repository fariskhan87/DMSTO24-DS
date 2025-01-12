def filter_odd(numbers):
    return [num for num in numbers if num % 2 == 0]

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_odd(numbers)
    print(result)

if __name__ == "__main__":
    main()
