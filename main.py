class game:
    def __init__(self):
        self.total_points = 0
        self.points = []
        self.moves = 0 
        self.removed_cells = 0
        self.removed_cell_info = [] 

    def solve_game(self):
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
            if not s:
                s = input().strip()

            # support two formats:
            # - contiguous digits ("1122") -> split into ['1','1','2','2']
            # - space-separated ("1 1 2 2") -> split() -> ['1','1','2','2']
            row = list(s) if ' ' not in s else s.split()

            # ensure the row has exactly c values
            if len(row) != c:
                print(f"Expected {c} values per row but got {len(row)}")
                return

            # ensure tokens are digits (integers) using an explicit for-loop
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

        # print the rows in matrix form
        for rrow in rows:
            print(' '.join(str(v) for v in rrow))

    def game_score(self, number_of_cells):
        # Calculate the score based on the current state of the game
        self.total_points = (number_of_cells-1)**2
        return self.total_points
    
    def output_game(self):
        print("Total Points:", self.total_points)
        print("Total moves:" self.moves)
        print("Removed Cells:", self.removed_cells)
        '''
        store using tuples
        '''
        for i,j in removed_cells_positions:
            print("{i},{j})

    def validate_colors(rows, valid_set):
        for rrow in rows:
            for v in rrow:
                if v not in valid_set:
                    return v
        return None



    def remove_logic(self, curr_removed_cells):
        self.removed_cells += len(curr_removed_cells)
        self.removed_cells_positions += curr_removed_cells

        # Removing cells from rows
        for i in len(curr_removed_cells): # i is a row, rows are arrays
            for j in len(i): # getting a single cell
                

        

    # parts that need to be implemented:
    # 1. Remove logic; this includes what is allowed to be removed and 
    #    removing from the matrix, then updating the matrix cells like in 
    #    the game
    # 2. point system; this includes how many points you get for removing 
    #    certain color combos/number of a color removed
    # 3. output; this includes how to output the results of the game in its format
    # 4. Making a reverse matrix so that the bottom left corner is (1,1)

    if __name__ == "__main__":
        solve_game()
