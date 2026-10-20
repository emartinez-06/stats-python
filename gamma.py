from math import gamma, sqrt

alpha = 1.817
beta = 0.863

mean = beta * gamma(1 + 1 / alpha)
variance = beta**2 * (gamma(1 + 2 / alpha) - (gamma(1 + 1 / alpha) ** 2))
standard_deviation = sqrt(variance)

print("mean:", f"{mean:>25}")
print("variance:", f"{variance:>25}")
print("standard_deviation:", f"{standard_deviation:>25}")
