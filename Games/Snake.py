import tkinter

window = tkinter.Tk()
# window.geometry("500x500")
window.resizable(0,0)
window.title("Snake")

# parameters
board_height = 12
board_width = 12
board = []
snake = [[5 ,5]]


# initialize board layout
# for x in range(board_width):
#     board.append([])
#     for y in range(board_height):
#         if x == head_pos[0] and y == head_pos[1]:
#             board[x].append(1)
#         else:
#             board[x].append(0)



# functions
def start():
    # start the game
    tkinter.Label(window, text="Hi").pack()


def draw_board():
    # fill with greenspace
    for x in range(board_height):
        for y in range(board_width):
            rect = canvas.create_rectangle(25 * x, 25 * y, 25 * (x + 1), 25 * (y + 1), fill='green')
            # if board[x][y] == 1:
            #     color = 'blue'
            # else:
            #     color = 'green'
            # rect = canvas.create_rectangle(25*x, 25*y, 25*(x+1), 25*(y+1), fill=color)

    # fill in the snake
    length = len(snake)
    for x in range(length):
        rect = canvas.create_rectangle(25 * snake[x][0], 25 * snake[x][1], 25 * (snake[x][0] + 1), 25 * (snake[x][1] + 1), fill='brown')





# def left_click(event):
#     snake[0][0] = snake[0][0] - 1
#     draw_board()
#     tkinter.Label(window, text = "Left Click!").pack()
#
# def middle_click(event):
#     draw_board()
#     tkinter.Label(window, text = "Middle Click!").pack()
#
# def right_click(event):
#     snake[0][0] = snake[0][0] + 1
#     draw_board()
#     tkinter.Label(window, text = "Right Click!").pack()

# window.bind("<Button-1>", left_click)
# window.bind("<Button-2>", middle_click)
# window.bind("<Button-3>", right_click)



def left_key(event):
    snake[0][0] = snake[0][0] - 1
    draw_board()
    # tkinter.Label(window, text = "Left Click!").pack()

def up_key(event):
    snake[0][1] = snake[0][1] - 1
    draw_board()
    # tkinter.Label(window, text = "Middle Click!").pack()

def down_key(event):
    snake[0][1] = snake[0][1] + 1
    draw_board()
    # tkinter.Label(window, text = "Middle Click!").pack()

def right_key(event):
    snake[0][0] = snake[0][0] + 1
    draw_board()
    # tkinter.Label(window, text = "Right Click!").pack()

window.bind('<Left>', left_key)
window.bind('<Right>', right_key)
window.bind('<Up>', up_key)
window.bind('<Down>', down_key)

# game initialization
# button to start the game
tkinter.Button(window, text = "Start!", command = start).pack()

canvas = tkinter.Canvas(window, width = 500, height = 500)
canvas.pack()

draw_board()

#
# canvas.create_rectangle(10, 10, 20, 20, fill="green")
# canvas.create_rectangle(20, 20, 30, 30, fill="green")
# canvas.create_rectangle(30, 30, 40, 40, fill="green")

window.mainloop()
