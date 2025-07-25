import math

try:
    num = float(input("Enter a positive number: "))
    
    if num <= 0:
        print("Please enter a number greater than 0 for logarithm and square root.")
    else:
        sqrt_result = math.sqrt(num)
        log_result = math.log(num)
        sine_result = math.sin(num)

        print("\nResults:")
        print(" Square root:", sqrt_result)
        print(" Natural logarithm (base e):", log_result)
        print(" Sine (in radians):", sine_result)

except ValueError:
    print("Invalid input. Please enter a numeric value.")
