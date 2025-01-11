
def sum_list(numbers):
    sum = 0
    for num in numbers:
      sum = sum + num
    return sum  

# Example usage
def main():
    # Test cases
    test_numbers = [0, 5, 10, 7, 22,11, 20]
    print(f"sum of the selected range is: {sum(test_numbers)}")

    print(f"sum from 1 to 100 is: {sum(range(1, 100))}")
    
    
if __name__ == "__main__":
    main()