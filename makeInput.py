import random

rows, cols = 90, 90

with open("input90x90.txt", "w") as f:
    f.write(f"{rows} {cols}\n")
    for _ in range(rows):
        line = "".join(str(random.randint(1, 8)) for _ in range(cols))
        f.write(line + "\n")

print("input90x90.txt created.")
