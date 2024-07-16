from tkinter import messagebox
from tkinter import ttk
from tkinter import *

# Declare global variables
playAgain = True
start_game_bool = False
start_button_called_bool = False
gameStarted = True
default_icon_called = False
counter = 0
winner = "None"
icon_style = ("Calistoga", 25)
arr = [[0 for x in range(3)] for x in range(3)]

def start_game():
    global start_game_bool
    start_game_bool = True
    
    global start_button_called_bool
    start_button_called_bool = True
    
    home_window.destroy()
    
def exit_app():
    confirmation = messagebox.askquestion(title="Form", message="Are you sure you would like to exit the game?")
    if confirmation == "yes":
        global playAgain
        playAgain = False
        
        try:
            home_window.destroy()
        except:
            gameWindow.destroy()

def settings():
    home_frame.forget()
    settings_frame.pack(fill="both", expand=1)
    
def return_to_home():
    settings_frame.forget()
    home_frame.pack(fill="both", expand=1)

def go_homepage():
    gameWindow.destroy()
    
    global gameStarted
    global counter
    global arr
    global winner
    
    gameStarted = True
    counter = 0
    arr = [[0 for x in range(3)] for x in range(3)]
    winner = "None"
    
    select_comic_icons()

def new_game():
    for row in range(3):
        for col in range(3):
            points[row][col]["state"] = "normal"
            points[row][col].configure(text=" ")
            
    global counter
    global arr
    global winner
    counter = 0
    arr = [[0 for x in range(3)] for x in range(3)]
    winner = "None"
    
    winner_label.configure(text="")
    go_home_page.grid_forget()
    turn_label.grid(column=3, row=2)
    turn_label.configure(text="O")

def tic_tac_toe_calculator(x, y):
    global counter
    global arr

    if points[x][y].cget('text') != "X" and points[x][y].cget('text') != "O":
        if counter % 2 == 0:
            points[x][y].configure(text="X")
            points[x][y].configure(font=icon_style)
            arr[x][y] = 1 # represents X
        else:
            points[x][y].configure(text="O")
            points[x][y].configure(font=icon_style)
            arr[x][y] = 2 # represents O
    else:
        counter -= 1
    
    turn_signal()
    check_winner(1)
    check_winner(2)
    
    if counter == 9:
        call_tie()
    
def count_click(event):
    global counter
    counter += 1

def turn_signal():
    if counter % 2 == 0:
        turn_label.configure(text="O")
    else:
        turn_label.configure(text="X")

def check_winner(indicator):
    global winner
    if indicator == 1:
        prompt_when_won = "X IS THE WINNER :D"
    else:
        prompt_when_won = "O IS THE WINNER :D"
    
    for row in range(3):
        for col in range(3):
            if arr[0][col] == arr[1][col] == arr[2][col] != 0:
                update_winner(prompt_when_won)
                return
            elif arr[row][0] == arr[row][1] == arr[row][2] != 0:
                update_winner(prompt_when_won)
                return

    if arr[0][0] == arr[1][1] == arr[2][2]!= 0 or arr[0][2] == arr[1][1] == arr[2][0] != 0:
        update_winner(prompt_when_won)
        return

def update_winner(prompt):
    winner_label.configure(text=prompt)
    disable_button()

def disable_button():
    for row in range(3):
        for col in range(3):
            points[row][col]["state"] = "disabled"
            points[row][col].config(disabledforeground="#FFC000")
    
    turn_label.grid_forget()
    go_home_page.grid(column=3, row=2)

def call_tie():
    winner_label.configure(text="THE GAME IS A TIE :/")
    disable_button()

def select_default_theme():
    tic.place_forget()
    tac.place_forget()
    toe.place_forget()
    
    home_title.pack(fill="x", expand=1)
    title_comic.configure(text="DEFAULT THEME", font=("Arial", 15), bg="black")
    title_comic.pack(fill="x", expand=0)
    
    edition.place_forget()
    stdnt_id.place_forget()
    
    play_btn.configure(text="Start", font=("Comic Sans MS", 20))
    play_btn.pack(fill="both", expand=1)
    
    settings_btn.configure(text="Settings", font=("Comic Sans MS", 20))
    settings_btn.pack(fill="both", expand=1)
    
    exit_btn.configure(text="Exit", font=("Comic Sans MS", 20))
    exit_btn.pack(fill="both", expand=1)
    
    panel_img.configure(file="")
    img_label.place_forget()
    
    settings_title.configure(font=("Arial", 50))
    theme_frame.configure(font=("Arial", 15))
    default_theme_radiobtn.configure(font=("Arial", 10))
    comic_theme_radiobtn.configure(font=("Arial", 10))
    icon_frame.configure(font=("Arial", 15))
    default_icons_radiobtn.configure(font=("Arial", 10))
    comic_icons_radiobtn.configure(font=("Arial", 10))
    return_btn.configure(font=("Arial", 10))
    
def select_comic_theme():
    home_title.forget()
    tic.place(x=25, y=-115)
    toe.place(x=310, y=95)
    tac.place(x=310, y=-30)
    
    title_comic.configure(text="OLD COMICS", font=("Just Another Hand", 55), bg="#C70E0E",)
    title_comic.place(x=50, y=230)
    
    edition.place(x=340, y=240)
    stdnt_id.place(x=340, y=280)
    
    play_btn.configure(text="LET'S GET STARTED", font=("Just Another Hand", 15))
    play_btn.place(x=50, y=340)
    
    settings_btn.configure(text="CHANGE THINGS UP", font=("Just Another Hand", 15))
    settings_btn.place(x=50, y=390)
    
    exit_btn.configure(text="LET ME OUTTA HERE", font=("Just Another Hand", 15))
    exit_btn.place(x=50, y=440)
    
    img_label.place(x=260, y=340, relwidth=0.34, relheight=0.29)
    
    settings_title.configure(font=("Bayon", 65))
    theme_frame.configure(font=("Bayon", 20))
    
    default_theme_radiobtn.configure(font=("Just Another Hand", 15))
    comic_theme_radiobtn.configure(font=("Just Another Hand", 15))
    
    icon_frame.configure(font=("Bayon", 20))
    default_icons_radiobtn.configure(font=("Just Another Hand", 15))
    
    comic_icons_radiobtn.configure(font=("Just Another Hand", 15))
    return_btn.configure(font=("Just Another Hand", 15))
    
def select_default_icons():
    global icon_style
    global default_icon_called
    icon_style = ("Arial", 25)
    default_icon_called = True

def select_comic_icons():
    global icon_style
    global default_icon_called
    icon_style = ("Calistoga", 25)
    default_icon_called = False

# --- MAIN CODE ---
while playAgain and gameStarted:
    gameStarted = False
    
    # -- Set home window -- 
    home_window = Tk()
    home_window.title("Tic Tac Toe")
    home_window.geometry("500x500")
    home_window.resizable(False, False) 

    # Set frames for home_window
    home_frame = Frame(home_window, bg="white")
    home_frame.pack(fill="both", expand=1)
    settings_frame = Frame(home_window, bg="white")

    # -- Title screen -- 
    # Title of game (comic)
    tic = Label(home_frame, text="TIC", bg="white")
    tic.configure(font=("Bayon", 200))
    tac = Label(home_frame, text="TAC")
    tac.configure(font=("Bayon", 75), bg="white")
    toe = Label(home_frame, text="TOE")
    toe.configure(font=("Bayon", 75), bg="white")

    # Title of game (default)
    home_title = Label(home_frame, text="TIC TAC TOE", bg="white")
    home_title.configure(font=("Comic Sans MS", 50))

    # -- Display comic theme ---
    title_comic = Label(home_frame, fg="#FFFFFF")
    edition = Label(home_frame, text="Edition", font=("Caesar Dressing", 20), bg="#C70E0E", fg="#FFFFFF")
    stdnt_id = Label(home_frame, text="867802", font=("Caesar Dressing", 19), bg="#C70E0E", fg="#FFFFFF")

    # Buttons for home window
    play_btn = Button(home_frame, command=start_game, bg="#FFFFFF", width=32)
    settings_btn = Button(home_frame, command=settings, bg="#FFFFFF", width=32)
    exit_btn = Button(home_frame, command=exit_app, bg="#FFFFFF", width=32)

    # Image for visuals
    panel_img = PhotoImage(file="comic_panel.png")
    img_label = Label(home_frame, image=panel_img)
    
    # -- Settings --
    # Settings title
    settings_title = Label(settings_frame, text="SETTINGS", bg="black", fg="white")
    settings_title.pack(fill="x", expand=0)
    # Select theme
    theme_frame = LabelFrame(settings_frame, text="Customize theme", bg="white")
    theme_frame.pack(fill="x", expand=0)
    select_theme_val = IntVar()
    # Radiobuttons for theme selection
    default_theme_radiobtn = Radiobutton(theme_frame, text="DEFAULT", bg="white", value=1, variable=select_theme_val, command=select_default_theme) # do nothing
    default_theme_radiobtn.grid(sticky=W)
    comic_theme_radiobtn = Radiobutton(theme_frame, text="OLD COMICS", bg="white", value=0, variable=select_theme_val, command=select_comic_theme)
    comic_theme_radiobtn.grid(row=1, column=0, sticky=W)
    select_theme_val.set(0) # enable comic theme by default

    # Icons frame
    icon_frame = LabelFrame(settings_frame, text="Customize icons", bg="white")
    icon_frame.pack(fill="x", expand=0)
    select_icon_val = IntVar()
    # Radiobuttons for icon selection
    default_icons_radiobtn = Radiobutton(icon_frame, text="DEFAULT ICONS", bg="white", value=0, variable=select_icon_val, command=select_default_icons)
    default_icons_radiobtn.grid(sticky=W)
    comic_icons_radiobtn = Radiobutton(icon_frame, text="PANEL ICONS", bg="white", value=1, variable=select_icon_val, command=select_comic_icons)
    comic_icons_radiobtn.grid(row=1, column=0, sticky=W)
    select_icon_val.set(1) # enable comic icon by default

    # Button to go back to home
    return_btn = Button(settings_frame, text="RETURN TO HOME", command=return_to_home, bg="white")
    return_btn.pack(fill="both", expand=0)

    # Set to comic theme by default
    select_comic_theme()
    
    home_window.mainloop()



    # --- GAME SEQUENCE -- 
    if start_game_bool == True and start_button_called_bool == True:
        # Create game window
        gameWindow = Tk()
        gameWindow.title("Tic Tac Toe")
        gameWindow.geometry("480x500")
        gameWindow.resizable(False, False) 

        # Create frame for tic tac toe grid
        tic_tac_toe_grid = LabelFrame(gameWindow, text="", borderwidth=0, highlightthickness=0, bg="white")
        tic_tac_toe_grid.pack(fill="both", expand=1)

        # Populates array to make 2d list
        points = [[0 for x in range(3)] for x in range(3)]
        # Creates the 2D Grid
        for x in range(3):
            for y in range(3):
                # Reassigns the integer array to button array
                points[x][y] = Button(tic_tac_toe_grid, text='', bg="#C70E0E", fg="white", height=1, width=7, command=lambda x=x, y=y: tic_tac_toe_calculator(x, y), font=icon_style)
                
                # Change styling based on icon style
                if icon_style == ("Arial", 25):
                    points[x][y].configure(height=2)
                
                # Bind click to count_click function
                points[x][y].bind("<Button-1>", count_click)
                
                # Format & center
                point_x = x + 3
                point_y = y + 3
                points[x][y].grid(column=point_x, row=point_y)
                
        # Information grid
        display_grid = Frame(gameWindow, borderwidth=0, highlightthickness=0, bg="white")
        display_grid.pack(fill="both", expand=1)
    
        # Tells you whose turn it is
        turn_label = Label(display_grid, width=6, height=0, text="O", font=icon_style, bg="white", borderwidth=2, relief="groove")
        turn_label.grid(column=3, row=2)

        # Button to restart game
        new_game = Button(display_grid, text="RESTART GAME", font=("Just Another Hand", 20), bg="white", command=new_game)
        new_game.grid(column=1, row=2)
        
        # Label to display winnner
        winner_label = Label(display_grid, text="", font=("Just Another Hand", 30), bg="white", width=35, borderwidth=2, relief="groove")
        winner_label.grid(column=1, row=0, columnspan=5)

        # Display home page button after game is finished
        go_home_page = Button(display_grid, text="  HOME  ", font=("Just Another Hand", 21), width= 11, command=go_homepage, bg="black", fg="white")
        
        # Option to exit game 
        exit_game = Button(display_grid, text="EXIT THE GAME", font=("Just Another Hand", 20), bg="white", command=exit_app)   
        exit_game.grid(column=5, row=2)
        
        # Ensures that the loop repeats for BOTH windows
        playAgain = True
        
        # Empty labels to format grid accordingly
        Label(display_grid, text="", font=("Calistoga", 4), bg="white").grid(column=4, row=1)
        if default_icon_called:
            Label(tic_tac_toe_grid, text="   ", bg="white").grid(column=0, row=0)
            Label(tic_tac_toe_grid, text="   ", bg="white").grid(column=1, row=0)
            Label(display_grid, text="", font=icon_style, bg="white").grid(column=4, row=2)
        else:
            Label(tic_tac_toe_grid, text="  ", bg="white").grid(column=0, row=0)
            Label(tic_tac_toe_grid, text="  ", bg="white").grid(column=1, row=0)
            Label(display_grid, text="  ", font=icon_style, bg="white").grid(column=4, row=2)
        Label(display_grid, text="    ", font=("Calistoga", 25), bg="white").grid(column=0, row=2)
        Label(display_grid, text="   ", font=icon_style, bg="white").grid(column=2, row=2)
        Label(display_grid, text="  ", font=icon_style, bg="white").grid(column=4, row=2)
            
        gameWindow.mainloop()
    else:
        exit()
