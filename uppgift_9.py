def is_palindrome(string):
    cleaned_string = ""
    for char in string:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
            cleaned_string += char.lower()
    reversed_string = ""
    for char in cleaned_string:
        reversed_string = char + reversed_string
    return cleaned_string == reversed_string

def main():
    string = "A man, a plan, a canal, Panama"
    print(is_palindrome(string))
    string = "Hello"
    print(is_palindrome(string))


if __name__ == "__main__":
    main()
