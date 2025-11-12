import numpy as np
import os

def solve_game():
    # Inputs
    # read dimensions
    r, c = map(int, input().split())

    # dimensions check
    if r < 2 or c < 2 or r * c > 10**4:
        print("Invalid dimensions")
        return

    rows = []
    for _ in range(r):
        # read a row; if a blank line is encountered, read the next one
        s = input().strip()
        while s == "":
            s = input().strip()

        # support two formats:
        # - contiguous digits ("1122") -> split into ['1','1','2','2']
        # - space-separated ("1 1 2 2") -> split() -> ['1','1','2','2']
        row = list(s) if ' ' not in s else s.split()

        # ensure the row has exactly c values
        if len(row) != c:
            print(f"Expected {c} values per row but got {len(row)}")
            return

        # ensure tokens are digits (integers)
        for x in row:
            if not x.isdigit():
                print("All colors must be integers")
                return

        # convert strings to ints and append
        rows.append([int(x) for x in row])

    # valid color set (1..8)
    valid = set(range(1, 9))

    # validate colors using a helper; helper returns the first bad value or None
    bad = validate_colors(rows, valid)
    if bad is not None:
        print("Colors need to be between 1 and 8")
        print(bad)
        return

    # Only rotate if matrix is square and has proper dimensions
    if r == c and r >= 2:
        try:
            rows = inverse_matrix(rows)
        except ValueError as e:
            print(f"Matrix rotation failed: {e}")
            return

    # print the rows in matrix form
    for rrow in rows:
        print(' '.join(str(v) for v in rrow))
    remove_cells = (get_connected_colors(rows, 3, 3))
    input(f"Press Enter to remove these cells {remove_cells}")
    os.system("cls")
    remove_logic(remove_cells, rows)
    for rrow in rows:
        print(' '.join(str(v) for v in rrow))
    ## Time to solve
    

def game_score(number_of_cells):
    # Calculate the score based on the current state of the game
    total_points = (number_of_cells-1)**2
    return total_points

def output_game(total_points, moves, removed_cells, removed_cells_positions):
    print("Total Points:", total_points)
    print("Total moves:", moves)
    print("Removed Cells:", removed_cells)
    for i, j in removed_cells_positions:
        print(i, j)

def validate_colors(rows, valid_set):
    for rrow in rows:
        for v in rrow:
            if v not in valid_set:
                return v
    return None



def remove_logic(curr_removed_cells, matrix):
    for i in matrix:
        for j in range(len(i)):
            if (matrix.index(i), j) in curr_removed_cells:
                #i[j] = None
                i.pop(j)

def get_connected_colors(rows, x, y): # color is a 1-8, rows is the graph
    visited = [[False for _ in range(len(rows[0]))] for _ in range(len(rows))]
    
    color = rows[y][x]
    found_colors = []

    def dfs(r, c):
        if r < 0 or r >= len(rows) or c < 0 or c >= len(rows[0]):
            return 0
        if visited[r][c] or rows[r][c] != color:
            return 0
        
        visited[r][c] = True
        curr_cell = (r, c)
        found_colors.append(curr_cell)

        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)

    dfs(x, y)
    return found_colors
    



def inverse_matrix(matrix):
    # Rotate the matrix by 180 degrees so top-left becomes bottom-right.
    # Returns a new list-of-lists with integer entries.
    
    # Validate input is rectangular
    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Input must be a non-empty rectangular matrix")
    
    # Note, do not reverse the order as we are supposed to search bottom left, not bottom right
    # Reverse the order of rows, and reverse each row
    rotated = [row[::1] for row in matrix[::-1]]

    # Ensure elements are ints
    try:
        rotated = [[int(x) for x in row] for row in rotated]
    except Exception as e:
        raise ValueError(f"Non-integer matrix elements: {e}")

    return rotated

def transpose_matrix(matrix):
    # Transpose the matrix(swap rows and columsns)
    matrix = [list(row) for row in zip(*matrix)]
    return matrix


def remove_column_logic(matrix): 
    # Identify columns to remove (columns where every entry is None)
    if not matrix:
        return []

    n_cols = len(matrix[0])
    columns_to_remove = set()
    for i in range(n_cols):  # for each column
        all_none = True
        for j in range(len(matrix)):
            if matrix[j][i] is not None:
                all_none = False
                break
        if all_none:
            columns_to_remove.add(i)

    # If nothing to remove, return a shallow copy of the original matrix
    if not columns_to_remove:
        return [row[:] for row in matrix]

    # Build and return a new matrix excluding the columns in columns_to_remove
    cols_keep = [k for k in range(n_cols) if k not in columns_to_remove]
    new_matrix = []
    for row in matrix:
        new_row = [row[k] for k in cols_keep]
        new_matrix.append(new_row)

    return new_matrix


    # parts that need to be implemented:
    # 1. Remove logic; this includes what is allowed to be removed and 
    #    removing from the matrix, then updating the matrix cells like in 
    #    the game
    # 2. output; this includes how to output the results of the game in its format
    # 3. Input validation; this includes checking if the input is valid for other peoples inputs and implementation

if __name__ == "__main__":
    solve_game()
