def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [[int(n) for n in entry.split(',')] for entry in f.readlines()][0]
        return entries


def program_1(data):
    return(data)


def main():
    data = open_file("input.txt")
    print(program_1(data))


if __name__ == '__main__':
    main()
