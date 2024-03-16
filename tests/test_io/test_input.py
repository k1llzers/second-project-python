import pytest

import app.io.input as input


EXPECTED_READ_VALUE_FROM_TXT_FILE = "Hello everyone"
EXPECTED_READ_VALUE_FROM_CSV_FILE = "TEST First\ntest good\nmark 10"
TXT_FILE_PATH = "tests/data/input_for_test.txt"
CSV_FILE_PATH = "tests/data/input_for_test.csv"
NON_EXISTENT_FILE_PATH = "aaa/daaa.txt"


def test_read_text_from_file_simple():
    actual_value = input.read_text_from_file_simple(TXT_FILE_PATH)
    assert EXPECTED_READ_VALUE_FROM_TXT_FILE == actual_value


def test_read_text_from_file_simple_raise_exception():
    with pytest.raises(FileNotFoundError):
        input.read_text_from_file_simple(NON_EXISTENT_FILE_PATH)


def test_read_text_from_file_simple_csv_file():
    actual_value = input.read_text_from_file_simple(CSV_FILE_PATH)
    assert EXPECTED_READ_VALUE_FROM_CSV_FILE == actual_value
