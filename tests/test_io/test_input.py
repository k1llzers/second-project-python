import app.io.input as input


EXPECTED_READ_VALUE_FROM_TXT_FILE = "Hello everyone"
TXT_FILE_PATH = "tests/data/input_for_test.txt"


def test_read_text_from_file_simple():
    actual_value = input.read_text_from_file_simple(TXT_FILE_PATH)
    assert EXPECTED_READ_VALUE_FROM_TXT_FILE == actual_value