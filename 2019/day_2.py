
# vals = [1,9,10,3,2,3,11,0,99,30,40,50]
vals = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,13,23,27,1,6,27,31,1,31,10,35,1,35,6,39,1,39,13,43,2,10,43,47,1,47,6,51,2,6,51,55,1,5,55,59,2,13,59,63,2,63,9,67,1,5,67,71,2,13,71,75,1,75,5,79,1,10,79,83,2,6,83,87,2,13,87,91,1,9,91,95,1,9,95,99,2,99,9,103,1,5,103,107,2,9,107,111,1,5,111,115,1,115,2,119,1,9,119,0,99,2,0,14,0]

def process_code(op_code_idx, vals):
    if vals[op_code_idx] == 1:
        # add
        one = vals[op_code_idx + 1]
        two = vals[op_code_idx + 2]
        res = vals[op_code_idx + 3]

        vals[res] = vals[one] + vals[two]
        return vals, op_code_idx + 4

    elif vals[op_code_idx] == 2:
        # multiply
        one = vals[op_code_idx + 1]
        two = vals[op_code_idx + 2]
        res = vals[op_code_idx + 3]

        vals[res] = vals[one] * vals[two]
        return vals, op_code_idx + 4

    elif vals[op_code_idx] == 99:
        return None, vals[0]

    raise Exception(f"invalid op_code vals[{op_code_idx}] = {vals[op_code_idx]}")

def initialize(vals):
    vals[1] = 12
    vals[2] = 2

    return vals

def run_machine(vals):
    result = 0
    while vals:
        vals, result = process_code(result, vals)

    return result

def search_machine(vals, target):
    print("vals", vals)

    for noun in range(100):
        for verb in range(100):
            try:
                new_vals = vals[:]
                new_vals[1] = noun
                new_vals[2] = verb

                old_vals = new_vals[:]
                if run_machine(new_vals) == target:
                    print("vals", old_vals)
                    print("vals", new_vals)
                    print(f"{noun}, {verb} = {target}")
                    return 100 * noun + verb
            except:
                print(f"{noun}, {verb} invalid")

    return None

if __name__ == '__main__':
    new_vals = initialize(vals)[:]
    print(new_vals)

    result = run_machine(new_vals)
    print(f"result is: {result}")

    result = search_machine(vals, 19690720)
    print(f"result is: {result}")
