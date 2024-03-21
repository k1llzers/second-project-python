

def write_to_console(text):
    """
    Write text to console

    Example:
        >>> write_to_console("Hello!")

    Args:
        text (any): Text for writing to console.
    """
    print(text)


def write_to_file(path, text):
    """
    Write text to file using python methods

    Example:
        >>> write_to_file("./data/input.txt", "Hello!")

    Args:
        path (str): Path to the file to read
        text (str): Text for writing to file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    with open(path, mode="w") as file:
        file.write(text)


def write_to_csv_file(path, output_data_frame):
    """
    Write text to file using python methods

    Example:
        >>> write_to_csv_file("./data/input.txt", "Hello!")

    Args:
        path (str): Path to the file to read
        output_data_frame (DataFrame): DataFrame to write to file.

    Raises:
        FileNotFoundError: If the file does not exist.
        AttributeError: If the output_data_frame not a DataFrame.
    """
    output_data_frame.to_csv(path)
