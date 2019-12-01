### PART 1
# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

# For example:

# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.

# The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

### PART 2
# Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

# So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

# A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.
# At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
# The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.


module_masses = [
    123265,
    68442,
    94896,
    94670,
    145483,
    93807,
    88703,
    139755,
    53652,
    52754,
    128052,
    81533,
    56602,
    96476,
    87674,
    102510,
    95735,
    69174,
    136331,
    51266,
    148009,
    72417,
    52577,
    86813,
    60803,
    149232,
    115843,
    138175,
    94723,
    85623,
    97925,
    141772,
    63662,
    107293,
    130779,
    147027,
    88003,
    77238,
    53184,
    149255,
    71921,
    139799,
    84851,
    104899,
    92290,
    74438,
    55631,
    58655,
    140496,
    110176,
    138718,
    104768,
    93177,
    53212,
    129572,
    69877,
    139944,
    116062,
    51362,
    135245,
    59682,
    128705,
    98105,
    69172,
    89244,
    109048,
    88690,
    62124,
    53981,
    71885,
    59216,
    107718,
    146343,
    138788,
    73588,
    51648,
    122227,
    54507,
    59283,
    101230,
    93080,
    123120,
    148248,
    102909,
    91199,
    105704,
    113956,
    120368,
    75020,
    103734,
    81791,
    87323,
    77278,
    123013,
    58901,
    136351,
    121295,
    132994,
    84039,
    76813,
]


def fuel_for_mass(mass):
    return (mass // 3) - 2


def total_fuel(module_masses):
    total_fuel = 0
    for mass in module_masses:
        fuel_for_module = fuel_for_mass(mass)
        total_fuel += fuel_for_module + fuel_for_fuel(fuel_for_module)

    return total_fuel


def fuel_for_fuel(fuel_mass):
    total_fuel = 0
    while fuel_mass > 6:
        print("### fuel: ", fuel_mass)
        fuel_mass = fuel_for_mass(fuel_mass)
        print("### mass for fuel: ", fuel_mass)
        # if fuel > 0:
        total_fuel += fuel_mass
        print("### total mass: ", total_fuel)

    return total_fuel


if __name__ == '__main__':

    assert total_fuel([1969]) == 966
    assert total_fuel([100756]) == 50346

    # 1. 3229279
    # 2. 4841054
    print(total_fuel(module_masses))
