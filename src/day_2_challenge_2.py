from day_2_challenge_1 import parse_all_op_codes

for i in range(100):
    for j in range(100):
        with open("input_d2") as f:
            op_code = list(map(lambda x: int(x), f.read().split(',')))
        op_code[1] = i
        op_code[2] = j
        parse_all_op_codes(op_code)
        if (op_code[0] == 19690720):
            print("Found values: " + str(i) + " and " + str(j) + ", calculated to " + str(100 * i + j))

