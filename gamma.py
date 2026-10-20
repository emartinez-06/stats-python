from math import gamma, sqrt

alpha = 1.817
beta = 0.863

mean = beta * gamma(1 + 1 / alpha)
variance = beta**2 * (gamma(1 + 2 / alpha) - (gamma(1 + 1 / alpha) ** 2))
standard_deviation = sqrt(variance)

print("\u03bc:", f"{mean:>6.3f}")
print("\u03c3\u00b2:", f"{variance:>4.3f}")
print("\u03c3:", f"{standard_deviation:>6.3f}")
