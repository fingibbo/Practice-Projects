def square_root_bisection(value, tolerance= 0.01, max_iterations= 10):
    if value < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if value == 0 or value == 1:
        print(f"The square root of {value} is {value}")
        return value
    i = 0
    lower_bound = 0.0
    upper_bound = value if value >= 1 else 1
    while i < max_iterations:
        mid = (lower_bound + upper_bound) / 2
        mid_sqr = mid ** 2
        if abs(upper_bound - lower_bound) <= tolerance:
            print(f"The square root of {value} is approximately {mid}")
            return mid
        if mid_sqr > value:
            upper_bound = mid
        else:
            lower_bound = mid
        print(mid)
        i += 1
    print(f"Failed to converge within {max_iterations} iterations")
    return None


print(square_root_bisection(225, 1e-7, 10))

