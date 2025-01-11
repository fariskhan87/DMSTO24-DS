
def is_odd(number):
    return number % 2 != 0

# Example usage
def main():
    # Test cases
    test_numbers = [0, 1, 2, 3, 4, 5, 10, 15, 20]

    print("Checking if numbers are odd:")
    for i in range(1,100):
        print(f"{i} is odd: {is_odd(i)}")
    
    for num in test_numbers:
        print(f"{num} is odd: {is_odd(num)}")

if __name__ == "__main__":
    main()