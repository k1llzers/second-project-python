import pandas as pd


def read_text_from_console():
    """
    Read text from console input

    Returns:
        str: The text input read from the console.

    Note:
        After input text press enter.
    """
    return input("Enter your text: ")


def read_text_from_file_simple(path):
    """
    Read text from file using python methods

    Example:
        >>> read_text_from_file_simple("./data/input.txt")
        This is an example

    Args:
        path (str): Path to the file to read

    Returns:
        str: The text that read from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    with open(path, mode="r") as file:
        file_content = file.read()
        return file_content


def read_text_from_csv_file(path):
    """
    Read text from file using pandas methods

    Notes: Recomended type of fyle for using this method is csv, if you choose the other type of file, method can
    work unpredictably

    Example:
        >>> read_text_from_csv_file("./data/input.csv")
        This is an example

    Args:
        path (str): Path to the file to read

    Returns:
        DataFrame: The DataFrame read from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    file_content = pd.read_csv(path)
    return file_content.head()
