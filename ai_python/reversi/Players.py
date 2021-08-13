from random import randint
from copy import deepcopy
import time


class RandomPlayer:
    def __init__(self, player_number, name="Random"):
        self.__player_number = player_number
        self.__name = name

    def __str__(self):
        return self.__name

    def select_square(self, gameboard, time_left=-1):
        possible_moves = gameboard.get_current_moves(self.__player_number)
        # print("Random player's possible moves are {}".format(possible_moves))
        if len(possible_moves) == 0:
            return None
        r = randint(0, len(possible_moves)-1)
        # print("---and selected {}".format(possible_moves[r]))
        return possible_moves[r]


class Human:
    def __init__(self, player_number, name="Human"):
        self.__player_number = player_number
        self.__name = name

    def select_square(self, gameboard, time_limit=-1):
        print(gameboard)
        possible_moves = gameboard.get_current_moves(self.__player_number)
        for i, v in enumerate(possible_moves):
            print("{}) {}".format(i, v))
        x = int(input("Enter selection: "))
        return possible_moves[x]

    def __str__(self):
        return self.__name


class AIAgent:
    def __init__(self, player_number, name=None):
        self.__player_number = player_number
        self.__name = name

    def __str__(self):
        return self.__name

    def select_square(self, gameboard, time_limit=-1):
        start_time = time.perf_counter()
        count = gameboard.count_pieces()
        depth = 3
        if 8 < count[0] < 48:
            depth = 2
        elif 4 < count[0] <= 8 or 48 <= count[0] < 56:
            depth = 3
        move, _ = self.__minmax(gameboard, depth, start_time=start_time, time_limit=time_limit)
        while time.perf_counter() - start_time < time_limit:
            depth += 1
            if time.perf_counter() - start_time >= time_limit - .35:
                return move
            move, _ = self.__minmax(gameboard, depth, start_time=start_time, time_limit=time_limit, epsilon=0.22)

        return move

    def __eval_fn(self, gameboard):
        pieces = gameboard.count_pieces()
        if self.__player_number == 1:
            return pieces[2]-pieces[3]
        return pieces[3]-pieces[2]

    def __utility(self, gameboard):
        winner = gameboard.find_winner()
        if winner == -1:
            return self.__eval_fn(gameboard)
        elif winner == 0:
            return 0
        elif winner == 1 and self.__player_number == 1:
            return float("inf")
        elif winner == 2 and self.__player_number == 2:
            return float("inf")
        else:
            return float("-inf")

    def __minmax(self, gameboard, depth=float("inf"), maximizing_player=True, start_time=0.0, time_limit=0, epsilon=0.1):
        if depth == 0:
            return None, self.__utility(gameboard)
        #max
        if maximizing_player:
            moves = gameboard.get_current_moves(self.__player_number)
            if len(moves) == 0:
                return None, 0
            if time.perf_counter() - start_time >= time_limit - epsilon:
                return moves[randint(0, len(moves)-1)], 0

            max_move = moves[0]
            max_val = float("-inf")
            for move in moves:
                gb_copy = deepcopy(gameboard)
                gb_copy.update_board(move, self.__player_number)
                result = self.__minmax(gb_copy, depth-1, not maximizing_player, start_time, time_limit, epsilon)[1]
                if 0 or 7 in move:
                    result += 20
                #print(result)
                if result > max_val:
                    max_val = result
                    max_move = move
            return max_move, max_val
        else:
            other_player = 1 if self.__player_number == 2 else 2
            moves = gameboard.get_current_moves(other_player)
            if len(moves) == 0:
                return None, 0
            if time.perf_counter() - start_time >= time_limit - epsilon:
                return moves[randint(0, len(moves)-1)], 0

            min_move = moves[0]
            min_val = float("inf")
            for move in moves:
                gb_copy = deepcopy(gameboard)
                gb_copy.update_board(move, other_player)
                result = self.__minmax(gb_copy, depth-1, not maximizing_player, start_time, time_limit, epsilon)[1]

                #print(result)
                if result < min_val:
                    min_val = result
                    min_move = move
            return min_move, min_val

    def __alphabeta(self, board, depth=float("inf"), maximizing_player=True, alpha=float("-inf"), beta=float("inf")):
        pass