def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def main():
    celsius = 0
    print(celsius_to_fahrenheit(celsius))  # Output: 32.0
    celsius = 100
    print(celsius_to_fahrenheit(celsius))


if __name__ == "__main__":
    main()
