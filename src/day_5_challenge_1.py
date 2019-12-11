DEBUG_LOGS = True

with open("../Data/input_d5") as f:
    op_code = list(map(lambda x: int(x), f.read().split(',')))

# Modified version of day 2 parser
# result: steps of the instruction pointer after the execution
def parse_single_op_code(op_code, pointer):
    modes = str(int(op_code[pointer] / 100))
    if op_code[pointer] > 10:
        for i in range(len(modes), 3):
            modes = "0" + modes
        
    # TODO: code the position/instruction mode variable


    if op_code[pointer] % 10 == 1:
        # execute add here
        if(DEBUG_LOGS):
            print("On position " + str(op_code[pointer + 3]) + " will be " + str(op_code[op_code[pointer + 1]]) + " plus " + str(op_code[op_code[pointer + 2]]))
        op_code[op_code[pointer + 3]] = op_code[op_code[pointer + 1]] + op_code[op_code[pointer + 2]]
        return 4
    elif op_code[pointer] % 10 == 2:
        # execute multiply here
        if(DEBUG_LOGS):
            print("On position " + str(op_code[pointer + 3]) + " will be " + str(op_code[op_code[pointer + 1]]) + " times " + str(op_code[op_code[pointer + 2]]))
        op_code[op_code[pointer + 3]] = op_code[op_code[pointer + 1]] * op_code[op_code[pointer + 2]]
        return 4
    elif op_code[pointer] % 10 == 3:
        # execute input here
        while (1):
            try:
                input_val = int(input("Your input: "))
                if input_val < 0 or input_val > 9:
                    raise ValueError("The input must be between 0 and 9, please try again!")
                else:
                    break
            except ValueError as err:
                print("An Error occured: " + repr(err))
        op_code[op_code[pointer + 1]] = input_val
        return 2
    elif op_code[pointer] % 10 == 4:
        # execute output here
        if op_code[pointer] > 10:
            print(op_code[pointer + 1])
        else:
            print(op_code[op_code[pointer + 1]])
        return 2
    else:
        return 0
    return 0
