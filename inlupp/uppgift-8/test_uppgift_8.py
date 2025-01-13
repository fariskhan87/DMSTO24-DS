def count_letters(string):
    letter_counts = {}
    for char in string:
        if char.isalpha():
            char = char.lower()
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts

def main():
    string = "Hello World!"
    letter_counts = count_letters(string)
    print(letter_counts) 


if __name__ == "__main__":
    main()


