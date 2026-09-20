def square_root_bisection(value, tolerance= 0.01, max_iterations= 10):
    if value < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if value == 0 or value == 1:
        print(f"The square root of {value} is {value}")
        return value
    i = 0
    divisor = value / 2
    while i <= max_iterations:
        divisor_result = value / divisor
        average = ((divisor + divisor_result) / 2)
        if value / average == average:
            return average
        if abs(divisor - average) <= tolerance:
            print(f"The square root of {value} is approximately {average}")
            return average
        else:
            divisor = average
        print(average)
        i += 1
    print(f"Failed to converge within {max_iterations} iterations")
    return None


print(square_root_bisection(225, 1e-7, 10))

