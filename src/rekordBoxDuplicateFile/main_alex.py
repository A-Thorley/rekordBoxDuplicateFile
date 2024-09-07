import filecmp
import os


def get_duplicates(path):
    """
    Prints duplicate files from a directory
    :param path: path to directory
    :return: None
    """
    assert os.path.isdir(path), "Path is not a directory"

    files = os.listdir(path)

    duplicates = []

    for file_1 in files:
        for file_2 in files:
            if file_1 != file_2 and filecmp.cmp(os.path.join(path, file_1), os.path.join(path, file_2)) and file_1 not in duplicates:
                duplicates.append(file_2)

    print(duplicates)


if __name__ == "__main__":
    target_folder = "C:\\Users\\leoca\\Music\\320kbps"

    get_duplicates(target_folder)