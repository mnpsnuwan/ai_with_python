import scipy.optimize

# Objective Function   : 50X1 + 80X2
# Constraint      : 5X1 + 2X2 <= 20
# Constraint      : (-10X1) + (-12X2) <= -90

result = scipy.optimize.linprog(
    [50, 80],  # Cost function 50X1 + 80X2
    A_ub=[[5, 2], [-10, -12]],  # Coefficient for inequalities
    b_ub=[20, -90],  # Constraints for inequalities: 20 and -90
)

if result.success:
    print(f"X1: {round(result.x[0], 2)} hours")
    print(f"X2: {round(result.x[1], 2)} hours")

else:
    print("No solution")

