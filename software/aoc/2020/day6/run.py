# --- Day 6: Custom Customs ---


def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [entry.split('\n')[0] for entry in f.readlines()]
        return entries


def program_2(string, people):
    correct = 0
    for char in set(string):
        if string.count(char) == people:
            correct += 1
    return correct


def program_1(data):
    string = ""
    people = 0
    result_1 = 0
    result_2 = 0
    for d in data:
        if d is "":
            result_1 += len(set(string))
            temp_2 = program_2(string, people)
            result_2 += temp_2
            people = 0
            string = ""
            continue
        string += d
        people += 1
    result_1 += len(set(string))
    temp_2 = program_2(string, people)
    result_2 += temp_2
    print(result_1)
    print(result_2)


def main():
    data = open_file("input.txt")
    program_1(data)


if __name__ == '__main__':
    main()