# -*- coding: utf-8 -*-
# Use `Fraction` to avoid floaring-point errors
from fractions import Fraction

def is_24_points_solvable(numbers: list) -> (bool, int):
    # Pick two numbers, merge them, then put it back to the list
    # Do this recursively until there is only one number left.
    # If this number equals 24, we get a solution.
    #
    # The key point here is to ensure that all combinations are
    # considered.
    #
    # For each (i, j) index pair where i < j, we consider the merging of
    # the i-th and j-th items. After merging, the i-th position will store
    # the new number, and the j-th position will be deleted.
    if len(numbers) == 1:
        return (numbers[0] == 24, 0)
    
    total_recursion_times = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            add_numbers = numbers.copy()
            add_numbers[i] = numbers[i] + numbers[j]
            del add_numbers[j]
            is_solvable, recursion_times = is_24_points_solvable(add_numbers)
            total_recursion_times += recursion_times + 1
            if is_solvable:
                return (True, total_recursion_times)

            min1_numbers = numbers.copy()
            min1_numbers[i] = numbers[i] - numbers[j]
            del min1_numbers[j]
            is_solvable, recursion_times = is_24_points_solvable(min1_numbers)
            total_recursion_times += recursion_times + 1
            if is_solvable:
                return (True, total_recursion_times)

            min2_numbers = numbers.copy()
            min2_numbers[i] = numbers[j] - numbers[i]
            del min2_numbers[j]
            is_solvable, recursion_times = is_24_points_solvable(min2_numbers)
            total_recursion_times += recursion_times + 1
            if is_solvable:
                return (True, total_recursion_times)
            
            mul_numbers = numbers.copy()
            mul_numbers[i] = numbers[i] * numbers[j]
            del mul_numbers[j]
            is_solvable, recursion_times = is_24_points_solvable(mul_numbers)
            total_recursion_times += recursion_times + 1
            if is_solvable:
                return (True, total_recursion_times)
            
            if numbers[j] != 0:
                div1_numbers = numbers.copy()
                div1_numbers[i] = Fraction(numbers[i], numbers[j])
                del div1_numbers[j]
                is_solvable, recursion_times = is_24_points_solvable(div1_numbers)
                total_recursion_times += recursion_times + 1
                if is_solvable:
                    return (True, total_recursion_times)
            
            if numbers[i] != 0:
                div2_numbers = numbers.copy()
                div2_numbers[i] = Fraction(numbers[j], numbers[i])
                del div2_numbers[j]
                is_solvable, recursion_times = is_24_points_solvable(div2_numbers)
                total_recursion_times += recursion_times + 1
                if is_solvable:
                    return (True, total_recursion_times)
    
    return (False, total_recursion_times)

numbers = input("Please input numbers to compute 24: (use ',' to divide them)").split(',')

is_valid_input = True
for i in range(len(numbers)):
    if not numbers[i].isnumeric() or not (1 <= int(numbers[i]) <= 23):
        print("Invalid input: input should be integers between 1 and 23.")
        is_valid_input = False
        break
    
    numbers[i] = int(numbers[i])


if is_valid_input:
    is_solvable, recursion_times = is_24_points_solvable(numbers)
    print("Yes" if is_solvable else "No")
    print("Recursion times:", recursion_times)