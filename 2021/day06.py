q1 = '''
3,4,3,1,2
'''

q2 = '''
5,1,1,3,1,1,5,1,2,1,5,2,5,1,1,1,4,1,1,5,1,1,4,1,1,1,3,5,1,1,1,1,1,1,1,1,1,4,4,4,1,1,1,1,1,4,1,1,1,1,1,5,1,1,1,4,1,1,1,1,1,3,1,1,4,1,4,1,1,2,3,1,1,1,1,4,1,2,2,1,1,1,1,1,1,3,1,1,1,1,1,2,1,1,1,1,1,1,1,4,4,1,4,2,1,1,1,1,1,4,3,1,1,1,1,2,1,1,1,2,1,1,3,1,1,1,2,1,1,1,3,1,3,1,1,1,1,1,1,1,1,1,3,1,1,1,1,3,1,1,1,1,1,1,2,1,1,2,3,1,2,1,1,4,1,1,5,3,1,1,1,2,4,1,1,2,4,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,4,3,1,2,1,2,1,5,1,2,1,1,5,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1,1,3,1,1,5,1,1,1,1,5,1,4,1,1,1,4,1,3,4,1,4,1,1,1,1,1,1,1,1,1,3,5,1,3,1,1,1,1,4,1,5,3,1,1,1,1,1,5,1,1,1,2,2
'''


def get_input(string):
    return [
        int(i)
        for i in string.strip().split(',')
    ]


def run(problem, arg, expected=None):
    print(problem.__name__, 'result:', problem(arg), 'expected: ' + str(expected) if expected else None)


class Counter:

    NEW_TIME = 8
    RESET_TIME = 6

    def __init__(self, vals):
        # self._vals = {val: 0 for val in range(self.NEW_TIME)}
        self._vals = [0] * (self.NEW_TIME + 1)
        self._day = 0

        for val in vals:
            self._vals[val] += 1

    def __str__(self):
        return f"After Day {self._day:02d}: {self._vals} ({self.size()})"

    __repr__ = __str__

    def tick(self):
        # for idx in range(len(self._vals)):
        #     self._vals[idx] -= 1
        #     if self._vals[idx] < 0:
        #         self._vals.append(self.NEW_TIME)
        #         self._vals[idx] = self.RESET_TIME
        reset_count = self._vals[0]
        for idx in range(self.NEW_TIME):
            self._vals[idx] = self._vals[idx + 1]

        self._vals[self.RESET_TIME] += reset_count
        self._vals[self.NEW_TIME] = reset_count

        self._day += 1

    def size(self):
        # return len(self._vals)
        total = 0
        for count in self._vals:
            total += count

        return total


def problem_one(vals):
    vals, days = vals

    counter = Counter(vals)
    # print(counter)

    for day in range(days):
        counter.tick()
        # print(counter)

    return counter.size()


def problem_two(vals):
    pass


if __name__ == '__main__':

    run(problem_one, (get_input(q1), 18), 26)
    run(problem_one, (get_input(q1), 80), 5934)
    run(problem_one, (get_input(q2), 80))
    run(problem_one, (get_input(q2), 256))
