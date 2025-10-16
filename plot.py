import csv

import matplotlib.pyplot as plt
import numpy as np

x = []
err_quake = []
err_c = []

with open("errors.csv", "r", encoding="utf-16", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        x.append(float(row["x"].strip()))
        err_quake.append(float(row["err_quake"].strip()))
        err_c.append(float(row["err_sqrtf"].strip()))

x = np.array(x)
err_quake = np.array(err_quake)
err_c = np.array(err_c)

order = np.argsort(x)
x = x[order]
err_quake = err_quake[order]
err_c = err_c[order]

print(
    f"{'Algorithm':<12}  | {'Max Rel Error':<12} | {'Min Rel Error':<12}\n"
    f"{'-'*13} | {'-'*13} | {'-'*13}\n"
    f"{'Quake':<12}  | {np.max(err_quake):^13.2e} | {np.min(err_quake):^13.2e}\n"
    f"{'-'*13} | {'-'*13} | {'-'*13}\n"
    f"{'1.0f/sqrtf(x)':<12} | {np.max(err_c):^13.2e} | {np.min(err_c):^13.2e}"
)

plt.figure()
plt.plot(x, err_quake, label="Quake III Q_rsqrt")
plt.plot(x, err_c, label="C 1.0f/sqrtf(x)")
plt.xscale("linear")
plt.yscale("log")
plt.xlabel("x (floating point input values to the inverse square root)")
plt.ylabel("Relative error against C's 1.0/sqrt(x) (double precision) (log scale)")
plt.title("Comparison of relative error of inverse square root approximations")
plt.legend()
plt.tight_layout()
plt.savefig("errors.png", dpi=300)
plt.show()
