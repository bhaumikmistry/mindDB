---
description: Advent of Code at https://adventofcode.com/
---
# Advent of Code


{% tabs %}
{% tab title="Day 1" %}
### 12-01-2020 
```pyhton
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
