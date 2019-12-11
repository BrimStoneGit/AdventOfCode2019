import day_3_challenge_1 as d3
import sys

# all_data = d3.load_input("../Data/test1_d3")
# print(all_data[0])
# print(all_data[1])

# start_point = (0, 0)
# visited_nodes_first = []
# for date in all_data[0]:
#     start_point = d3.parse_lines(start_point, date, visited_nodes_first)
# print(visited_nodes_first)

# start_point = (0, 0)
# visited_nodes_second = []
# for date in all_data[1]:
#     start_point = d3.parse_lines(start_point, date, visited_nodes_second)

# distances = []
# for i in visited_nodes_first:
#     for j in visited_nodes_second:
#         if i == j:
#             print("Node (" + str(i) + " , " + str(j) + ")")
#             distances.append(abs(i[0]) + abs(i[1]))

# print(distances)

f = open(sys.argv[2])
result = int(f.read())
calculation = d3.do_all(str(sys.argv[1]))
if (calculation == result):
    print("Test passed")
else:
    print("Test not passed. The Result should be " + str(result) + " but it is " + str(calculation))