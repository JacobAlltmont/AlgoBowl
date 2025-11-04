
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
    # for rrow in rows:
    #     print(' '.join(str(v) for v in rrow))


def validate_colors(rows, valid_set):
    for rrow in rows:
        for v in rrow:
            if v not in valid_set:
                return v
    return None

if __name__ == "__main__":
    solve_game()