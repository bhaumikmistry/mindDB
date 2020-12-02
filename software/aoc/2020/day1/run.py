# --- Day 1: Report Repair --- #


def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [int(entry) for entry in f.readlines()]
        return entries


def program_1(data):
    for num_a in data:
        for num_b in data:
            d_diff = 2020 - num_a
            if d_diff == num_b:
                return num_a * num_b


def program_2(data):
    for num_a in data:
        for num_b in data:
            for num_c in data:
                if num_a + num_b + num_c == 2020:
                    return num_a * num_b * num_c


def main():
    data = open_file("input.txt")
    result_1 = program_1(data)
    print(result_1)
    result_2 = program_2(data)
    print(result_2)


if __name__ == '__main__':
    main()
