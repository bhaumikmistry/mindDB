import copy
import math as m

def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [(entry.split('\n')[0]).split(' = ') for entry in f.readlines()]
        return entries


def countBits(number): 
      
    # log function in base 2  
    # take only integer part 
    return int((m.log(number) / 
                m.log(2)) + 1);


def genBins(n):
    """
       generate all the binary strings with n-length
    """
    max_int = '0b' + '1' * n
    return [str(format(i, 'b').zfill(n)) for i in range(0, int(max_int, 2)+1, 1)]


def program_2(current_mask, mem_loc, value, og_mem):
    b_mem = list(format(int(mem_loc), f'036b'))
    for i, val in enumerate(list(current_mask)):
        if val != "0":
            b_mem[i] = val
    count_x = ''.join(b_mem).count("X")
    new_mem_list = []
    # print(b_mem, mem_loc, count_x)
    for i in genBins(count_x):
        i = list(i)
        i.reverse()
        b_temp_mem = copy.deepcopy(b_mem)
        # print(i, count_x, genBins(count_x))
        count = len(i)
        for index, char in enumerate(b_mem):
            if char == "X":
                b_temp_mem[index] = i.pop()
            if not i:
                break
        og_mem[int(''.join(b_temp_mem),2)] = value
        new_mem_list.append(int(''.join(b_temp_mem),2))
    # print(new_mem_list)
    return og_mem




def program_1(data):
    mem = {}
    current_mask = []
    for line in data:
        if line[0] == "mask":
            current_mask = list(line[1])
        else:
            mem_loc = line[0].split("[")[1].split("]")[0]
            value = line[1]
            # print(''.join(current_mask))
            # print(format(int(value), f'036b'))
            b_value = list(format(int(value), f'036b'))
            for i, val in enumerate(list(current_mask)):
                if val != "X":
                    b_value[i] = val
            # print(''.join(b_value))
            # print(int(value), int(''.join(b_value),2))
            # mem[int(mem_loc)] = int(''.join(b_value),2)
            # print("--start--")
            mem = program_2(current_mask, mem_loc, int(value), mem)
            # print("--end--")
    return sum(mem.values())


def main():
    data = open_file("input.txt")
    print(program_1(data))


if __name__ == '__main__':
    main()
