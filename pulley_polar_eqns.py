"""This solves for the GT-2 and GT-3 pulley tooth profile analytically
using sympy. Solving for all variables at once doesn't tend to converge quickly,
so the solution is approached in two steps.

Step 1: Solve for BCX and BCY
Step 2: Solve for CDX and CDY

We create a dummy variable L for BCY in order to help sympy solve, and then
substitute the dummy variable after the solution is completed.
"""

import json
import sympy as sp


# Variables
AX, AY, BX, BY, ABX, ABY, BCX, BCY, RBXY = sp.symbols(
    'AX, AY, BX, BY, ABX, ABY, BCX, BCY, RBXY', real=True)

# Parameters
RAB, RBC, RCD, b, h, PLD, t, PD = sp.symbols(
    'RAB, RBC, RCD, b, h, PLD, t, PD')
params = [RAB, RBC, RCD, b, h, PLD, t, PD]
vals = [0.555, 1, 0.15, 0.4, 0.75, 0.254,
        10, 6.36619772368]
param_associations = list(zip(params, vals))

L = sp.symbols("L")
equations_1 = [
    AX + BX,
    AY - BY,
    ABX,
    L - ABY,
    RBXY * sp.sin(2 * b / PD) + BCX,
    RBXY * sp.cos(2 * b / PD) - BCY,
    sp.sqrt(BCX**2 + BCY**2) - RBXY,
    (BX - ABX)**2 + (BY - ABY)**2 - RAB**2,
    (BX - BCX)**2 + (BY - BCY)**2 - RBC**2,
    (BCY - ABY) / (BCX - ABX) - (ABY - BY) / (ABX - BX)
]

res_1 = sp.solve(equations_1, AX, AY, BX, BY, ABX,
                 ABY, BCX, BCY, RBXY, dict=True)[1]

for i, sol in enumerate([res_1]):
    print(f"\nSolution {i}")
    for key, val in sol.items():
        print(
            f"\t{key}: {val.subs(L, PD / 2 - PLD - h + RAB).subs(param_associations)}")

for i, sol in enumerate([res_1]):
    print(f"\nSolution {i}")
    for key, val in sol.items():
        print(
            f"\t{key}: {val}")
