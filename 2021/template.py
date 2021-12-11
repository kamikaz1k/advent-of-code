q1 = '''
'''

q2 = '''
'''

from collections import defaultdict, deque, Counter


def log(*args):
    # return
    print(*args)


def get_input(string):
    return [
        i
        for i in string.strip().split('\n')
    ]


def run(problem, arg, expected=None):
    print(problem.__name__, 'result:', problem(arg), 'expected: ' + str(expected) if expected else None)


def problem_one(vals):
    pass


def problem_two(vals):
    pass


if __name__ == '__main__':

    run(problem_one, get_input(q1))
    # run(problem_one, get_input(q2))

    # run(problem_two, get_input(q1))
    # run(problem_two, get_input(q2))
