from day_2_challenge_1 import parse_all_op_codes
from pprint import pprint

tests = []

tests.append("1,0,0,0,99")
tests.append("2,3,0,3,99")
tests.append("2,4,4,5,99,0")
tests.append("1,1,1,4,99,5,6,0,99")

# pprint(tests)

results = []

results.append("2,0,0,0,99")
results.append("2,3,0,6,99")
results.append("2,4,4,5,99,9801")
results.append("30,1,1,4,2,5,6,0,99")

# pprint(results)

for i in range(len(tests)):
    test = list(map(lambda x: int(x), tests[i].split(',')))
    result = list(map(lambda x: int(x), results[i].split(',')))
    parse_all_op_codes(test)
    if result == test:
        print("Success on test " + str(i))
    else:
        print("Failure on test " + str(i))
        print("Should be " + str(result) + ", but it is " + str(test))
