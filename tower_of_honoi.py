def hanoi(n, from_peg, to_peg, aux_peg, moves):
    if n == 1:
        moves.append((from_peg, to_peg))
        return
    hanoi(n - 1, from_peg, aux_peg, to_peg, moves)
    moves.append((from_peg, to_peg))
    hanoi(n - 1, aux_peg, to_peg, from_peg, moves)

def solve_hanoi(n):
    moves = []
    hanoi(n, 1, 3, 2, moves)
    print(len(moves))
    for move in moves:
        print(move[0], move[1])

# Read input
n = int(input())
solve_hanoi(n)
