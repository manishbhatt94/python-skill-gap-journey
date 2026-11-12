def valid_records(records):
    """Generator function that takes in an iterable of dicts, and yields only
    the valid ones.

    A record is considered valid if:
    1. It is a dictionary.
    2. It contains an id key whose value is a non-empty string.
    3. It contains a type key whose value is a non-empty string.
    4. Neither id nor type is empty or consists entirely of whitespace.
    """

    def validate_record_key(record, key, /):
        value = record.get(key)
        return isinstance(value, str) and bool(value.strip())

    for record in records:
        if not isinstance(record, dict):
            continue
        keys = ("id", "type")
        if all(validate_record_key(record, key) for key in keys):
            yield record


def test(records):
    result = valid_records(records)

    print("Generator created!")

    print(type(result).__name__)
    # Expected: generator

    first = next(result)
    print("First record retrieved!")
    print(first)
    # Expected: {"id": "evt-001", "type": "login"}

    print(list(result))
    # Expected: Remaining three valid records

    print(list(result))
    # Expected: []


if __name__ == "__main__":
    records = [
        {"id": "evt-001", "type": "login"},
        {"id": "evt-002", "type": "purchase"},
        {"id": "evt-003", "type": " "},
        {"type": "logout"},
        None,
        "not a dictionary",
        {"id": "evt-004", "type": "logout"},
        {"id": "evt-005", "type": " login "},
    ]
    test(records)
