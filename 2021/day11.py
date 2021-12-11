q1 = '''
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''

q2 = '''
2238518614
4552388553
2562121143
2666685337
7575518784
3572534871
8411718283
7742668385
1235133231
2546165345
'''

from collections import defaultdict, deque, Counter


def log(*args):
    # return
    print(*args)


def get_input(string):
    return [
        [int(v) for v in i]
        for i in string.strip().split('\n')
    ]


def run(problem, arg, expected=None):
    print(problem.__name__, 'result:', problem(arg), 'expected: ' + str(expected) if expected else None)


class Grid:
    def __init__(self, grid):
        self._grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self._steps = 0
        self._visited = self._init_visited()
        self._last_cycle_flash_counter = 0
        self._flash_counter = 0

    def _init_visited(self):
        return [
            [False] * len(self._grid[0]) for _ in range(len(self._grid))
        ]

    def __str__(self):
        return (
            f"Step {self._steps}\n" +
            "\n".join([
                "".join(self._get_formatted_val(row, col) for col in range(self.cols))
                for row in range(self.rows)
            ]) +
            f"\n{self._flash_counter} Flashes (+{self._last_cycle_flash_counter})"
        )

    def _get_formatted_val(self, row, col):
        if self._visited[row][col]:
            return '\033[1m' + f"{self._grid[row][col]}" + '\033[0m'
        return f"{self._grid[row][col]}"

    __repr__ = __str__

    def get_val(self, row, col):
        return self._grid[row][col]

    def set_val(self, row, col, val):
        self._grid[row][col] = val

    def get_adjacent_coordinates(self, row, col):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                check_row = row + i
                check_col = col + j

                if 0 <= check_col < self.cols and 0 <= check_row < self.rows:
                    yield check_row, check_col

    def cycle(self):
        MAX = 9
        MIN = 0
        rows = len(self._grid)
        cols = len(self._grid[0])
        visited = self._init_visited()

        queue = deque([])

        for row in range(rows):
            for col in range(cols):
                val = self.get_val(row, col)
                val += 1
                if val > MAX:
                    queue.append((row, col))
                self.set_val(row, col, val)

        flashes = 0
        while queue:
            row, col = queue.popleft()
            if visited[row][col]:
                continue

            visited[row][col] = True

            self._grid[row][col] = MIN
            flashes += 1

            for adj_row, adj_col in self.get_adjacent_coordinates(row, col):
                if visited[adj_row][adj_col]:
                    continue

                val = self.get_val(adj_row, adj_col)
                val += 1
                if val > MAX:
                    queue.append((adj_row, adj_col))
                self.set_val(adj_row, adj_col, val)

        self._steps += 1
        self._visited = visited
        self._last_cycle_flash_counter = flashes
        self._flash_counter += flashes

    @property
    def flashes(self):
        return self._flash_counter

    @property
    def steps(self):
        return self._steps

    def go_to_step(self, step):
        while self._steps < step:
            self.cycle()

    def go_to_all_flash(self):
        while self._last_cycle_flash_counter != 100:
            self.cycle()


def problem_one(vals):
    grid = Grid(vals)
    grid.go_to_step(100)
    return grid.flashes


def problem_two(vals):
    grid = Grid(vals)
    grid.go_to_all_flash()
    return grid.steps


if __name__ == '__main__':

    run(problem_one, get_input(q1), 1656)
    run(problem_one, get_input(q2), 1723)

    run(problem_two, get_input(q1), 195)
    run(problem_two, get_input(q2), 327)
