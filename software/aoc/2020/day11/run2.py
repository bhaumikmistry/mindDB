import os.path

input_path = "input.txt"

class Ferry:
    def __init__(self, map, threshold):
        self.state = map
        self.threshold = threshold
                
    def update(self):
        new_state = ['.' * len(self.state[0]) for _ in range(len(self.state))]

        for row in range(len(self.state)):
            for col in range(len(self.state[0])):
                change = self.state[row][col]
                if self.state[row][col] == 'L' and self.adjacentOccupiedCount(row, col) == 0:
                    change = '#'
                elif self.state[row][col] == '#' and self.adjacentOccupiedCount(row, col) >= self.threshold:
                    change = 'L'

                new_state[row] = new_state[row][:col] + change + new_state[row][col + 1:]

        return new_state

    def adjacentOccupiedCount(self, row, col):
        count = 0
        for j in range(max(0, row - 1), min(row + 1, len(self.state) - 1) + 1):
            # r = ''
            for i in range(max(0, col - 1), min(col + 1, len(self.state[0]) - 1) + 1):
                # r = r + self.state[j][i]
                if self.state[j][i] == '#' and not (row == j and col == i):
                    count += 1
            # print(r)

        return count

    def print(self, state):
        for row in range(len(state)):
            print(state[row])

    def debug(self):
        self.print(self.state)
        print('\n')
    
    def run(self):
        new_state = self.update()

        while self.state != new_state:
            self.state = new_state.copy()
            new_state = self.update()

    def countOccupied(self):
        count = 0
        for row in range(len(self.state)):
            for col in range(len(self.state[0])):
                if self.state[row][col] == '#':
                    count += 1
        return count

class Ferry2(Ferry):
    def __init__(self, map, threshold):
        super().__init__(map, threshold)

    def closestNonEmpty(self, row, col, delta_x, delta_y):
        i, j = col + delta_x, row + delta_y

        while i in range(0, len(self.state[0])) and j in range(0, len(self.state)):
            if self.state[j][i] != '.':
                return self.state[j][i]
            else:
                i, j = i + delta_x, j + delta_y

        return '.'

    def adjacentOccupiedCount(self, row, col):
        count = 0
        #top left
        if self.closestNonEmpty(row, col, -1, -1) == '#':
            count += 1
        if self.closestNonEmpty(row, col, -1, 0) == '#':
            count += 1
        if self.closestNonEmpty(row, col, -1, 1) == '#':
            count += 1
        if self.closestNonEmpty(row, col, 0, 1) == '#':
            count += 1
        if self.closestNonEmpty(row, col, 0, -1) == '#':
            count += 1
        if self.closestNonEmpty(row, col, 1, 1) == '#':
            count += 1
        if self.closestNonEmpty(row, col, 1, 0) == '#':
            count += 1
        if self.closestNonEmpty(row, col, 1, -1) == '#':
            count += 1

        return count

with open(input_path) as f:
    map = f.read().strip().split('\n')
    
    ferry = Ferry(map, 4)
    ferry.run()

    print(f'Part 1: {ferry.countOccupied()}')

    ferry2 = Ferry2(map, 5)
    ferry2.run()

    print(f'Part 2: {ferry2.countOccupied()}')