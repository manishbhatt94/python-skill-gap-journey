import json


def read_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):  # noqa: UP028
            yield line_number, line


def parse_json_lines(lines, stats):
    for line_number, line in lines:
        stats["total_lines"] += 1

        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            stats["malformed_json_lines"] += 1
            print(f"Skipping malformed JSON on line {line_number}: {exc.msg}")
            continue

        yield line_number, record


def is_valid_record(record):
    if not isinstance(record, dict):
        return False

    required_keys = ("id", "type")

    return all(
        isinstance(record.get(key), str) and bool(record[key].strip())
        for key in required_keys
    )


def valid_records(records, stats):
    for line_number, record in records:
        if not is_valid_record(record):
            stats["invalid_records"] += 1
            print(f"Skipping invalid record on line {line_number}")
            continue

        stats["valid_records"] += 1
        yield line_number, record


def normalize_records(records):
    for line_number, record in records:
        normalized_record = record.copy()
        normalized_record["type"] = normalized_record["type"].strip().lower()

        yield line_number, normalized_record


def select_records(records, *, event_type):
    for line_number, record in records:
        if record["type"] == event_type:
            yield line_number, record


def generate_summary(records, stats, *, event_type):
    selected_event_ids = []

    for _, record in records:
        selected_event_ids.append(record["id"])

    return {
        **stats,
        "selected_event_type": event_type,
        "selected_event_count": len(selected_event_ids),
        "selected_event_ids": selected_event_ids,
    }


def process_events(path, *, event_type):
    stats = {
        "total_lines": 0,
        "malformed_json_lines": 0,
        "invalid_records": 0,
        "valid_records": 0,
    }

    pipeline = select_records(
        normalize_records(
            valid_records(
                parse_json_lines(read_lines(path), stats),
                stats,
            ),
        ),
        event_type=event_type,
    )

    return generate_summary(pipeline, stats, event_type=event_type)


if __name__ == "__main__":
    summary = process_events(
        "data/events.ndjson",
        event_type="logout",  # Or: event_type="login",
    )

    print(summary)
