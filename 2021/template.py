import time
from collections import defaultdict, deque, Counter


q1 = '''
'''

q2 = '''
'''


def get_input(string):
    return [
        i
        for i in string.strip().split('\n')
    ]


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

    log("hi!")

    duration = time.time() - start
    result = actual == expected
    print("Pass: ", OKGREEN if result else FAIL, result, ENDC, " time: ", duration, " Actual: ", actual, " Expected: ", expected)#, " Input: ", input)

    if show_input_on_fail and not result:
        print("Failed for input: ", arg)


def run(problem, arg, expected=None, debug=None):
    if debug is None:
        debug = LOG
    tester(arg, expected, problem, debug=debug)


def problem_one(vals):
    pass


def problem_two(vals):
    pass


if __name__ == '__main__':

    run(problem_one, get_input(q1), debug=True)
    # run(problem_one, get_input(q2))

    # run(problem_two, get_input(q1))
    # run(problem_two, get_input(q2))
