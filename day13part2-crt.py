def get_inputs(FILENAME="day13input.txt"):
    begin_timestamp = None
    bus_ids = list()

    with open(FILENAME, "r") as f:
        lines = f.readlines()
        
        begin_timestamp = int(lines[0][:-1])
        
        bus_ids_raw = lines[1].split(',')
        
        for bus_id in bus_ids_raw:
            if bus_id == 'x':
                bus_ids.append(bus_id)
                continue
            bus_ids.append(int(bus_id))
        

        f.close()
    
    return begin_timestamp, bus_ids

def solve_crt(pair_modular_equations):
    remainder_pair = (0, 1) # remainder, coefficient

    for modular_equation in pair_modular_equations:
        coefficient = remainder_pair[1]

        for k in range(1, modular_equation[1]):
            if (coefficient * k) % modular_equation[1] == 1:
                remainder_pair = ((((modular_equation[0] - remainder_pair[0]) * k) % modular_equation[1]) * remainder_pair[1] + remainder_pair[0], remainder_pair[1] * modular_equation[1])
                break

    return remainder_pair


def get_modular_equations(bus_ids):
    k = 0

    modular_equations = list()

    for bus_id in bus_ids:
        if bus_id == 'x':
            k += 1
            continue
        
        modular_equations.append((-k % bus_id, bus_id))
        k += 1

    return modular_equations
        

begin_timestamp, bus_ids = get_inputs("day13input.txt")

print(begin_timestamp)
print(bus_ids)

modular_equations = get_modular_equations(bus_ids)

print(modular_equations)

solution_pair = solve_crt(modular_equations)

print(solution_pair)