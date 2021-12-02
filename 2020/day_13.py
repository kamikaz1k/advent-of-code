test_values = '''
939
7,13,x,x,59,x,31,19
'''.strip().split('\n')

test_values2 = '''
939
17,x,13,19
'''.strip().split('\n')

values = '''
1001938
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,431,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,19,x,x,x,x,x,x,x,x,x,x,x,863,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29
'''.strip().split('\n')

import math

def find_num_closest_to_target(target, base):
    return math.ceil(target / base) * base

def find_num_closest_to_target_exceeding(target, base):
    result = math.ceil(target / base)
    if target % base == 0:
        result += 1
    return result * base


def get_bus_ids(vals):
    return [
        int(b) for b in vals[1].split(',') if b != 'x'
    ]

def problem_one(vals):
    departure_time = int(vals[0])
    bus_ids = get_bus_ids(vals)

    # find lowest exceeding or equal sum
    # the lowest exceeding sum is going to be the
    # pick the lower id

    closest_times = [
        (find_num_closest_to_target(departure_time, bus), bus)
        for bus in bus_ids
    ]

    lowest_time, acceptable_bus_id = sorted(closest_times)[0]

    time_to_wait = lowest_time - departure_time
    return time_to_wait * acceptable_bus_id

def get_slope(X, m1, c, m2):
    # 7 * X + 1 = 13 * Y
    # m1 * X + c = m2 * Y

    # for x = 1
    # 7 + 1 = 13 Y
    # 8/13 = Y
    left = m1 * X + c
    return left / m2

def is_integer_slope(X, m1, c, m2):
    left = m1 * X + c
    return (left % m2) == 0

def find_slope_starting_at(bus_id1, bus_id2, offset, starting):
    # `starting` is the integer factor for bus_id1
    while True:
        if is_integer_slope(starting, bus_id1, offset, bus_id2):
            return starting

        starting += 1

def problem_two(vals, start_after=None):
    size = 10000
    count = 0
    def log(*args):
        nonlocal count
        if count % size == 0:
            print(*args)
        count += 1

    # bus_ids = get_bus_ids(vals)
    bus_id_and_idx = [
        (idx, int(b))
        for idx, b in enumerate(vals[1].split(',')) if b != 'x'
    ]

    # starting is the integer factor for bus_id_1
    starting = 1
    if start_after is not None:
        result = find_num_closest_to_target(start_after, bus_id_and_idx[0][1])
        starting = result // bus_id_and_idx[0][1]

    while True:
        prev_idx, prev_bus_id = bus_id_and_idx[0]
        idx, bus_id = bus_id_and_idx[1]

        offset = idx - prev_idx
        starting = find_slope_starting_at(prev_bus_id, bus_id, offset, starting)
        # print(f'new starting {starting}')

        assert (starting * prev_bus_id) - find_num_closest_to_target(starting * prev_bus_id, bus_id) == -offset

        prev_timestamp = (starting * prev_bus_id)
        starting_timestamp = prev_timestamp
        log(f'new starting({starting}) with timestamp {starting_timestamp}')

        bail_main = True
        # prev_idx, prev_bus_id = bus_id_and_idx[1]
        for (prev_idx, prev_bus_id), (idx, bus_id) in zip(bus_id_and_idx[1:-1], bus_id_and_idx[2:]):

            result = find_num_closest_to_target_exceeding(starting_timestamp, bus_id)
            # prev_timestamp = (starting * prev_bus_id)
            if result != (starting_timestamp + idx):
                bail_main = False
                starting += 1
                break
            # import pdb; pdb.set_trace()
            # print(f'maybe {starting} for timestamp {starting * bus_id_and_idx[0][1]}')

        if bail_main:
            break

    prev_timestamp = starting * bus_id_and_idx[0][1]
    starting_timestamp = prev_timestamp
    for idx, bus_id in bus_id_and_idx:
        result = find_num_closest_to_target(prev_timestamp, bus_id)

        print(f'offset: {idx} bus: {bus_id} timestamp: {result} expected: {starting_timestamp + idx} and {result / bus_id}')
        prev_timestamp = result

    return starting * bus_id_and_idx[0][1]


if __name__ == '__main__':

    from helpers import tester

    tester(
        (test_values,),
        295,
        problem_one
    )

    tester(
      (test_values,),
      1068781,
      problem_two
    )

    tester(
      (test_values2,),
      3417,
      problem_two
    )

    tester(
      ([1, "67,7,59,61"],),
      754018,
      problem_two
    )

    tester(
      ([1, "67,x,7,59,61"],),
      779210,
      problem_two
    )

    tester(
      ([1, "67,7,x,59,61"],),
      1261476,
      problem_two
    )

    tester(
      ([1, "1789,37,47,1889"],),
      1202161486,
      problem_two
    )

    # print('problem_one', problem_one(values))
    print('problem_two', problem_two(values, start_after=100087735696234))

