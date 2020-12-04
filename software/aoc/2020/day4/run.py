# --- Day 4: Passport Processing ---


def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [entry.split('\n')[0] for entry in f.readlines()]
        return entries


def validate_field(field, data):
    if field == "byr:":
        if len(data) is 4 and data.isdigit():
            if 1920 <= int(data) <= 2002:
                return True
        return False

    if field == "iyr:":
        if len(data) is 4 and data.isdigit():
            if 2010 <= int(data) <= 2020:
                return True
        return False

    if field == "eyr:":
        if len(data) is 4 and data.isdigit():
            if 2020 <= int(data) <= 2030:
                return True
        return False

    if field == "hgt:":
        if data.endswith("in"):
            if 59 <= int(data[:-2]) <= 76:
                return True
        if data.endswith("cm"):
            if 150 <= int(data[:-2]) <= 193:
                return True
        return False

    if field == "hcl:":
        if data.startswith('#'):
            for s in data[1:]:
                if s is range(0, 10) or s in [c for c in "abcdef"]:
                    continue
                else:
                    break
            return True
        return False

    if field == "ecl:":
        if data in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return True
        return False

    if field == "pid:":
        if len(data) is 9 and data.isdigit():
            return True
    return False


def validate(line):
    rule = [ "byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    line_list = line.split(" ")
    for r in rule:
        if r not in line:
            return False
        matching = [s for s in line_list if r in s]
        data = matching[0][4:]
        if validate_field(r, data):
            continue
        else:
            return False
    return True


def program_1(data,):
    merge_list = []
    string = ""
    valid = 0
    for line in data:
        if not line:
            merge_list.append(string)
            if validate(string):
                valid += 1
            string = ""
        else:
            string += line + " "
    merge_list.append(string)
    if validate(string):
        valid += 1
    print(valid)

def main():
    data = open_file("input.txt")
    program_1(data)


if __name__ == '__main__':
    main()
