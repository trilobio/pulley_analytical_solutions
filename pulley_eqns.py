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
AX, AY, BX, BY, ABX, ABY, CX, CY, BCX, BCY = sp.symbols(
    'AX, AY, BX, BY, ABX, ABY, CX, CY, BCX, BCY')

# Parameters
RAB, RBC, RCD, d, h = sp.symbols(
    'RAB, RBC, RCD, d, h')
params = [RAB, RBC, RCD, d, h]
vals = [0.555, 1, 0.15, 0.4, 0.75]
param_associations = list(zip(params, vals))

equations_1 = [
    AX + BX,
    AY - BY,
    ABX,
    ABY,
    BCX + d,
    (BX - ABX)**2 + (BY - ABY)**2 - RAB**2,
    (BX - BCX)**2 + (BY - BCY)**2 - RBC**2,
    CX - RBC + d,
    (BCY - ABY) / (BCX - ABX) - (ABY - BY) / (ABX - BX),
    CY - BCY,
    -RAB * d / (RAB - RBC) - BX,
    RAB * sp.sqrt(RAB**2 - 2 * RAB * RBC + RBC**2 - d**2) / (RAB - RBC) - BY,
]

res_1 = sp.solve(equations_1, AX, AY, BX, BY, ABX, ABY, CX,
                 CY, BCX, BCY, dict=True)[0]  # Assume exactly 1 solution, since the equations were tailored such that that is the case


# New Variables
CDX, CDY, DX, DY = sp.symbols("CDX, CDY, DX, DY")

# New Parameters
RCD, h = sp.symbols("RCD, h")

# Temporary variable for res_1[BCY]
L = sp.symbols("L")

equations_2 = [
    res_1[BCX] - BCX,
    L - BCY,
    (-RBC * d + RBC * sp.sqrt(-L**2 - 2 * L * RAB - 2 * L * RCD + 2 * L * h - RAB**2 - 2 * RAB *
     RCD + 2 * RAB * h + RBC**2 + 2 * RBC * RCD + 2 * RCD * h - h**2) - RCD * d) / (RBC + RCD) - CX,
    (L * RCD - RAB * RBC - RBC * RCD + RBC * h) / (RBC + RCD) - CY,
    (CX - BCX)**2 + (CY - BCY)**2 - RBC**2,
    (CX - CDX)**2 + (CY - CDY)**2 - RCD**2,
    DX - CDX,
    -RAB + h - DY,
    (BCX - CX) / (BCY - CY) - (CX - CDX) / (CY - CDY),
    DY - RCD - CDY
]

res_2 = sp.solve(equations_2, CX,
                 CY, BCX, BCY, DX, DY, CDX, CDY, dict=True)[0]

# Substitue L for res_1[BCY]
for key, val in res_2.items():
    res_2[key] = res_2[key].subs(L, res_1[BCY])

res_full = {**res_1, **res_2}

for key, val in res_full.items():
    res_full[key] = res_full[key].subs(param_associations)
print(res_full)
