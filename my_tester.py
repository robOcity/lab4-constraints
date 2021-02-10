from constraint_api import *
from lab4 import solve_constraint_dfs

# test 14
from test_problems import triangle_problem, triangle_problem_soln

expected = (triangle_problem_soln.assignments, 15)

result = solve_constraint_dfs(triangle_problem)
print(f"actual: {result}")
print(f"expected: {expected}")

# Hint: Look at search.py, specifically the Edge and UndirectedGraph classes.  Path are lists of vertices connected by edges.  Edges have length.  Graphs have a get_edge method.  Iterate over the edges in the path and add up the lengths.  Hope this helps!
