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


# Test Code:

stats = {
    "total_lines": 0,
    "malformed_json_lines": 0,
}

for line_number, record in parse_json_lines(read_lines("data/events.ndjson"), stats):
    print(line_number, repr(record))

print(stats)
