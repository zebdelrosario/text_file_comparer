"""Program that compares two different .txt files and performs actions  based on user input.
Developer: Zeb del Rosario
Creation Start: 24/06/2022
"""


def main():
    """Main code block."""
    FILE_ONE = "file1.txt"
    FILE_TWO = "file2.txt"
    lines_one = get_lines(FILE_ONE)
    lines_two = get_lines(FILE_TWO)
    dict = compare_lines(lines_one, lines_two)
    # test_compare_lines(lines_one, lines_two)
    display_values(dict, "list_one_unique", "list_two_unique", "identical_values")


def display_values(dict, unique_key1, unique_key2, identical_key):
    """Display the values of provided keys neatly."""
    print(f"""
    ====UNIQUE VALUES====

    LIST ONE
    ->\t{[item for item in dict[unique_key1]]}

    LIST TWO
    ->\t{[item for item in dict[unique_key2]]}

    {"=" * 21}

    ====IDENTICAL VALUES====

    ->\t{[item for item in dict[identical_key]]}

    {"=" * 21}
    """)


def test_get_lines(file_path, file_name):
    """Test the function"""
    lines = get_lines(file_path)
    print(f"""
    TESTING FUNCTION:\tget_lines
    FILE NAME:\t\t{file_name}
    RESULT:
    {lines}
    """)


def get_lines(file_path):
    """Returns content provided in parameter."""
    with open(file_path, 'r') as in_file:
        lines = [line.strip("\n") for line in in_file]
    return lines


def test_compare_lines(lines_one, lines_two):
    """Test the function"""
    dict = compare_lines(lines_one, lines_two)
    print(f"""
    TESTING FUNCTION:\t'compare_lines'
    RESULT:
    {dict}
    """)


def compare_lines(lines_one, lines_two):
    """Compares two lists of lines and returns a dictionary of identical and unique values."""
    dict = {"list_one_unique": [], "list_two_unique": [], "identical_values": []}
    for line in lines_one:
        if line in lines_two:
            dict["identical_values"].append(line)
        elif line not in lines_two:
            dict["list_one_unique"].append(line)
    for line in lines_two:
        if line not in lines_one:
            dict["list_two_unique"].append(line)
    return dict


if __name__ == '__main__':
    main()