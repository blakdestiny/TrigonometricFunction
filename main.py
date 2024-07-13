import math

def find_b_beta(a, alpha, gamma):
    beta = 180 - (alpha + gamma)
    b = a * math.sin(math.radians(beta)) / math.sin(math.radians(alpha))
    print(f"The length of b is {b}")
    print(f"The angle beta is {beta} degrees")

while True:
    alpha = int(input("Enter angle alpha (degrees): "))
    gamma = int(input("Enter angle gamma (degrees): "))
    if (alpha + gamma) > 180:
        print(f"Invalid sum of angles. Please enter a values whose sum is less than 180.")
    else:
        break

while True:
    a = int(input("Enter length A: "))
    if a < 0:
        print(f"Invalid length, enter length greater than 0.")
    else:
        break

find_b_beta(a, alpha, gamma)