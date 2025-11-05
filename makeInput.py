import random

rows, cols = 10, 10

with open(f"input{rows}x{cols}.txt", "w") as f:
    f.write(f"{rows} {cols}\n")
    for _ in range(rows):
        line = "".join(str(random.randint(1, 8)) for _ in range(cols))
        # f.write(line + "\n")
        f.write(line)

print(f"input{rows}x{cols}.txt created.")
