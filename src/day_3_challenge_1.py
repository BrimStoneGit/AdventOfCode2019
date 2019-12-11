# startpoint: (int, int), input: "Rxx" or "Lxx" or "Uxx" or "Dxx" as str, visited Nodes: [list with tuples (x, y)] 
def parse_lines(startpoint, input, visited_nodes):
    if (input[0] == "R"):
        for i in range(int(input[1:]) + 1):
            visited_nodes.append((startpoint[0] + i, startpoint[1]))
        return (startpoint[0] + int(input[1:]), startpoint[1])
    elif (input[0] == "L"):
        for i in range(int(input[1:]) + 1):
            visited_nodes.append((startpoint[0] - i, startpoint[1]))
        return (startpoint[0] - int(input[1:]), startpoint[1])
    elif (input[0] == "U"):
        for i in range(int(input[1:]) + 1):
            visited_nodes.append((startpoint[0], startpoint[1] + i))
        return (startpoint[0], startpoint[1] + int(input[1:]))
    elif (input[0] == "D"):
        for i in range(int(input[1:]) + 1):
            visited_nodes.append((startpoint[0], startpoint[1] - i))
        return (startpoint[0], startpoint[1] - int(input[1:]))



def load_input(name):
    input_array = []
    with open(name) as f:
        for line in f:
            input_array.append([x.replace("\n", "") for x in line.split(",")])
    return input_array

def calculate_distances(list_of_lists):
    distances = []
    for i in list_of_lists[0]:
        print("On position " + str(list_of_lists[0].index(i)) + " of " + str(len(list_of_lists[0])))
        for j in list_of_lists[1]:
            if i == j:
                distances.append(abs(i[0]) + abs(i[1]))
    return distances

def do_all(name):
    input_array = load_input(name)
    visited_nodes = [[],[]]
    for each_list in range(len(input_array)):
        startpoint = (0,0)
        for each_element in input_array[each_list]:
            startpoint = parse_lines(startpoint, each_element, visited_nodes[each_list])
    distances = calculate_distances(visited_nodes)
    return min(list(filter(lambda x: x > 0, distances)))
    
    
