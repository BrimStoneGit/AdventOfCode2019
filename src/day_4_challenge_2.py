inp_4 = "125730-579381"
ranges = inp_4.split("-")
num_solutions = 0
"""
adjacent_bool is a binary with three bits. 
right-most bit: temporary two-consecutive-number region
middle bit: more than two consecutive numbers
left-most bit: found one safe two-consecutive-number region
The two right bits cannot be set at the same time
"""
adjacent_bool_num = 0b000
ascending = True
for i in range(int(ranges[0]), int(ranges[1])):
    ascending = True
    adjacent_bool_num = 0b000
    for j in range(len(str(i)) - 1):
        if int(str(i)[j]) > int(str(i)[j + 1]):
            ascending = False
        # if two numbers are the same and the last number was different or it is the start:
        elif int(str(i)[j]) == int(str(i)[j + 1]) and (adjacent_bool_num & 0b011) == 0:
            # Set left-most bit
            adjacent_bool_num = adjacent_bool_num | 0b001
        # if two numbers are the same, but it is the third occurence:
        elif int(str(i)[j]) == int(str(i)[j + 1]) and (adjacent_bool_num & 0b001) == 1:
            # right-most bit gets unset and middle bit get set
            adjacent_bool_num = (adjacent_bool_num & 0b110) | 0b010
        # if two numbers are not the same, but the two numbers before were the same
        elif int(str(i)[j]) != int(str(i)[j + 1]) and (adjacent_bool_num & 0b001) == 1:
            # we found a winner! Set the left-most bit
            adjacent_bool_num = adjacent_bool_num | 0b100
        # if two numbers are not the same and the two numbers before them weren't either
        elif int(str(i)[j]) != int(str(i)[j + 1]) and (adjacent_bool_num & 0b001) == 0:
            # Reset Value 
            adjacent_bool_num = adjacent_bool_num & 0b100     
    if ascending and (adjacent_bool_num & 0b101 != 0):
        num_solutions += 1
print(num_solutions)
