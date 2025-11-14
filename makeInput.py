import random

rows, cols = 10, 25

with open(f"input{rows}x{cols}.txt", "w") as f:
    f.write(f"{rows} {cols}\n")
    for _ in range(rows):
        if _ % 2 == 1:
            line = "".join(str(random.randint(1, 4)) for _ in range(cols))
        else:
            line = "".join(str(random.randint(5, 8)) for _ in range(cols))
        f.write(line + "\n")
        #f.write(line)

print(f"input{rows}x{cols}.txt created.")
