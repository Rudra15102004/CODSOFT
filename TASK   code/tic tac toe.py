import pygame, sys
import numpy as np

pygame.init()

# Game Settings
W, H = 600, 600
ROWS, COLS = 3, 3
SQ_SIZE = W // COLS
RADIUS = 60
CIRCLE_W = 15
CROSS_W = 20
GAP = 55

# Colors
BG = (28, 170, 156)
LINES = (0, 0, 0)
CIRCLE = (239, 231, 200)
CROSS = (66, 66, 66)
WIN_LINE = (250, 250, 250)
TEXT = (255, 255, 255)

# Pygame Setup
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG)
FONT = pygame.font.SysFont("arial", 48)

# Game Variables
board = np.zeros((ROWS, COLS))
turn = 1
end = False
who_won = 0

# Draw Grid Lines
def lines():
    for i in range(1, ROWS):
        pygame.draw.line(screen, LINES, (0, i * SQ_SIZE), (W, i * SQ_SIZE), 5)
        pygame.draw.line(screen, LINES, (i * SQ_SIZE, 0), (i * SQ_SIZE, H), 5)

# Draw Moves
def draw():
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == 1:
                pygame.draw.circle(screen, CIRCLE, (j * SQ_SIZE + SQ_SIZE // 2,
                                                    i * SQ_SIZE + SQ_SIZE // 2),
                                                    RADIUS, CIRCLE_W)
            elif board[i][j] == 2:
                pygame.draw.line(screen, CROSS, (j * SQ_SIZE + GAP, i * SQ_SIZE + GAP),
                                 (j * SQ_SIZE + SQ_SIZE - GAP, i * SQ_SIZE + SQ_SIZE - GAP), CROSS_W)
                pygame.draw.line(screen, CROSS, (j * SQ_SIZE + GAP, i * SQ_SIZE + SQ_SIZE - GAP),
                                 (j * SQ_SIZE + SQ_SIZE - GAP, i * SQ_SIZE + GAP), CROSS_W)

# Game Mechanics
def is_open(i, j): return board[i][j] == 0
def full(): return not np.any(board == 0)

# Mark Move
def mark(i, j, val): board[i][j] = val

# Check Win
def check(val):
    for i in range(ROWS):
        if np.all(board[i, :] == val):
            h_line(i, val)
            return True
    for j in range(COLS):
        if np.all(board[:, j] == val):
            v_line(j, val)
            return True
    if np.all(np.diag(board) == val):
        d_line(val)
        return True
    if np.all(np.diag(np.fliplr(board)) == val):
        ad_line(val)
        return True
    return False

# Drawing Win Lines
def v_line(j, val):
    col = CIRCLE if val == 1 else CROSS
    x = j * SQ_SIZE + SQ_SIZE // 2
    pygame.draw.line(screen, col, (x, 15), (x, H - 15), 10)

def h_line(i, val):
    col = CIRCLE if val == 1 else CROSS
    y = i * SQ_SIZE + SQ_SIZE // 2
    pygame.draw.line(screen, col, (15, y), (W - 15, y), 10)

def d_line(val):
    col = CIRCLE if val == 1 else CROSS
    pygame.draw.line(screen, col, (15, 15), (W - 15, H - 15), 10)

def ad_line(val):
    col = CIRCLE if val == 1 else CROSS
    pygame.draw.line(screen, col, (15, H - 15), (W - 15, 15), 10)

# Winner Check for AI
def result(bd):
    for i in range(ROWS):
        if np.all(bd[i, :] == 1): return 1
        if np.all(bd[i, :] == 2): return 2
    for j in range(COLS):
        if np.all(bd[:, j] == 1): return 1
        if np.all(bd[:, j] == 2): return 2
    if np.all(np.diag(bd) == 1) or np.all(np.diag(np.fliplr(bd)) == 1): return 1
    if np.all(np.diag(bd) == 2) or np.all(np.diag(np.fliplr(bd)) == 2): return 2
    return 0

# Minimax Logic
def minimax(bd, d, isMax):
    r = result(bd)
    if r == 2: return 1
    if r == 1: return -1
    if full(): return 0

    if isMax:
        maxEval = -np.inf
        for x in range(ROWS):
            for y in range(COLS):
                if bd[x][y] == 0:
                    bd[x][y] = 2
                    score = minimax(bd, d+1, False)
                    bd[x][y] = 0
                    maxEval = max(maxEval, score)
        return maxEval
    else:
        minEval = np.inf
        for x in range(ROWS):
            for y in range(COLS):
                if bd[x][y] == 0:
                    bd[x][y] = 1
                    score = minimax(bd, d+1, True)
                    bd[x][y] = 0
                    minEval = min(minEval, score)
        return minEval

# AI Turn
def ai_turn():
    maxScore = -np.inf
    bestMove = None
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == 0:
                board[i][j] = 2
                s = minimax(board, 0, False)
                board[i][j] = 0
                if s > maxScore:
                    maxScore = s
                    bestMove = (i, j)
    if bestMove:
        mark(bestMove[0], bestMove[1], 2)
        draw()
        return check(2)
    return False

# Game Over Message
def show(text):
    label = FONT.render(text, True, TEXT)
    rect = label.get_rect(center=(W // 2, H // 2))
    screen.blit(label, rect)

# Reset Game
def again():
    screen.fill(BG)
    lines()
    global board, turn, end, who_won
    board = np.zeros((ROWS, COLS))
    turn = 1
    end = False
    who_won = 0

# Start
lines()

while True:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not end:
            if turn == 1 and evt.type == pygame.MOUSEBUTTONDOWN:
                mx, my = evt.pos
                r, c = my // SQ_SIZE, mx // SQ_SIZE

                if is_open(r, c):
                    mark(r, c, 1)
                    draw()
                    if check(1):
                        who_won = 1
                        end = True
                    elif full():
                        end = True
                    else:
                        turn = 2

            if turn == 2 and not end:
                pygame.time.wait(300)
                if ai_turn():
                    who_won = 2
                    end = True
                elif full():
                    end = True
                else:
                    turn = 1

        if end:
            if who_won == 1:
                show("You Win!")
            elif who_won == 2:
                show("AI Wins!")
            else:
                show("Draw!")

        if evt.type == pygame.KEYDOWN and evt.key == pygame.K_r:
            again()

    pygame.display.update()
