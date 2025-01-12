
def max_in_list(numbers):
    max = numbers[0]
    for num in numbers:
      if num > max:
        max = num
    return max  

# Example usage
def main():
    # Test cases
    test_numbers = [100, 5, 10, 7, 22,11, 20]
    print(f"maximum in the selected range is: {max(test_numbers)}")   

if __name__ == "__main__":
    main()