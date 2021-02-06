from constraint_api import *
from test_problems import get_pokemon_problem
from lab4 import solve_constraint_dfs


# test 16
solve_constraint_dfs_2_expected = (
    {"Q1": "B", "Q3": "D", "Q2": "B", "Q5": "C", "Q4": "C"},
    20,
)

result = solve_constraint_dfs(get_pokemon_problem())
print(result)
