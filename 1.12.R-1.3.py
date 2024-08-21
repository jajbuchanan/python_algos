# Write a short Python function, minmax(data), that
# takes a sequence of one or more numbers, and returns
# the smallest and largest numbers, in the form of a tuple
# of length two. Do not use the built-in functions min or
# max in implementing your solution


def minmax(data):
    min_val = max_val = data[0]
    for x in data[1:]:
        if x < min_val:
            min_val = x
        elif x > max_val:
            max_val = x

    return min_val, max_val


test_nos = [1, 2, -3, 5, -6, 8, 32, 4, 2, 5, 34, 55, 21]


def main():
    print(f"Output is: {minmax(test_nos)}")


if __name__ == "__main__":
    main()
