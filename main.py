from app.io import input, output


def main():
    console_read = input.read_text_from_console()
    python_read = input.read_text_from_file_simple("data/input.txt")
    pandos_read = input.read_text_from_csv_file("data/input.csv")
    output.write_to_console(console_read)
    output.write_to_console(python_read)
    output.write_to_console(pandos_read)
    output.write_to_file("data/output.txt", console_read)
    output.write_to_file("data/output1.txt", python_read)
    output.write_to_csv_file("data/output_for_csv.txt", pandos_read)
    output.write_to_csv_file("data/output.csv", pandos_read)


if __name__ == '__main__':
    main()
