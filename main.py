import tkinter


def check_nul():
    print("match nul")


def print_winner():
    global win

    if win is False:
        win = True
        print("le joueur", current_player, "a gagné le jeu gg")


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def check_win(cliked_row, cliked_col):
    # détecter victoire horizontale
    count = 0
    for i in range(3):
        current_button = buttons[i][cliked_row]

        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # détecter victoire verticalement
    count = 0
    for i in range(3):
        current_button = buttons[cliked_col][i]

        if current_button['text'] == current_player:
            count += 1

    if count == 3:
        print_winner()

    # détecter victoire diagonale
    count = 0
    for i in range(3):
        current_button = buttons[i][i]

        if current_button['text'] == current_player:
            count += 1

    if count == 3:
        print_winner()

    # détecter victoire diagonale inverse
    count = 0
    for i in range(3):
        current_button = buttons[2 - i][i]

        if current_button['text'] == current_player:
            count += 1

    if count == 3:
        print_winner()

    if win is False:
        count = 0
        for col in range(3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button['text'] == 'X' or current_button['text'] == 'O':
                    count += 1
        if count == 9:
            print("match nul")


def place_symbol(row, column):
    print("click", row, column)

    cliked_button = buttons[column][row]
    if cliked_button['text'] == "":
        cliked_button.config(text=current_player)

        check_win(row, column)
        switch_player()


def lagrille():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                fenetre, font=("Arial", 50),
                width=5, height=3,
                command=lambda r=row, c=column: place_symbol(r, c)
            )
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

# stockages
buttons = []
current_player = 'X'
win = False

# crée la fenêtre du jeu
fenetre = tkinter.Tk()

# personnaliser la fenêtre
fenetre.title("morpion")
fenetre.minsize(500, 500)

lagrille()
fenetre.mainloop()
