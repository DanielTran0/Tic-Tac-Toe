# Two Player Tic Tac Toe
from turtle import onscreenclick, listen, onkey, mainloop, bye, Screen, Turtle, clearscreen


def main():
    main_screen()
    game_board()
    game = Game()
    onscreenclick(game.player_move, 1)
    listen()
    onkey(game.restart, "space")
    onkey(bye, "Escape")
    mainloop()


# Create main screen for the game
def main_screen():
    screen = Screen()
    screen.title('Tic Tac Toe')
    screen.setup(1200, 1200)
    screen.setworldcoordinates(0, 0, 1200, 1200)
    return screen


# Base turtle used for drawing everything
def turtle():
    t = Turtle()
    t.pensize(10)
    t.speed(0)
    t.ht()
    return t


# Draw vertical or horizontal line for game board
def draw_line(pos_x_y, line, colour):
    t = turtle()
    t.color(colour)
    t.up()
    t.goto(pos_x_y[0], pos_x_y[1])
    t.down()
    if line == 'v':
        t.seth(90)
        t.forward(1000)
    elif line == 'h':
        t.seth(0)
        t.forward(1200)
    elif line == 'r':
        t.seth(0)
        t.left(40)
        t.forward(1500)
    elif line == 'l':
        t.seth(0)
        t.left(140)
        t.forward(1500)


# Create game board
def game_board():
    for i in range(400, 900, 400):
        draw_line((i, 0), 'v', 'black')
    for i in range(333, 700, 333):
        draw_line((0, i), 'h', 'black')
    t = turtle()
    t.up()
    t.goto(600, 1100)
    t.down()
    t.write("Player 1's Turn", False, align='center', font=('arial', 30, ''))


# Draw circle or x depending on player turn
def draw(true, x, y):
    if true:
        draw_circle(x, y)
    else:
        draw_x(x, y)


# Draw circle for first player
def draw_circle(x, y):
    t = turtle()
    t.pencolor('indigo')
    t.up()
    t.goto(x, y - 100)
    t.down()
    t.circle(100)


# Draw x for second player
def draw_x(x, y):
    t = turtle()
    t.color('red')
    t.up()
    t.goto(x - 70.7, y - 70.7)
    t.down()
    t.left(45)
    t.forward(200)
    t.left(-45)
    t.up()
    t.forward(-141.4)
    t.down()
    t.left(-45)
    t.forward(200)


# Write who's turn it is
def draw_player_turn(turn, over):
    t = turtle()
    t.up()
    t.goto(600, 1100)
    t.down()
    if turn and not over[0]:
        erase_write()
        t.write("Player 1's Turn", False, align='center', font=('arial', 30, ''))
    elif not turn and not over[0]:
        erase_write()
        t.write("Player 2's Turn", False, align='center', font=('arial', 30, ''))


# Erase writing
def erase_write():
    t = turtle()
    t.color('white')
    t.seth(0)
    t.up()
    t.goto(0, 1100)
    t.down()
    t.pensize(100)
    t.forward(1000)


#  Check for any winner
def winner(state, over, counter):
    t = turtle()
    t.up()
    t.goto(600, 1100)
    t.down()

    if not over[0]:
        for c in range(1, 10, 3):
            if state[c][1] == 1 and state[c+1][1] == 1 and state[c+2][1] == 1:
                over[0] = True
                over[1] = 1
                erase_write()
                t.write("Player 1 Wins", False, align='center', font=('arial', 30, ''))
                if c == 1:
                    draw_line((0, 166), 'h', 'blue')
                else:
                    draw_line((0, 166 + 333 * (c / 2.2 - 1)), 'h', 'blue')
            elif state[c][1] == 2 and state[c+1][1] == 2 and state[c+2][1] == 2:
                over[0] = True
                over[1] = 1
                erase_write()
                t.write("Player 2 Wins", False, align='center', font=('arial', 30, ''))
                if c == 1:
                    draw_line((0, 166), 'h', 'black')
                else:
                    draw_line((0, 166 + 333 * (c / 2.2 - 1)), 'h', 'blue')

        for c in range(1, 4):
            if state[c][1] == 1 and state[c+3][1] == 1 and state[c+6][1] == 1:
                over[0] = True
                over[1] = 1
                erase_write()
                t.write("Player 1 Wins", False, align='center', font=('arial', 30, ''))
                draw_line((200 + 400 * (c - 1), 0), 'v', 'blue')
            elif state[c][1] == 2 and state[c+3][1] == 2 and state[c+6][1] == 2:
                over[0] = True
                over[1] = 1
                erase_write()
                t.write("Player 2 Wins", False, align='center', font=('arial', 30, ''))
                draw_line((200 + 400 * (c - 1), 0), 'v', 'blue')

        if state[1][1] == 1 and state[5][1] == 1 and state[9][1] == 1:
            over[0] = True
            over[1] = 1
            erase_write()
            t.write("Player 1 Wins", False, align='center', font=('arial', 30, ''))
            draw_line((0, 0), 'r', 'blue')
        elif state[3][1] == 1 and state[5][1] == 1 and state[7][1] == 1:
            over[0] = True
            over[1] = 1
            erase_write()
            t.write("Player 1 Wins", False, align='center', font=('arial', 30, ''))
            draw_line((1200, 0), 'l', 'blue')
        elif state[1][1] == 2 and state[5][1] == 2 and state[9][1] == 2:
            over[0] = True
            over[1] = 1
            erase_write()
            t.write("Player 2 Wins", False, align='center', font=('arial', 30, ''))
            draw_line((0, 0), 'r', 'blue')
        elif state[3][1] == 2 and state[5][1] == 2 and state[7][1] == 2:
            over[0] = True
            over[1] = 1
            erase_write()
            t.write("Player 2 Wins", False, align='center', font=('arial', 30, ''))
            draw_line((1200, 0), 'l', 'blue')
    if not over[0] and counter == 9:
        erase_write()
        t.write("Tie Game", False, align='center', font=('arial', 30, ''))
        over[0] = True
    if over[0]:
        t.up()
        t.goto(200, 1150)
        t.write("Space bar to play again", False, align='center', font=('arial', 20, ''))
        t.up()
        t.goto(1000, 1150)
        t.write("Esc to quit", False, align='center', font=('arial', 20, ''))


# Divide the board and alternate player turns
class Game:
    def __init__(self):
        self.game_over = [False, 0]
        self.board_location = {
            1: [(0, 0), (400, 333)],
            2: [(401, 0), (800, 333)],
            3: [(801, 0), (1200, 333)],
            4: [(0, 334), (400, 666)],
            5: [(401, 334), (800, 666)],
            6: [(801, 334), (1200, 666)],
            7: [(0, 667), (400, 1000)],
            8: [(401, 667), (800, 1000)],
            9: [(801, 667), (1200, 1000)]
        }
        self.board_state = {
            1: [False, 0],
            2: [False, 0],
            3: [False, 0],
            4: [False, 0],
            5: [False, 0],
            6: [False, 0],
            7: [False, 0],
            8: [False, 0],
            9: [False, 0]
        }
        self.board_counter = 0
        self.player_turn = True

    def player_move(self, x, y):
        if not self.game_over[0]:
            for i in self.board_location:
                if self.board_location[i][0][0] <= x <= self.board_location[i][1][0] and \
                   self.board_location[i][0][1] <= y <= self.board_location[i][1][1] and not self.board_state[i][0]:
                    self.board_state[i][0] = True
                    draw(self.player_turn, x, y)
                    if self.player_turn:
                        self.board_state[i][1] = 1
                    else:
                        self.board_state[i][1] = 2
                    self.player_turn = not self.player_turn
                    self.board_counter += 1
                    winner(self.board_state, self.game_over, self.board_counter)
                    if self.board_counter < 9:
                        draw_player_turn(self.player_turn, self.game_over)

    def restart(self):
        clearscreen()
        main()


if __name__ == '__main__':
    main()
