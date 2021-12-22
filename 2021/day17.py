import time
from collections import defaultdict, deque, Counter


q1 = '''
target area: x=20..30, y=-10..-5
'''

q2 = '''
target area: x=70..96, y=-179..-124
'''


def get_input(string):
    x, y = string.strip().replace('target area: ', '').split(', ')
    x = x[2:].split('..')
    y = y[2:].split('..')

    x = [int(i) for i in x]
    y = [int(i) for i in y]

    return x, y


LOG = True


def log(*args):
    if not LOG:
        return
    print(*args)


def boldify(val):
    return '\033[1m' + f"{val}" + '\033[0m'


def tester(arg, expected, method, debug=0, show_input_on_fail=True):
    global LOG

    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    # HEADER = '\033[95m'
    # OKBLUE = '\033[94m'
    # WARNING = '\033[93m'
    # BOLD = '\033[1m'
    # UNDERLINE = '\033[4m'
    LOG = bool(debug)

    start = time.time()
    actual = method(arg)

    duration = time.time() - start
    result = actual == expected
    print("Pass: ", OKGREEN if result else FAIL, result, ENDC, " time: ", duration, " Actual: ", actual, " Expected: ", expected)#, " Input: ", input)

    if show_input_on_fail and not result:
        print("Failed for input: ", arg)


def run(problem, arg, expected=None, debug=None):
    if debug is None:
        debug = LOG
    tester(arg, expected, problem, debug=debug)


class Launcher:
    def __init__(self, x_range, y_range):
        self.x_range = x_range
        self.y_range = y_range
        self._last_velocity = []

    def get_height_for_start(self, x_velocity, y_velocity):
        x, y = 0, 0
        vx, vy = x_velocity, y_velocity

        max_height = y
        while not self.is_beyond_box(x, y, vx, vy):
            x, y, vx, vy = self.calculate(x, y, vx, vy)
            max_height = max(max_height, y)
            if self.in_bounding_box(x, y):
                return max_height

        return -1

    def solve(self):
        MAX_Y_VELOCITY = 200
        max_height = 0
        max_height_velocity = None
        for dx in range(max(self.x_range) // 2):
            for dy in range(MAX_Y_VELOCITY):
                height = self.get_height_for_start(dx, dy)

                if height > max_height:
                    max_height = height
                    max_height_velocity = dx, dy

        log(max_height_velocity)
        return max_height

    def solve_all(self):
        MAX_Y_VELOCITY = 200
        max_height = 0
        max_height_velocity = None
        solution_count = 0
        solutions = []

        # log(max(self.x_range), (min(self.y_range), MAX_Y_VELOCITY))
        for dx in range(max(self.x_range) + 1):
            for dy in range(min(self.y_range), MAX_Y_VELOCITY):
                # if (dx, dy) in [(30, -6), (30, -10), (30, -8), (30, -7), (30, -9), (30, -5)]:
                #     import pdb; pdb.set_trace()
                #     True
                height = self.get_height_for_start(dx, dy)
                if height != -1:
                    solution_count += 1
                    solutions.append((dx, dy))

                if height > max_height:
                    max_height = height
                    max_height_velocity = dx, dy

        log(max_height, max_height_velocity)
        log(solution_count)
        log(solutions)
        return solution_count

    def in_bounding_box(self, x, y):
        return self._in_range(self.x_range, x) and self._in_range(self.y_range, y)

    def _in_range(self, box, v):
        return min(box) <= v <= max(box)

    def is_beyond_box(self, x, y, vx, vy):
        if x > max(self.x_range):
            return True
        if y < min(self.y_range) and vy <= 0:
            return True
        # if y > max(self.y_range)
        return False

    def calculate(self, x, y, vx, vy):
        new_x = x + vx
        new_y = y + vy

        new_vx = 0
        if vx > 0:
            new_vx = vx - 1
        elif vx < 0:
            new_vx = vx + 1

        new_vy = vy - 1

        return new_x, new_y, new_vx, new_vy

    def __str__(self):
        return f"<Launcher {self.x_range} {self.y_range} >"


def problem_one(vals):
    l = Launcher(*vals)
    result = l.solve()
    log(result)
    return result


def problem_two(vals):
    l = Launcher(*vals)
    solutions = l.solve_all()
    return solutions


if __name__ == '__main__':
    log(get_input(q1))
    run(problem_one, get_input(q1), 45, debug=True)
    run(problem_one, get_input(q2), 15931)

    run(problem_two, get_input(q1), 112, debug=True)
    run(problem_two, get_input(q2))
