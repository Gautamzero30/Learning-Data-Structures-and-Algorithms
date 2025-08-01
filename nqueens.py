def solve_n_queens(n):
    def is_safe(row, col):
        return col not in cols and (row - col) not in diag1 and (row + col) not in diag2

    def backtrack(row, current):
        if row == n:
            result.append(current[:])
            return
        for col in range(n):
            if is_safe(row, col):
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                current.append("." * col + "Q" + "." * (n - col - 1))
                backtrack(row + 1, current)
                current.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

    result = []
    cols = set()
    diag1 = set()  # top-left to bottom-right
    diag2 = set()  # top-right to bottom-left
    backtrack(0, [])
    return result

# Example Usage
n = 4
solutions = solve_n_queens(n)
for i, sol in enumerate(solutions, 1):
    print(f"Solution {i}:")
    for row in sol:
        print(row)
    print()
