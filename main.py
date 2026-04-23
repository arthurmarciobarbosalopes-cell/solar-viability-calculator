# ------------------------
# INPUTS
# ------------------------

print("=== Solar Viability Calculator ===")

P = float(input("System power (kW): "))
G_m = float(input("Monthly solar irradiation (kWh/kW/month): "))
eta = float(input("System efficiency (0–1): "))
T = float(input("Electricity tariff ($/kWh): "))
C = float(input("Installation cost ($): "))
Cm = float(input("Annual maintenance cost ($): "))
N = int(input("Number of households in the city: "))
alpha = float(input("Adoption rate (0–1): "))
t = float(input("Time horizon (years): "))

# ------------------------
# CALCULATIONS
# ------------------------

Sm = P * G_m * eta * T
R = 12 * t * Sm - C - t * Cm

den = 12 * Sm - Cm

if den <= 0:
    payback = None
else:
    payback = C / den

R_city = alpha * N * R

# ------------------------
# OUTPUT
# ------------------------

print("\n=== RESULTS ===")

print(f"Time analyzed: {t:.2f} years")

if R >= 0:
    print(f"Individual return: {R:.2f} $ (profit)")
else:
    print(f"Individual return: {R:.2f} $ (not yet profitable)")

if payback is None:
    print("Payback: not achievable under current conditions")
else:
    print(f"Payback time: {payback:.2f} years")

print(f"Total city return: {R_city:.2f} $")
