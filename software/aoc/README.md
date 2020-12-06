---
description: Advent of Code at https://adventofcode.com/
---
# Advent of Code


{% tabs %}
{% tab title="Day 6" %}
```python
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

data = open_file("input.txt")
program_1(data)
```
{% endtab %}

{% tab title="Day 5" %}
```python
import math


def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [entry.split('\n')[0] for entry in f.readlines()]
        return entries


def validate(letter, lower, upper):
    if letter in ['F', 'L']:
        return lower, lower+int(math.ceil((upper-lower)/2))
    else:
        return lower+int(math.floor(1+(upper - lower)/2)), upper


def program_1(data):
    lower = 0
    upper = 127
    for letter in data[:7]:
        lower, upper = validate(letter, lower, upper)
    row = lower
    lower = 0
    upper = 7
    for letter in data[7:]:
        lower, upper = validate(letter, lower, upper)
    column = lower
    return row * 8 + column

data = open_file("input.txt")
seat_id = 0
seat_list = []
for string in data:
    id = program_1(string)
    seat_list.append(id)
    if id > seat_id:
        seat_id = id
print("result_1", seat_id)
seat_list.sort()
x = seat_list[0]
for y in seat_list[1:-1]:
    if x+1 == y:
        x = y
    else:
        print("result", x+1)
        break
```
{% endtab %}

{% tab title="Day 4" %}
```
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

data = open_file("input.txt")
program_1(data)
```
{% endtab %}

{% tab title="Day 3" %}
```
def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [list(entry.split('\n')[0]) for entry in f.readlines()]
        return entries


def program_1(data, move_right, move_down):
    length = len(data)
    width = len(data[0])
    tree_count = 0
    w = 0
    l = 0
    while l < length:
        w += move_right
        l += move_down
        w = w - width if w >= width else w
        if l >= length:
            break
        if data[l][w] == "#":
            tree_count += 1
    return tree_count


data = open_file("input.txt")
result = 1
for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    result *= program_1(data, x, y)
print(result)
```
{% endtab %}

{% tab title="Day 2" %}
```pyhton
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


data = open_file("input.txt")
print(program_1(data))
print(program_2(data))
```
{% endtab %}

{% tab title="Day 1" %}
```pyhton
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

print(program_1(data))
print(program_2(data))
```
{% endtab %}
{% endtabs %}