import numpy as np

original_graph = []

score = 0
moves = 0

def check_inputs():
    score = map(int, input())
    moves = map(int, input())

def check_move():
    moves -= 1
    c, n, x, y = map(int, input().split())
    score -= (n-1)^2



if __name__ == "__main__":
    solve_game()
