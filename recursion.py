import time
start_time = time.time()

def solveNQueens(n: int):
    col = set()
    posDiag = set()
    negDiag = set()

    res=[]
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = "Q "

            backtrack(r+1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = ". "
    backtrack(0)
    return res, len(res)

n = 11
res, solution = solveNQueens(n)
for i in range(solution):
    b = res[i]
    for j in range(n):
        print(b[j])
    print("")
print("Input :",n)
print("Number of Solution(s) : ",solution)
print("--- %s seconds ---" % (time.time() - start_time))
