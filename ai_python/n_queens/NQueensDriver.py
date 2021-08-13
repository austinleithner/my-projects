from NQueensStudentSolver import NQueensSolver
import time

N = 6
time_limit = 300
solver = NQueensSolver(N, time_limit)
solve_options = {#'Dumb Brute force': solver.attempt_with_brute_force_dumb,
         #'Smart Brute Force': solver.attempt_with_brute_force_smart,
         #'Inefficient Hill Climbing': solver.attempt_with_hill_climbing_dumb,
         #'More Efficient Hill Climbing': solver.attempt_with_hill_climb_smart,
         #'Stocastic Hill Climbing': solver.attempt_with_stocastich_hill_climb,
         'Random Restart Hill Climbing': solver.attempt_with_random_restart_hill_climbing,
         #'Simulated Annealing': solver.attempt_with_simulated_annealing,
         #'Genetic Algo': solver.attempt_with_genetic_algo,
         'My Best algo': solver.my_best_algo}

for k in solve_options.keys():
    st_time = time.perf_counter()
    solution = solve_options[k]()
    result = []
    if solution is not None:
        result = solution.get_state()
        ev = solution.eval_fn()
    end_time = time.perf_counter()
    print("Solution for {0} is {1} with eval fn of {3} in {2:.4f} seconds.".format(k, result, end_time-st_time, ev))
