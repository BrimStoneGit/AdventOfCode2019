from pprint import pprint

input_array = []
with open('input_d1') as f:
    for textline in f:
        input_array.append(textline[:-1])
# pprint(input_array)

def calculate_required_fuel(input_mass):
    return int(int(input_mass) / 3) - 2

fuel_sum = []

for module_mass in input_array:
    print("Number " + module_mass)
    fuel_array = []
    fuel_array.append(calculate_required_fuel(module_mass))
    print("Calculation 1 " + str(fuel_array[-1]))
    while(1):
        fuel_array.append(calculate_required_fuel(fuel_array[-1]))
        print("Calculation: next: " + str(fuel_array[-1]))
        if fuel_array[-1] <= 0:
            pprint([0 if i < 0 else i for i in fuel_array])
            fuel_sum.append(sum([0 if i < 0 else i for i in fuel_array]))
            break

print(sum(fuel_sum))