import pandas as pd
import pytest

import app.io.input as input


STRING_EXPECTED_READ_VALUE_FROM_TXT_FILE = "Hello everyone"
STRING_EXPECTED_READ_VALUE_FROM_CSV_FILE = "TEST First\ntest good\nmark 10"
TXT_FILE_PATH = "tests/data/input_for_test.txt"
CSV_FILE_PATH = "tests/data/input_for_test.csv"
NON_EXISTENT_FILE_PATH = "aaa/daaa.txt"


def test_read_text_from_simple_file():
    actual_value = input.read_text_from_file_simple(TXT_FILE_PATH)
    assert STRING_EXPECTED_READ_VALUE_FROM_TXT_FILE == actual_value


def test_read_text_from_file_simple_raise_exception():
    with pytest.raises(FileNotFoundError):
        input.read_text_from_file_simple(NON_EXISTENT_FILE_PATH)


def test_read_text_simple_from_csv_file():
    actual_value = input.read_text_from_file_simple(CSV_FILE_PATH)
    assert STRING_EXPECTED_READ_VALUE_FROM_CSV_FILE == actual_value


def test_read_text_from_csv_file():
    actual_value = input.read_text_from_csv_file(CSV_FILE_PATH)
    expected_value = pd.DataFrame(["test good", "mark 10"], columns=["TEST First"])
    pd.testing.assert_frame_equal(expected_value, actual_value)


def test_read_text_from_csv_file_raise_exception():
    with pytest.raises(FileNotFoundError):
        input.read_text_from_csv_file(NON_EXISTENT_FILE_PATH)


def test_read_text_from_csv_file_from_txt():
    actual_value = input.read_text_from_csv_file(TXT_FILE_PATH)
    expected_value = pd.DataFrame(columns=["Hello everyone"])
    pd.testing.assert_frame_equal(expected_value, actual_value)
