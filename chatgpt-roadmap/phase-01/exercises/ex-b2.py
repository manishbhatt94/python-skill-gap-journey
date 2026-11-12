def collect_errors(message, errors=[]):
    errors.append(message)
    return errors


def collect_errors2(message, errors=None):
    if errors is None:
        errors = []
    errors.append(message)
    return errors


def test_bad_code():
    # Prints: ['Hello.', 'Who is this?']
    print(collect_errors("Who is this?", ["Hello."]))

    # Prints: ['I need a pastry.', 'The pineapple one!', "It'll be 50 rupees."]
    print(
        collect_errors(
            "It'll be 50 rupees.", ["I need a pastry.", "The pineapple one!"]
        )
    )

    # Prints: ['Give me the loot!']
    print(collect_errors("Give me the loot!"))

    # Prints: ['Give me the loot!', 'Ghetto Bird']
    print(collect_errors("Ghetto Bird"))

    # Prints: ['Give me the loot!', 'Ghetto Bird', 'The Real Slim Shady']
    print(collect_errors("The Real Slim Shady"))

    # Prints: ['Notorious Thugs']
    print(collect_errors("Notorious Thugs", []))

    # Prints: ['Dead Wrong']
    print(collect_errors("Dead Wrong", []))


def test_good_code():
    # Prints: ['Hello.', 'Who is this?']
    print(collect_errors2("Who is this?", ["Hello."]))

    # Prints: ['I need a pastry.', 'The pineapple one!', "It'll be 50 rupees."]
    print(
        collect_errors2(
            "It'll be 50 rupees.", ["I need a pastry.", "The pineapple one!"]
        )
    )

    # Prints: ['Give me the loot!']
    print(collect_errors2("Give me the loot!"))

    # Prints: ['Ghetto Bird']
    print(collect_errors2("Ghetto Bird"))

    # Prints: ['The Real Slim Shady']
    print(collect_errors2("The Real Slim Shady"))

    # Prints: ['Notorious Thugs']
    print(collect_errors2("Notorious Thugs", []))

    # Prints: ['Dead Wrong']
    print(collect_errors2("Dead Wrong", []))


def main():
    print("\n --- Testing bad code ---\n")
    test_bad_code()
    print()
    print("\n --- Testing good code ---\n")
    test_good_code()


if __name__ == "__main__":
    main()
