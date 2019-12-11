from pprint import pprint

DEBUG_LOGS = False

with open("input_d2") as f:
    op_code = list(map(lambda x: int(x), f.read().split(',')))

def parse_single_op_code(op_code, pointer):
    if op_code[pointer] == 1:
        # execute add here
        if(DEBUG_LOGS):
            print("On position " + str(op_code[pointer + 3]) + " will be " + str(op_code[op_code[pointer + 1]]) + " plus " + str(op_code[op_code[pointer + 2]]))
        op_code[op_code[pointer + 3]] = op_code[op_code[pointer + 1]] + op_code[op_code[pointer + 2]]
    elif op_code[pointer] == 2:
        # execute multiply here
        if(DEBUG_LOGS):
            print("On position " + str(op_code[pointer + 3]) + " will be " + str(op_code[op_code[pointer + 1]]) + " times " + str(op_code[op_code[pointer + 2]]))
        op_code[op_code[pointer + 3]] = op_code[op_code[pointer + 1]] * op_code[op_code[pointer + 2]]
    elif op_code[pointer] == 99:
        return 1
    else:
        return -1
    return 0

def parse_all_op_codes(op_code):
    execution_finished = 0
    pointer = 0
    while (execution_finished != 1):
        if(DEBUG_LOGS):
            print(op_code)
        execution_finished = parse_single_op_code(op_code, pointer)
        pointer += 4

parse_all_op_codes(op_code)
print(op_code)

# pos = 0
# for number in op_code:
#     if pos % 4 != 3:
#         print(str(number) + ",", end = "")
#     else:
#         print(number)
#     pos += 1
    