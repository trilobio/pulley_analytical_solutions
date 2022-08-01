# pulley_analytical_solutions

This solves for the GT-2 and GT-3 pulley tooth profile analytically
using sympy. The variables and pararmeters named in `pulley_eqns.py` are referenced in the diagram below. The parameters are RAB, RBC, RCD, d, h, P. All of the other named values are variables. The origin is at AB.

![Tooth Profile Diagram](/diagrams/pulley_eqns_diagram.png)

Solving for all variables at once doesn't tend to converge quickly,
so the solution is approached in two steps.

Step 1: Solve for BX, BY, BCX and BCY
Step 2: Solve for CX, CY, CDX, CDY, and DX
