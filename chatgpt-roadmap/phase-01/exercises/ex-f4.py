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


def normalize_records(records):
    """For every incoming record:
    1. Create a shallow copy of the record.
    2. Normalize its type field using .strip().lower().
    3. Yield the new dictionary.
    """
    for record in records:
        record_copy = record.copy()
        record_copy["type"] = record_copy["type"].strip().lower()
        yield record_copy


def select_records(records, *, event_type):
    """Requirements:
    - Accept an iterable of records.
    - Yield only records whose normalized type matches event_type.
    - Use exact equality (==).
    - Do not create an intermediate list.
    """
    for record in records:
        if record["type"] == event_type:
            yield record


def events_pipeline(raw_records):
    pipeline = select_records(
        normalize_records(valid_records(raw_records)),
        event_type="login",
    )
    result = list(pipeline)
    print(result)


def test_types_generator_functions(raw_records):
    validated = valid_records(raw_records)
    print("validated:", validated)  # <generator object valid_records at 0x..>
    print("type(validated):", type(validated))  # <class 'generator'>

    normalized = normalize_records(valid_records(raw_records))
    print("normalized:", normalized)  # <generator object normalize_records at 0x..>
    print("type(normalized):", type(normalized))  # <class 'generator'>

    selected = select_records(
        normalize_records(valid_records(raw_records)),
        event_type="login",
    )
    print("selected:", selected)  # <generator object select_records at 0x..>
    print("type(selected):", type(selected))  # <class 'generator'>


def test_shallow_copy(raw_records):
    normalized = list(normalize_records(valid_records(raw_records)))
    print(normalized[0] is raw_records[0])
    print(normalized[0]["metadata"] is raw_records[0]["metadata"])


if __name__ == "__main__":
    raw_records = [
        {
            "id": "evt-001",
            "type": " LOGIN ",
            "user_id": 12,
            "metadata": {"source": "web"},
        },
        {
            "id": "evt-002",
            "type": "purchase",
            "user_id": 12,
            "metadata": {"source": "app"},
        },
        {
            "id": "evt-003",
            "type": "login",
            "user_id": 27,
            "metadata": {"source": "web"},
        },
        {
            "id": "evt-004",
            "type": "  ",
            "user_id": 30,
            "metadata": {"source": "web"},
        },
        {
            "type": "login",
            "user_id": 35,
        },
        None,
        {
            "id": "evt-005",
            "type": " LOGOUT ",
            "user_id": 12,
            "metadata": {"source": "mobile"},
        },
        {
            "id": "evt-006",
            "type": "login",
            "user_id": 45,
            "metadata": {"source": "mobile"},
        },
    ]
    events_pipeline(raw_records)
    test_types_generator_functions(raw_records)
    test_shallow_copy(raw_records)
