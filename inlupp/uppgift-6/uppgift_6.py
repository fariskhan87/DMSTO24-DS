def multiplication_table(n, limit):
    result = []
    for i in range(1, limit + 1):
        result.append(n * i)
    return result

def main():
    n = 15
    limit = 10
    multiplication_result = multiplication_table(n, limit)
    print(multiplication_result)


if __name__ == "__main__":
    main()
