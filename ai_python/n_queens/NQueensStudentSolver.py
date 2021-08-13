from NQueensWorld import NQueensWorld
import time
from random import randint, random
import math

class NQueensSolver:
    def __init__(self, N, time_limit=300):
        self.__N = N
        self.count = 0
        self.__time_limit = time_limit
        self.__start_time = None

    def attempt_with_brute_force_dumb(self):
        self.__start_time = time.perf_counter()
        best_world = None
        best_ev = float("inf")
        for i in range(10**self.__N):
            if time.perf_counter() - self.__start_time >= self.__time_limit:
                return best_world
            temp_state = [0 for _ in range(self.__N)]
            temp_i = i
            cnt = -1
            invalid = False
            while temp_i > 0 and not invalid:
                digit = temp_i % 10
                # if digit >= N:
                #     invalid = True
                temp_state[cnt] = temp_i % 10
                temp_i = temp_i // 10
                cnt -= 1
            # if len(set(temp_state)) != N:
            #     invalid = True
            if not invalid:
                # print(temp_state)
                try:
                    temp_world = NQueensWorld(self.__N, state=temp_state)
                    temp_ev = temp_world.eval_fn()
                    if temp_ev == 0:
                        print("found solution in {} seconds".format(time.perf_counter()-self.__start_time))
                        return temp_world
                    if temp_ev < best_ev:
                        best_world = temp_world
                        best_ev = temp_ev
                except ValueError:
                    pass
        return None

    def attempt_with_brute_force_smart(self):
        self.__start_time = time.perf_counter()
        for i in range(10**self.__N):
            if time.perf_counter() - self.__start_time >= self.__time_limit:
                raise TimeoutError("Ran out of time with i={}".format(i))
            temp_state = [0 for _ in range(self.__N)]
            temp_i = i
            cnt = -1
            invalid = False
            while temp_i > 0 and not invalid:
                digit = temp_i % 10
                if digit >= self.__N:
                    invalid = True
                temp_state[cnt] = temp_i % 10
                temp_i = temp_i // 10
                cnt -= 1
            if len(set(temp_state)) != self.__N:
                invalid = True
            if not invalid:
                # print(temp_state)
                try:
                    temp_world = NQueensWorld(self.__N, state=temp_state)
                    if temp_world.eval_fn() == 0:
                        # print("found solution in {} seconds".format(time.perf_counter()-start_time))
                        return temp_world
                except ValueError:
                    pass
        return None

    def attempt_with_hill_climbing_dumb(self, world=None, depth=0):
        if depth == 0:
            self.__start_time = time.perf_counter()
        if time.perf_counter() - self.__start_time >= self.__time_limit:
            raise TimeoutError("Ran out of time.")
        if world is None:
            world = NQueensWorld(self.__N)
        best_ev = world.eval_fn()
        next_states = world.get_one_move_next_states()
        i = 0
        better_world = None
        while i < self.__N and better_world is None:
            temp_world = NQueensWorld(state=next_states[i])
            if temp_world.eval_fn() < best_ev:
                better_world = temp_world
                best_ev = temp_world.eval_fn()
            i += 1
        if better_world is None:
            return world
        if best_ev == 0:
            return better_world
        return self.attempt_with_hill_climbing_dumb(better_world, depth+1)
            # print("--{} has eval fn of {}".format(next_state, temp_world.eval_fn()))
        # print("{} possible next states".format(len(next_states)))

    def attempt_with_hill_climb_smart(self, world=None, depth=0):
        if depth == 0:
            self.__start_time = time.perf_counter()
        if time.perf_counter() - self.__start_time >= self.__time_limit:
            raise TimeoutError("Ran out of time.")
        if world is None:
            world = NQueensWorld(self.__N)
        best_ev = world.eval_fn()
        next_states = world.get_one_move_next_states()
        #i = 0
        better_world = None
        next_world = []
        for states in next_states:
            next_world.append(NQueensWorld(N=self.__N, state=states))
        #print(next_states)
        next_world = sorted(next_world, reverse=True)
        #print(next_states)
        #print(best_ev)
        #min of next states
        #first elem is min
        temp_world = next_world[0]
        #temp_world = NQueensWorld(state=next_states[0])
        #print(temp_world.eval_fn())
        #check to see if peak has been reached
        if temp_world.eval_fn() < best_ev:
            better_world = temp_world
            best_ev = temp_world.eval_fn()
        #while i < len(next_states):
        #    temp_world = NQueensWorld(state=next_states[i])
        #    if temp_world.eval_fn() < best_ev:
        #        better_world = temp_world
        #        best_ev = temp_world.eval_fn()
        #    i += 1
        if better_world is None:
            return world
        if best_ev == 0:
            return better_world
        return self.attempt_with_hill_climb_smart(better_world, depth + 1)

    def attempt_with_stocastich_hill_climb(self, world=None, depth=0):
        if depth == 0:
            self.__start_time = time.perf_counter()
        if time.perf_counter() - self.__start_time >= self.__time_limit:
            raise TimeoutError("Ran out of time.")
        if world is None:
            world = NQueensWorld(self.__N)
        rand_eval = world.eval_fn()
        next_states = world.get_one_move_next_states()

        rand_world = None
        next_world = []
        for states in next_states:
            temp_world = NQueensWorld(N=self.__N, state=states)
            if temp_world.eval_fn() < rand_eval:
                next_world.append(temp_world)

        if len(next_world) > 0:
            rand_world = next_world[randint(0, len(next_world)-1)]
            rand_eval = rand_world.eval_fn()

        if rand_world is None:
            return world
        if rand_eval == 0:
            return rand_world
        return self.attempt_with_stocastich_hill_climb(rand_world, depth+1)

    def attempt_with_random_restart_hill_climbing(self):
        world = self.attempt_with_stocastich_hill_climb(NQueensWorld(N=self.__N, state=-1))
        while world.eval_fn() != 0:
            world = self.attempt_with_stocastich_hill_climb(NQueensWorld(N=self.__N, state=-1))
        return world

    def attempt_with_genetic_algo(self):
        self.__start_time = time.perf_counter()
        population_size = 30
        mid_point = self.__N // 2
        population = []

        generations = 0

        for _ in range(population_size):
            population.append(NQueensWorld(N=self.__N, state=-1))

        while time.perf_counter() - self.__start_time < self.__time_limit:
            for _ in range(population_size):
                parent1 = population[randint(0, population_size-1)].get_state()
                parent2 = population[randint(0, population_size-1)].get_state()
                child1 = NQueensWorld(state=parent1[:mid_point] + parent2[mid_point:])
                child2 = NQueensWorld(state=parent2[:mid_point] + parent1[mid_point:])
                if random() <= .80:
                    child1_state = child1.get_state()
                    child1_state[randint(0, self.__N - 1)] = randint(0, self.__N -1)
                    child1 = NQueensWorld(state=child1_state)
                    # print("------------------------------child1\n{}".format(child1))
                if random() <= .70:
                    child2_state = child2.get_state()
                    child2_state[randint(0, self.__N - 1)] = randint(0, self.__N -1)
                    child2 = NQueensWorld(state=child2_state)
                    # print("------------------------------child2\n{}".format(child1))
                population.append(child1)
                population.append(child2)
                # print("{} and {} make:\n--{}\n--{}".format(parent1, parent2, child1.get_state(), child2.get_state()))
            if generations >= 10:
                del(population[randint(0, len(population)//2)])
                population.append(NQueensWorld(N=self.__N, state=-1))
            population = sorted(population, reverse=True)
            for item in population:
                print("{} -> {}".format(item.get_state(), item.eval_fn()))
            population = population[:population_size]
            print("----------------------")
            for item in population:
                print("{} -> {}".format(item.get_state(), item.eval_fn()))
            if population[0].eval_fn() == 0:
                return population[0]

            generations += 1
        return population[0]

    def attempt_with_simulated_annealing(self):
        self.__start_time = time.perf_counter()
        current_world = NQueensWorld(N=self.__N, state=-1)
        while (time.perf_counter() - self.__start_time < self.__time_limit) and (current_world.eval_fn() != 0):
            #temp = self.exponential_temp(time.perf_counter())
            temp = self.asa_temp(time.perf_counter())

            next_states = current_world.get_one_move_next_states()
            if temp == 0:
                return current_world
            next_world = NQueensWorld(N=self.__N, state=next_states[randint(0, len(next_states)-1)])
            delta_e = next_world.eval_fn() - current_world.eval_fn()
            if delta_e < 0:
                current_world = next_world
            else:
                if math.exp(-(delta_e/temp)) >= random():
                    current_world = next_world

        return current_world

    def exponential_temp(self, t):
        #exponetial decrease init temp/t
        #init_temp = 30
        if t == 0:
            return float("inf")
        init_temp = self.__N
        return init_temp/t

    def asa_temp(self, t):
        #tempature function used from Adaptive Simulated Annealing
        #all credit goes to Lester Ingber <lester@ingber.com>
        #the function is used but not the ASA algorithm
        #init_temp = 30
        init_temp = 175
        dim = 2
        conv = 6
        return init_temp * math.exp(-conv*(t**(1/dim)))

    def my_best_algo(self):
        return self.attempt_with_simulated_annealing()
