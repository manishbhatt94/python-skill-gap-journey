def square(n):
    print(f"Calculating square of {n}")
    return n * n


def test():
    numbers = [1, 2, 3, 4]

    print("--- Eager evaluation ---")

    eager = [square(n) for n in numbers]

    print("Eager collection created!")
    print(eager)

    print("\n--- Lazy evaluation ---")

    lazy = (square(n) for n in numbers)

    print("Lazy generator created!")

    first = next(lazy)
    print("First value:", first)

    remaining = list(lazy)
    print("Remaining values:", remaining)

    print("Trying to consume again:")
    print(list(lazy))

    print(type(eager))  # <class 'list'>
    print(type(lazy))  # <class 'generator'>


if __name__ == "__main__":
    test()
