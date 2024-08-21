import timeit


def is_even_1(k):
    input_number = k
    while input_number != 0:
        input_number -= 1
        if input_number == 0:
            return False
        input_number -= 1
        if input_number == 0:
            return True


def is_even_bitwise(k):
    return (k & 1) == 0


test_cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1324]


def main():
    print("Testing with is_even_1")
    execution_time = timeit.timeit("is_even_1(1234)", globals=globals(), number=1000000)
    print(f"Execution time for is_even(1234): {execution_time} seconds.")
    for x in test_cases:
        print(f"Testing {x}: {is_even_1(x)}")
    print("Testing with is_even_bitwise")
    execution_time_bitwise = timeit.timeit(
        "is_even_bitwise(1234)", globals=globals(), number=1000000
    )
    print(
        f"Execution time for is_even_bitwise(1234): {execution_time_bitwise} seconds."
    )
    for x in test_cases:
        print(f"Testing {x}: {is_even_bitwise(x)}")


if __name__ == "__main__":
    main()
