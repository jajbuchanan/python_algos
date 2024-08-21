def is_multiple(n, m):
    if m % n == 0:
        return True
    else:
        return False


test_cases = [[1, 2], [5, 25], [13, 22]]


def main():
    for a, b in test_cases:
        print(f"Testing a: {a} and b: {b}")
        print(f"Result of is_multiple: {is_multiple(a,b)}")


if __name__ == "__main__":
    main()
