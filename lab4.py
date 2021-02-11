# MIT 6.034 Lab 4: Constraint Satisfaction Problems
# Written by 6.034 staff

from constraint_api import *
from test_problems import get_pokemon_problem


#### Part 1: Warmup ############################################################


def has_empty_domains(csp):
    """Returns True if the problem has one or more empty domains, otherwise False"""
    empty_domains = [
        len(csp.get_domain(v)) == 0 for v in csp.get_all_variables()
    ]
    return any(empty_domains)


def check_all_constraints(csp):
    """Return False if the problem's assigned values violate some constraint,
    otherwise True"""
    checked_constraints = [
        c.check(csp.get_assignment(c.var1), csp.get_assignment(c.var2))
        for c in csp.get_all_constraints()
        if c.var1 not in csp.unassigned_vars
        and c.var2 not in csp.unassigned_vars
    ]
    return all(checked_constraints)


#### Part 2: Depth-First Constraint Solver #####################################


def all_assigned(csp):
    """Returns True if all the csp values are assigned."""
    assignments = [csp.get_assignment(v) for v in csp.get_all_variables()]
    return all(assignments)


def solve_constraint_dfs(problem):
    """
    Solves the problem using depth-first search.  Returns a tuple containing:
    1. the solution (a dictionary mapping variables to assigned values)
    2. the number of extensions made (the number of problems popped off the agenda).
    If no solution was found, return None as the first element of the tuple.
    """
    # initialize
    solution, num_extensions, agenda = None, 0, []
    agenda.append(problem)

    while agenda:
        csp = agenda.pop()
        num_extensions += 1

        if check_all_constraints(csp) and all_assigned(csp):
            solution = {
                var: csp.get_assignment(var) for var in csp.get_all_variables()
            }
            return solution, num_extensions

        while unassigned_var := csp.pop_next_unassigned_var():
            for domain_val in csp.get_domain(unassigned_var):
                new_csp = csp.copy()
                new_csp.set_assignment(unassigned_var, domain_val)
                if not has_empty_domains(new_csp):
                    agenda.append(new_csp)

    return solution, num_extensions


# QUESTION 1: How many extensions does it take to solve the Pokemon problem
#    with DFS?

# Hint: Use get_pokemon_problem() to get a new copy of the Pokemon problem
#    each time you want to solve it with a different search method.

ANSWER_1 = None


#### Part 3: Forward Checking ##################################################


def eliminate_from_neighbors(csp, var):
    """
    Eliminates incompatible values from var's neighbors' domains, modifying
    the original csp.  Returns an alphabetically sorted list of the neighboring
    variables whose domains were reduced, with each variable appearing at most
    once.  If no domains were reduced, returns empty list.
    If a domain is reduced to size 0, quits immediately and returns None.
    """
    raise NotImplementedError


# Because names give us power over things (you're free to use this alias)
forward_check = eliminate_from_neighbors


def solve_constraint_forward_checking(problem):
    """
    Solves the problem using depth-first search with forward checking.
    Same return type as solve_constraint_dfs.
    """
    raise NotImplementedError


# QUESTION 2: How many extensions does it take to solve the Pokemon problem
#    with DFS and forward checking?

ANSWER_2 = None


#### Part 4: Domain Reduction ##################################################


def domain_reduction(csp, queue=None):
    """
    Uses constraints to reduce domains, propagating the domain reduction
    to all neighbors whose domains are reduced during the process.
    If queue is None, initializes propagation queue by adding all variables in
    their default order.
    Returns a list of all variables that were dequeued, in the order they
    were removed from the queue.  Variables may appear in the list multiple times.
    If a domain is reduced to size 0, quits immediately and returns None.
    This function modifies the original csp.
    """
    raise NotImplementedError


# QUESTION 3: How many extensions does it take to solve the Pokemon problem
#    with DFS (no forward checking) if you do domain reduction before solving it?

ANSWER_3 = None


def solve_constraint_propagate_reduced_domains(problem):
    """
    Solves the problem using depth-first search with forward checking and
    propagation through all reduced domains.  Same return type as
    solve_constraint_dfs.
    """
    raise NotImplementedError


# QUESTION 4: How many extensions does it take to solve the Pokemon problem
#    with forward checking and propagation through reduced domains?

ANSWER_4 = None


#### Part 5A: Generic Domain Reduction #########################################


def propagate(enqueue_condition_fn, csp, queue=None):
    """
    Uses constraints to reduce domains, modifying the original csp.
    Uses enqueue_condition_fn to determine whether to enqueue a variable whose
    domain has been reduced. Same return type as domain_reduction.
    """
    raise NotImplementedError


def condition_domain_reduction(csp, var):
    """Returns True if var should be enqueued under the all-reduced-domains
    condition, otherwise False"""
    raise NotImplementedError


def condition_singleton(csp, var):
    """Returns True if var should be enqueued under the singleton-domains
    condition, otherwise False"""
    raise NotImplementedError


def condition_forward_checking(csp, var):
    """Returns True if var should be enqueued under the forward-checking
    condition, otherwise False"""
    raise NotImplementedError


#### Part 5B: Generic Constraint Solver ########################################


def solve_constraint_generic(problem, enqueue_condition=None):
    """
    Solves the problem, calling propagate with the specified enqueue
    condition (a function). If enqueue_condition is None, uses DFS only.
    Same return type as solve_constraint_dfs.
    """
    raise NotImplementedError


# QUESTION 5: How many extensions does it take to solve the Pokemon problem
#    with forward checking and propagation through singleton domains? (Don't
#    use domain reduction before solving it.)

ANSWER_5 = None


#### Part 6: Defining Custom Constraints #######################################


def constraint_adjacent(m, n):
    """Returns True if m and n are adjacent, otherwise False.
    Assume m and n are ints."""
    raise NotImplementedError


def constraint_not_adjacent(m, n):
    """Returns True if m and n are NOT adjacent, otherwise False.
    Assume m and n are ints."""
    raise NotImplementedError


def all_different(variables):
    """Returns a list of constraints, with one difference constraint between
    each pair of variables."""
    raise NotImplementedError


#### SURVEY ####################################################################

NAME = None
COLLABORATORS = None
HOW_MANY_HOURS_THIS_LAB_TOOK = None
WHAT_I_FOUND_INTERESTING = None
WHAT_I_FOUND_BORING = None
SUGGESTIONS = None
