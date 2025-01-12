def word_count(text):
    if isinstance(text, str):
        return len(text.split())
    return 0

def main():
    print("Testar word_count:")
    print(word_count("Hello world"))
    print(word_count(""))
    print(word_count(123)) 


if __name__ == "__main__":
    main()
