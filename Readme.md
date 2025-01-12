# DMSTO24-DS

This repository contains assignments and solutions for the **DMSTO24 Data Structures course**. Each assignment file (`uppgift`) is accompanied by a corresponding test file located in the `tests` directory to ensure correctness and validate the implementation.

## Repository Structure

### Branch: `upifgth01`

The branch is organized as follows:

```
DMSTO24-DS/
├── uppgift_1.py
├── uppgift_2.py
├── uppgift_3.py
├── uppgift_4.py
├── uppgift_5.py
├── uppgift_6.py
├── uppgift_7.py
├── uppgift_8.py
├── uppgift_9.py
├── uppgift_10.py
├── uppgift_11.py
├── uppgift_12.py
├── tests/
│   ├── test_uppgift_1.py
│   ├── test_uppgift_2.py
│   ├── test_uppgift_3.py
│   ├── test_uppgift_4.py
│   ├── test_uppgift_5.py
│   ├── test_uppgift_6.py
│   ├── test_uppgift_7.py
│   ├── test_uppgift_8.py
│   ├── test_uppgift_9.py
│   ├── test_uppgift_10.py
│   ├── test_uppgift_11.py
│   ├── test_uppgift_12.py
└── README.md
```

### Assignment Files and Descriptions

1. **`uppgift1.py`**
   - *Description:* The file uppgift_1.py defines a function named is_odd that determines whether a given integer is odd. The function takes an integer as input and returns True if the number is odd (i.e., not divisible by 2) and False otherwise.

2. **`uppgift2.py`**
   - *Description:* Implements a method sum_list, which takes a list of numbers and returns the sum of all the elements in the list. Additionally, the file demonstrates the function's usage by calculating the sum of predefined lists and a range of numbers.

3. **`uppgift3.py`**
   - *Description:* Defines a function is_prime that checks if a given number is a prime number. The script includes a main function that tests this functionality with various numbers.

4. **`uppgift4.py`**
   - *Description:* Contains a function factorial that computes the factorial of a non-negative integer. The main function demonstrates this by calculating the factorial of sample numbers.

5. **`uppgift5.py`**
   - *Description:* Implements a function fibonacci that returns the nth Fibonacci number. The script's main function showcases this by computing Fibonacci numbers for given indices.

6. **`uppgift6.py`**
   - *Description:* Provides a function reverse_string that reverses a given string. The main function tests this by reversing sample strings.

7. **`uppgift7.py`**
   - *Description:* Defines a function validate_password that checks if a password meets certain criteria: at least 8 characters long and contains at least one digit. The main function tests this validation with example passwords.
8. **`uppgift8.py`**
   - *Description:* Contains a function count_vowels that counts the number of vowels in a given string. The main function demonstrates this by counting vowels in sample strings.

9. **`uppgift9.py`**
   - *Description:* Implements a function palindrome_check that determines whether a given string is a palindrome. The main function tests this with various sample strings.

10. **`uppgift10.py`**
    - *Description:* Provides a function celsius_to_fahrenheit that converts a temperature from Celsius to Fahrenheit. The main function demonstrates this conversion with sample temperatures.

11. **`uppgift11.py`**
    - *Description:* Defines a function word_count that counts the number of words in a given string. The main function tests this functionality with sample sentences.

12. **`uppgift12.py`**
    - *Description:* Contains a function create_student_register that takes a list of student names and ages, and returns a dictionary mapping names to ages. The main function demonstrates this by creating a sample student register.

### Test Files

Each assignment has a corresponding test file located in the `tests` directory:

- **`tests/test_uppgift1.py`** to **`tests/test_uppgift12.py`**
  - *Description:* Contains unit tests for the respective assignment file, covering various cases to ensure the correctness and robustness of the implementations.

## How to Use

### Clone the Repository

```bash
git clone -b upifgth01 https://github.com/fariskhan87/DMSTO24-DS.git
cd DMSTO24-DS
```

### Run the Tests

Ensure you have Python installed along with `pytest`. To run the tests:

```bash
pip install pytest
pytest
```

This will execute all test files in the `tests` directory and display the results.

## Contribution Guidelines

1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request to the `upifgth01` branch with a detailed description of the changes.
