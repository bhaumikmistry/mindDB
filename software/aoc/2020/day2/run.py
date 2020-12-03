# --- Day 2: Report Repair --- #


def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [entry for entry in f.readlines()]
        return entries


class policy:
    def __init__(self, entry):
        self.entry = entry
        self.min_range = int()
        self.max_range = int()
        self.rule = str()
        self.data = str()
        self.parse()

    def parse(self):
        list_data = self.entry.split()
        range = list_data[0].split("-")
        self.min_range = int(range[0])
        self.max_range = int(range[1])
        self.rule = list_data[1].split(":")[0]
        self.data = list_data[2]


def program_1(data):
    valid_password = 0
    for password in data:
        info = policy(password)
        valid_password = valid_password + (1 if info.min_range <= info.data.count(info.rule) <= info.max_range else 0)
    return valid_password


def program_2(data):
    valid_password = 0
    for password in data:
        info = policy(password)
        if list(info.data)[info.min_range-1] == info.rule and not list(info.data)[info.max_range-1] == info.rule:
            valid_password += 1
        elif not list(info.data)[info.min_range-1] == info.rule and list(info.data)[info.max_range-1] == info.rule:
            valid_password += 1
    return valid_password


def main():
    data = open_file("input.txt")
    print(program_1(data))
    print(program_2(data))


if __name__ == '__main__':
    main()
