import json
import tempfile
import unittest
from pathlib import Path

from event_processor import is_valid_record, process_events


class TestIsValidRecord(unittest.TestCase):
    def test_valid_record(self):
        record = {
            "id": "evt-001",
            "type": "login",
            "user_id": 12,
        }

        self.assertTrue(is_valid_record(record))

    def test_record_with_missing_id(self):
        record = {"type": "login"}

        self.assertFalse(is_valid_record(record))

    def test_record_with_blank_type(self):
        record = {"id": "evt-001", "type": "   "}

        self.assertFalse(is_valid_record(record))

    def test_record_with_non_string_id(self):
        record = {"id": 123, "type": "login"}

        self.assertFalse(is_valid_record(record))

    def test_non_dictionary_record(self):
        self.assertFalse(is_valid_record(None))


class TestProcessEvents(unittest.TestCase):
    def test_process_login_events(self):
        input_lines = [
            {"id": "evt-001", "type": " LOGIN "},
            {"id": "evt-002", "type": "purchase"},
            {"id": "evt-003", "type": "login"},
            {"id": "evt-004", "type": "  "},
            {"type": "login"},
            {"id": "evt-005", "type": "logout"},
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "events.ndjson"

            with file_path.open("w", encoding="utf-8") as file:
                for record in input_lines:
                    file.write(json.dumps(record) + "\n")

            summary = process_events(file_path, event_type="login")

        self.assertEqual(summary["total_lines"], 6)
        self.assertEqual(summary["malformed_json_lines"], 0)
        self.assertEqual(summary["invalid_records"], 2)
        self.assertEqual(summary["valid_records"], 4)
        self.assertEqual(summary["selected_event_type"], "login")
        self.assertEqual(summary["selected_event_count"], 2)
        self.assertEqual(
            summary["selected_event_ids"],
            ["evt-001", "evt-003"],
        )


if __name__ == "__main__":
    unittest.main()
