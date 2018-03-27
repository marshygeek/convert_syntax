from re import sub
import os

from strip_hints import strip_file_to_string


def process_file(filename):
    source = strip_file_to_string(filename)
    source = sub(r"yield[\\ \n]+from", "yield ", source)

    with open(filename, "w") as out:
        out.write(source)


def check_path(path):
    if os.path.isfile(path):
        print(path)
        process_file(path)
        return

    for filename in os.listdir(path):
        path_to_file = os.path.join(path, filename)
        print(path_to_file)
        if os.path.isfile(path_to_file):
            process_file(path_to_file)
        elif os.path.isdir(path_to_file):
            check_path(path_to_file)


if __name__ == "__main__":
    path = input("Type in the path to a file or directory: ")
    check_path(path)
