import copy
import math as m

def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [[int(n) for n in entry.split(',')] for entry in f.readlines()][0]
        return entries


def program_2(data):
    return data


def get_update(mem, new, new_turn):
    previous_turn = mem[new].pop()
    pass


def program_1(data):
    mem = {}
    for i, d in enumerate(data[:-1],1):
        mem[d] = [i]
    turn = len(data)
    last = data[-1]
    last_perc = 0
    # print(mem)
    test = 0 
    while True:
        # print(turn, last, mem)
        if last in mem.keys():
            # print("last in mem")
            second_last_turn, last_turn = tuple(mem[last])
            turn+=1
            new = last_turn - second_last_turn
            if new in mem.keys():
                last_spoken = mem[new].pop()
                mem[new] = [last_spoken, turn]
            # print(turn, last, mem)
            last = new
        else:
            mem[last] = [turn]
            # print("last is new")
            new_turn = turn+1
            new = 0
            if new in mem.keys():
                last_spoken = mem[new].pop()
                mem[new] = [last_spoken, new_turn]
            last = new
            turn = new_turn
        # print(turn, last, mem)
        if turn == 30000000:
            break
        else:
            perc = 100*turn/30000000
            if perc > last_perc+1:
                print(perc)
                last_perc = perc
    return(last)
        





def main():
    data = open_file("input.txt")
    print(program_1(data))


if __name__ == '__main__':
    main()
