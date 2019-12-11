from pprint import pprint

input_array = []
with open('../Data/input_d1') as f:
    for textline in f:
        input_array.append(textline[:-1])
# pprint(input_array)

def calculate_required_fuel(input_mass):
    return int(int(input_mass) / 3) - 2

fuel_sum = 0

for module_mass in input_array:
    fuel_sum += calculate_required_fuel(module_mass)

print(fuel_sum)