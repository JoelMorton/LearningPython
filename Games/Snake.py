import tkinter
import random

window = tkinter.Tk()
# window.geometry("303x340")
window.geometry("400x400")
window.resizable(0,0)
window.title("Snake")


# functions
def start():
    # start the game
    tkinter.Label(window, text="Hi").pack()

def draw_board():
    # fill with greenspace
    for x in range(board_height):
        for y in range(board_width):
            rect = canvas.create_rectangle(25 * x, 25 * y, 25 * (x + 1), 25 * (y + 1), fill='black')
            # if board[x][y] == 1:
            #     color = 'blue'
            # else:
            #     color = 'green'
            # rect = canvas.create_rectangle(25*x, 25*y, 25*(x+1), 25*(y+1), fill=color)

    # fill in the snake
    length = len(snake)
    for x in range(length):
        rect = canvas.create_rectangle(25 * snake[x][0], 25 * snake[x][1], 25 * (snake[x][0] + 1), 25 * (snake[x][1] + 1), fill='brown')

    rect = canvas.create_rectangle(25 * apple[0],25 * apple[1],25 * apple[0] + 25,25 * apple[1] + 25, fill='green')

def new_apple():
    done = False
    x = 0
    y = 0
    while done == False:
        x = random.randrange(0, board_width)
        y = random.randrange(0, board_height)
        length = len(snake)
        for i in range(length):
            if snake[i][0] == x and snake[i][1] == y:
                done = False
                break
            else:
                done = True
    # apple = [x,y]
    return [x,y]





def update_snake_body():
    #iterate through snake's body
    snake_length = len(snake)
    for x in range(snake_length-1, 0, -1):
        snake[x][0] = snake[x-1][0]
        snake[x][1] = snake[x-1][1]

def up_key(event):
    check_collision([snake[0][0], snake[0][1] - 1])
    # update_snake_body()
    # snake[0][1] = snake[0][1] - 1
    print(snake)
    # draw_board()
     # tkinter.Label(window, text = "Middle Click!").pack()

def down_key(event):
    check_collision([snake[0][0], snake[0][1] + 1])
    # update_snake_body()
    # snake[0][1] = snake[0][1] + 1
    print(snake)
    # draw_board()
    # tkinter.Label(window, text = "Middle Click!").pack()

def left_key(event):
    check_collision([snake[0][0] - 1, snake[0][1]])
    # update_snake_body()
    # snake[0][0] = snake[0][0] - 1
    print(snake)
    # draw_board()
    # tkinter.Label(window, text = "Left Click!").pack()

def right_key(event):
    check_collision([snake[0][0] + 1, snake[0][1]])
    # update_snake_body()
    # snake[0][0] = snake[0][0] + 1
    print(snake)
    # draw_board()
    # tkinter.Label(window, text = "Right Click!").pack()

window.bind('<Left>', left_key)
window.bind('<Right>', right_key)
window.bind('<Up>', up_key)
window.bind('<Down>', down_key)

# collision
def check_collision(next_spot):
    # check boundaries
    global apple
    global score_int
    if next_spot[0] > board_width - 1 or next_spot[1] > board_width - 1 or next_spot[0] < 0 or next_spot[1] < 0:
        print('Game Over :(   You hit the wall!')
        # add something to actually make the game over
        return True

    # check self collision
    length = len(snake)
    for x in range(length - 1):
        if  next_spot == snake[x]:
            # add something to actually make the game over
            print('Game Over :(   You ran into yourself!')
            return True

    # check for apple
    if next_spot == apple:
        print('You ate an apple, yummy!')
        snake.insert(0, next_spot)
        apple = new_apple()
        score_int = score_int + 1
        score_str = 'You have ' + str(score_int) + ' points'
        if score_int == 1:
            score_str = 'You have ' + str(score_int) + ' point'
        score.set(score_str)
        window.update_idletasks()
    else:
        update_snake_body()
        snake[0] = next_spot
    draw_board()


# parameters
board_height = 12
board_width = 12
board = []
snake = [[5 ,5], [5,4], [4,4], [3,4]]
apple = new_apple()
score_int = 0

# game initialization
# button to start the game
tkinter.Button(window, text = "Start!", command = start).pack()

score = tkinter.StringVar()
score.set(0)
label = tkinter.Label(window, textvariable = score)
label.pack()

canvas = tkinter.Canvas(window, width = 500, height = 500)
canvas.pack()

#
# label = tkinter.Message(window, textvariable=score)
# print('initial score', score)
# score.set('0')
# print('initial score', score)
# label.pack()

draw_board()

#
# canvas.create_rectangle(10, 10, 20, 20, fill="green")
# canvas.create_rectangle(20, 20, 30, 30, fill="green")
# canvas.create_rectangle(30, 30, 40, 40, fill="green")

window.mainloop()
