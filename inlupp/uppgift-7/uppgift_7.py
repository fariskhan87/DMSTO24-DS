def validate_password(password):
    if len(password) < 8:
        return False
    for char in password:
        if char.isdigit():
            return True
    return False

def main():
    password = "password123"
    print(validate_password(password))
    password = "short"
    print(validate_password(password))


if __name__ == "__main__":
    main()
