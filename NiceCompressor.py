import sys
import os
import zipfile


def main():
    if len(sys.argv) < 3:
        print('usage: arg1 - dict file, arg2 - dir name')

    filename = sys.argv[1]
    directory = sys.argv[2]
    with open(filename, 'r', encoding='utf-8') as f:
        dict_list = list(filter(None, f.read().split()))

    with zipfile.ZipFile(f'{dict_list[-1]}.zip', 'x') as f:
        f.write(directory)
        os.remove(directory)
        directory = dict_list.pop()

    while len(dict_list) > 0:
        with zipfile.ZipFile(f'{dict_list[-1]}.zip', 'x') as z:
            z.write(f'{directory}.zip')
        os.remove(f'{directory}.zip')
        directory = dict_list.pop()


if __name__ == "__main__":
    main()