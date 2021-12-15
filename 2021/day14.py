import time
from collections import defaultdict, deque, Counter
from functools import lru_cache #, cache


q1 = '''
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
'''

q2 = '''
BCHCKFFHSKPBSNVVKVSK

OV -> V
CO -> V
CS -> O
NP -> H
HH -> P
KO -> F
VO -> B
SP -> O
CB -> N
SB -> F
CF -> S
KS -> P
OH -> H
NN -> O
SF -> K
FH -> F
VV -> B
VH -> O
BV -> V
KF -> K
CC -> F
NF -> H
VS -> O
SK -> K
HV -> O
CK -> K
VP -> F
HP -> S
CN -> K
OB -> H
NS -> F
PS -> S
KB -> S
VF -> S
FP -> H
BB -> N
HF -> V
CH -> N
BH -> F
KK -> B
OO -> N
NO -> K
BP -> K
KH -> P
KN -> P
OF -> B
VC -> F
NK -> F
ON -> O
OC -> P
VK -> O
SH -> C
NH -> C
FB -> B
FC -> K
OP -> O
PV -> V
BN -> V
PC -> K
PK -> S
FF -> C
SV -> S
HK -> H
NB -> C
OK -> C
PH -> B
SO -> O
PP -> F
KV -> V
FO -> B
FN -> H
HN -> C
VB -> K
CV -> O
BC -> C
CP -> S
FS -> S
KP -> V
BS -> V
BK -> B
PN -> C
PF -> S
HO -> V
NC -> N
SS -> N
BO -> P
BF -> N
NV -> P
PB -> K
HB -> H
VN -> H
FV -> B
FK -> K
PO -> S
SC -> S
HS -> S
KC -> F
HC -> S
OS -> K
SN -> N
'''


def get_input(string):
    lines = [
        i
        for i in string.strip().split('\n')
    ]

    return lines[0], [l.split(' -> ') for l in lines[2:]]


LOG = True


def log(*args):
    if not LOG:
        return
    print(*args)


def boldify(val):
    return '\033[1m' + f"{val}" + '\033[0m'


def tester(arg, expected, method, debug=0, show_input_on_fail=False):
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


def do_insertions(template, rules):
    insertions = []
    debug = []
    last_insertion_idx = 0
    for idx, char in enumerate(template[:-1]):
        pair = template[idx:idx+2]
        log(pair, rules)

        if pair not in rules:
            continue

        insertions.append(template[last_insertion_idx:idx + 1])
        insertions.append(rules[pair])
        debug.append(rules[pair])
        last_insertion_idx = idx + 1

    log(debug)
    insertions.append(template[last_insertion_idx:])

    return "".join(insertions)


def do_insertions_fast(template, rules, counter, count, max_count, CACHE=None):
    if CACHE is None:
        CACHE = {}

    if CACHE.get((count, template)):
        log('reading from cache')
        return counter + CACHE[(count, template)]

    old_counter = Counter(counter)
    for idx, char in enumerate(template[:-1]):
        pair = template[idx:idx+2]

        insert_char = rules.get(pair)
        if insert_char is None:
            continue

        counter[insert_char] += 1

        if count < max_count:
            counter = do_insertions_fast(
                f'{char}{insert_char}{template[idx+1]}',
                rules,
                counter,
                count + 1,
                max_count,
                CACHE
            )
        else:
            log(counter, count, max_count)

    CACHE[(count, template)] = counter - old_counter
    log('write to cache')
    return counter


def problem_one(vals):
    template, rules = vals

    rules = {k: v for k, v in rules}

    new_template = template
    for i in range(10):
        new_template = do_insertions(new_template, rules)
        log(new_template, Counter(new_template))

    new_counts = Counter(new_template)

    return new_counts.most_common(1)[0][1] - new_counts.most_common()[-1][1]


def problem_two(vals):
    template, rules = vals

    rules = {k: v for k, v in rules}

    new_counts = do_insertions_fast(template, rules, counter=Counter(template), count=1, max_count=40)

    return new_counts.most_common(1)[0][1] - new_counts.most_common()[-1][1]


if __name__ == '__main__':

    run(problem_one, get_input(q1), 1588, debug=False)
    run(problem_one, get_input(q2), 2797, debug=False)

    run(problem_two, get_input(q1), 2188189693529, debug=False)
    run(problem_two, get_input(q2), 2926813379532, debug=False)
