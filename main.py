import numpy as np

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

def remove_logic(curr_removed_cells, removed_cells, removed_cells_positions):
    # This function signature now takes and returns the accumulators so there
    # is no reliance on outer-scope variables.
    removed_cells += len(curr_removed_cells)
    removed_cells_positions += curr_removed_cells

    # Placeholder for removal logic
    # Implement actual removal/update logic specific to your game here

    return removed_cells, removed_cells_positions

def inverse_matrix(matrix):
    """
    Rotate the matrix by 180 degrees so top-left becomes bottom-right.
    Returns a new list-of-lists with integer entries.
    """
    # Validate input is rectangular
    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Input must be a non-empty rectangular matrix")

    # Simple Python implementation (no numeric inversion)
    # Reverse the order of rows, and reverse each row
    rotated = [row[::-1] for row in matrix[::-1]]

    # Ensure elements are ints
    try:
        rotated = [[int(x) for x in row] for row in rotated]
    except Exception as e:
        raise ValueError(f"Non-integer matrix elements: {e}")

    return rotated

if __name__ == "__main__":
    solve_game()
