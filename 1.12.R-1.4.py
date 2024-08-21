# Write a short python function that takes a positive integer n and
# returns the sum of the squares of all of the positive integers
# smaller than n


def sum_of_odd_squares(n):
    squares = []
    for x in range(0, n):
        if (x & 1) != 0:
            squares.append(x * x)
    print(f"squares: {squares}")
    return squares


test_numbers = [1, 3, 5, 20, 15, 26]


def main():
    for x in test_numbers:
        sum_of_odd_squares(x)


if __name__ == "__main__":
    main()
