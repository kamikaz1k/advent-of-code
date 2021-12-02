import time
def tester(input, expected, method, debug=0, show_input_on_fail=True):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    start = time.time()

    if debug:
        actual = method(*input, debug=debug)
    else:
        actual = method(*input)

    duration = time.time() - start
    result = actual == expected
    print("OURS Pass: ", OKGREEN if result else FAIL, result, ENDC, " time: ", duration, " Actual: ", actual, " Expected: ", expected)#, " Input: ", input)

    if show_input_on_fail and not result:
        print("Failed for input: ", *input)

t = tester
