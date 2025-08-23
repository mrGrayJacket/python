#importing the modules
import curses
from curses.textpad import rectangle
import random
import time

#initialising the screen
stdscr = curses.initscr()

#getting the height and width
max_height = stdscr.getmaxyx()[0] -2
max_width = stdscr.getmaxyx()[1] -2
x_begin = 0
y_begin = 0

#inisialising the colors
curses.start_color()
curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
RED_BLACK = curses.color_pair(1)
GREEN_BLACK = curses.color_pair(2)

#definig the menu
menu = curses.newwin(max_height,max_width,0,0)

#preparing the windows
curses.curs_set(0)
curses.noecho()

#menu rules
menu.keypad(True)
menu.timeout(200)
statement = None

##default settings
#the controls
controls_display = "→←↓↑"
controls = [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP]

#speed
speed = 5

#area
area = 3

#running the menu
selection_id = 1
#settings running
selection_id2 = 1
selection_id3 = 1

while True:
    #asking for key to navigate
    key = menu.getch()
    if key == curses.KEY_UP:
        selection_id -= 1
    if key == curses.KEY_DOWN:
        selection_id += 1
    #adjusting the selection id
    if selection_id > 3:
        selection_id = 3
    if selection_id < 1:
        selection_id = 1
    #adjusting the menu display
    if selection_id == 1:
        menu.clear()
        menu.addstr(max_height // 3, max_width // 2 - 5, "Snake", RED_BLACK)
        menu.addstr(max_height // 3 + 3, max_width // 2 - 6, "> Start <",curses.A_BOLD | GREEN_BLACK)
        menu.addstr(max_height // 3 + 4, max_width // 2 - 5, "Settings")
        menu.addstr(max_height // 3 + 5, max_width // 2 - 5, "Quit")
    if selection_id == 2:
        menu.clear()
        menu.addstr(max_height // 3, max_width // 2 - 5, "Snake", RED_BLACK)
        menu.addstr(max_height // 3 + 3, max_width // 2 - 5, "Start")
        menu.addstr(max_height // 3 + 4, max_width // 2 - 6, "> Settings <",curses.A_BOLD | GREEN_BLACK)
        menu.addstr(max_height // 3 + 5, max_width // 2 - 5, "Quit")
    if selection_id == 3:
        menu.clear()
        menu.addstr(max_height // 3, max_width // 2 - 5, "Snake", RED_BLACK)
        menu.addstr(max_height // 3 + 3, max_width // 2 - 5, "Start")
        menu.addstr(max_height // 3 + 4, max_width // 2 - 5, "Settings")
        menu.addstr(max_height // 3 + 5, max_width // 2 - 6, "> Quit <",curses.A_BOLD | GREEN_BLACK)

    #submiting the decision
    if key == 10:
        if selection_id == 1:
            statement = "start"
        if selection_id == 2:
            statement = "settings"
        if selection_id == 3:
            curses.endwin()
            quit()

    #setting menu
    while statement == "settings":
        key2 = menu.getch()
        if key2 == curses.KEY_UP:
            selection_id2 -= 1
        if key2 == curses.KEY_DOWN:
            selection_id2 += 1
        # adjusting the selection id2
        if selection_id2 > 4:
            selection_id2 = 4
        if selection_id2 < 1:
            selection_id2 = 1

        # showing the settings menu
        if selection_id2 == 1:
            if key2 == curses.KEY_LEFT:
                selection_id3 -= 1
            if key2 == curses.KEY_RIGHT:
                selection_id3 += 1
            # adjusting the selection id3
            if selection_id3 > 3:
                selection_id3 = 3
            if selection_id3 < 1:
                selection_id3 = 1
            # the functionality
            if selection_id3 == 1:
                controls_display = "→←↓↑"
                controls = [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP]
            if selection_id3 == 2:
                controls_display = "DASW"
                controls = [100,97,115,119]
            if selection_id3 == 3:
                controls_display = "DQSZ"
                controls = [100, 113, 115, 122]
            menu.clear()
            menu.addstr(max_height // 3, max_width // 2 - 5, "Settings", RED_BLACK)
            menu.addstr(max_height // 3 + 3, max_width // 2 - 6, f"> Controls < [{controls_display}]",curses.A_BOLD | GREEN_BLACK)
            menu.addstr(max_height // 3 + 4, max_width // 2 - 5, "Speed")
            menu.addstr(max_height // 3 + 5, max_width // 2 - 5, "Area")
            menu.addstr(max_height // 3 + 6, max_width // 2 - 5, "Back")

        if selection_id2 == 2:
            if key2 == curses.KEY_LEFT:
                speed -= 1
            if key2 == curses.KEY_RIGHT:
                speed += 1
            # adjusting the speed
            if speed > 10:
                speed = 10
            if speed < 1:
                speed = 1

            menu.clear()
            menu.addstr(max_height // 3, max_width // 2 - 5, "Settings", RED_BLACK)
            menu.addstr(max_height // 3 + 3, max_width // 2 - 5, "Controls")
            menu.addstr(max_height // 3 + 4, max_width // 2 - 6, f"> Speed < [{speed}]", curses.A_BOLD | GREEN_BLACK)
            menu.addstr(max_height // 3 + 5, max_width // 2 - 5, "Area")
            menu.addstr(max_height // 3 + 6, max_width // 2 - 5, "Back")

        if selection_id2 == 3:
            if key2 == curses.KEY_LEFT:
                area -= 1
            if key2 == curses.KEY_RIGHT:
                area += 1
            # adjusting the speed
            if area > 3:
                area = 3
            if area < 1:
                area = 1
            if area == 1:
                max_height = int(stdscr.getmaxyx()[0] // 2.5) #12
                max_width = int(stdscr.getmaxyx()[1] // 2.5) #48
                x_begin = int((stdscr.getmaxyx()[1] - max_width)// 2) #6
                y_begin = int((stdscr.getmaxyx()[0] - max_height) // 2) #24
            if area == 2:
                max_height = int(stdscr.getmaxyx()[0] // 1.5) #20
                max_width = int(stdscr.getmaxyx()[1] // 1.5) #80
                x_begin = int((stdscr.getmaxyx()[1] - max_width) // 2) #40
                y_begin = int((stdscr.getmaxyx()[0] - max_height) // 2) #10
            if area == 3:
                max_height = int(stdscr.getmaxyx()[0] -2)
                max_width = int(stdscr.getmaxyx()[1] -2)
                x_begin = 0
                y_begin = 0

            menu.clear()
            menu.addstr(max_height // 3, max_width // 2 - 5, "Settings", RED_BLACK)
            menu.addstr(max_height // 3 + 3, max_width // 2 - 5, "Controls")
            menu.addstr(max_height // 3 + 4, max_width // 2 - 5, "Speed")
            menu.addstr(max_height // 3 + 5, max_width // 2 - 6, f"> Area < [x{area}]", curses.A_BOLD | GREEN_BLACK)
            menu.addstr(max_height // 3 + 6, max_width // 2 - 5, "Back")

        if selection_id2 == 4:
            menu.clear()
            menu.addstr(max_height // 3, max_width // 2 - 5, "Settings", RED_BLACK)
            menu.addstr(max_height // 3 + 3, max_width // 2 - 5, "Controls")
            menu.addstr(max_height // 3 + 4, max_width // 2 - 5, "Speed")
            menu.addstr(max_height // 3 + 5, max_width // 2 - 5, "Area")
            menu.addstr(max_height // 3 + 6, max_width // 2 - 6, "> Back <", curses.A_BOLD | GREEN_BLACK)
            if key2 == 10:
                menu.clear()
                statement = None
                break

    # the score
    score = 0

    # initialising the game screen
    game_scr = curses.newwin(max_height +2, max_width +2, y_begin, x_begin)

    # initialising the rectangle
    rectangle(game_scr,0,0,max_height,max_width)

    #speed scale
    speed_scale = int(500 // speed)

    # preparing the screen
    game_scr.keypad(True)
    game_scr.timeout(speed_scale)

    # default snake coordinates
    snake_x = max_width // 2 -5
    snake_y = max_height // 2

    # the snake body
    snake = [[snake_x, snake_y], [snake_x - 1, snake_y], [snake_x - 2, snake_y]]

    # snake default rotation
    rotation = controls[0]

    # snake default food coordinate
    food_x = max_width // 2
    food_y = max_height // 2

    # initialising the food
    food = [food_x, food_y]

    # showing the food
    game_scr.addch(food[1], food[0], "⬤",RED_BLACK)

    #runing the game
    pause = False
    sleep_once = True
    while statement == "start":
        # getting the player input
        new_rotation = game_scr.getch()

        # ending the game
        if snake[0][0] in [0, max_width] or snake[0][1] in [0, max_height] or snake[0] in snake[1:]:
            game_scr.addstr(max_height//2,max_width//2 - 5,"Game over")
            game_scr.addstr(max_height//2 + 2,max_width//2 - 6,f"Your score:{score}")
            game_scr.addstr(max_height//2 + 4,max_width//2 - 13,f"Press \"{controls_display[0]}\" to exit to menu")
            game_scr.refresh()
            pause = True
            #sleep
            if sleep_once:
                time.sleep(3)
                curses.flushinp()
                sleep_once = False
                new_rotation = -1
            #when you press forward
            if new_rotation == controls[0]:
                statement = None
                game_scr.clear()
                game_scr.refresh()
                break

        #pausing the game
        if pause:
            continue

        # setting the rotation
        if new_rotation in controls:
            rotation = new_rotation
        else:
            rotation = rotation

        # adding new head
        new_head = [snake[0][0], snake[0][1]]

        # moving the snake
        if rotation == controls[0]:
            new_head[0] += 1

        if rotation == controls[1]:
            new_head[0] -= 1

        if rotation == controls[2]:
            new_head[1] += 1

        if rotation == controls[3]:
            new_head[1] -= 1

        # adding the head
        snake.insert(0, new_head)

        # eating the food
        if snake[0] == food:
            # clearing the food and adding 1 to score
            food = None
            score += 1

            # generating new food
            while food is None:
                new_food = [random.randint(1, max_width - 1), random.randint(1, max_height - 1)]
                if new_food in snake:
                    food = None
                else:
                    food = new_food
                    game_scr.addch(food[1], food[0], "⬤",RED_BLACK)
        else:
            tail = snake.pop()
            game_scr.addch(tail[1], tail[0], " ")

        # showing the snake and food
        game_scr.addch(snake[0][1], snake[0][0], curses.ACS_CKBOARD)
