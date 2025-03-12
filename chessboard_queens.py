def count_queen_placements(board):
    def solve(row):
        if row == 8:
            return 1  # A valid configuration found
        count = 0
        for col in range(8):
            if col in col_used or (row - col) in diag1 or (row + col) in diag2 or board[row][col] == '*':
                continue  # Skip if column/diagonal is attacked or cell is reserved
            
            # Place queen
            col_used.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            count += solve(row + 1)  # Recur for next row
            
            # Remove queen (backtrack)
            col_used.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
        return count
    
    col_used, diag1, diag2 = set(), set(), set()
    return solve(0)

# Read input
board = [input().strip() for _ in range(8)]
print(count_queen_placements(board))