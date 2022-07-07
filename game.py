# tic-tac-toe game (code academy project)
from tkinter import *
from tkinter import messagebox

# create a object root of TK(tkinter) class
root = Tk()

# Call the title method from TK class using root as an object since it can access all the methods of tkinter class
root.title("Tic-Tac-Toe")

# Put icon in the top left of the widget using iconbitmap method from root object of TK class
root.iconbitmap('/Users/prabhnoorsingh/Computing/Back End/Python/Project Game/title_icon.png')

# Check if the game is tied
def game_tied():
  if count == 9 and winner == False:
    messagebox.showinfo("Tic-Tac-Toe", "The game is tied")
    disable_all_buttons()


# Disable all functions
def disable_all_buttons():
  b1.config(state=DISABLED)
  b2.config(state=DISABLED)
  b3.config(state=DISABLED)
  b4.config(state=DISABLED)
  b5.config(state=DISABLED)
  b6.config(state=DISABLED)
  b7.config(state=DISABLED)
  b8.config(state=DISABLED)
  b9.config(state=DISABLED)

# Check to see if someone won
def checkifwon():
  global winner 
  winner = False
  
  # Checking for horizontal x axis first for "X"
  if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
    b1.config(highlightbackground="red")
    b2.config(highlightbackground="red")
    b3.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()
  elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
    b4.config(highlightbackground="red")
    b5.config(highlightbackground="red")
    b6.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()
  elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
    b7.config(highlightbackground="red")
    b8.config(highlightbackground="red")
    b9.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()
    
  # Checking for vertical Y axis next
  elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
    b1.config(highlightbackground="red")
    b4.config(highlightbackground="red")
    b7.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()
  elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
    b2.config(highlightbackground="red")
    b5.config(highlightbackground="red")
    b8.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()
  elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
    b3.config(highlightbackground="red")
    b6.config(highlightbackground="red")
    b9.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()
    
  #checking for diagonals now
  elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
    b1.config(highlightbackground="red")
    b5.config(highlightbackground="red")
    b9.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()
  elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
    b3.config(highlightbackground="red")
    b5.config(highlightbackground="red")
    b7.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()
    
  # Checking for horizontal x axis first for "O"
  elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
    b1.config(highlightbackground="red")
    b2.config(highlightbackground="red")
    b3.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()
  elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
    b4.config(highlightbackground="red")
    b5.config(highlightbackground="red")
    b6.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()
  elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
    b7.config(highlightbackground="red")
    b8.config(highlightbackground="red")
    b9.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()
    
  # Checking for vertical Y axis next
  elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
    b1.config(highlightbackground="red")
    b5.config(highlightbackground="red")
    b7.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()
  elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
    b2.config(highlightbackground="red")
    b5.config(highlightbackground="red")
    b8.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()
  elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
    b3.config(highlightbackground="red")
    b6.config(highlightbackground="red")
    b9.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()
    
  #checking for diagonals now
  elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
    b1.config(highlightbackground="red")
    b5.config(highlightbackground="red")
    b9.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()
  elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
    b3.config(highlightbackground="red")
    b5.config(highlightbackground="red")
    b7.config(highlightbackground="red")
    winner = True
    messagebox.showinfo("Tic-Tac-Toe", "Congratulations you won the game")
    disable_all_buttons()

# X starts first so "True"
clicked = True
count = 0

# Button clicked Function
def b_click(b):
  global clicked, count
  
  if b["text"] == " " and clicked == True:
    b["text"] = "X"
    clicked = False
    count += 1
    checkifwon()
    game_tied()
  elif b["text"] == " " and clicked == False:
    b["text"] = "O"
    clicked = True
    count += 1
    checkifwon()
    game_tied()
  else:
    messagebox.showerror("Tic-Tac-Toe", "Please click a empty box\n This box is already selected")

# Build our Buttons

b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, highlightbackground="white", command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, highlightbackground="white", command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, highlightbackground="white", command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, highlightbackground="white", command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, highlightbackground="white", command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, highlightbackground="white", command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, highlightbackground="white", command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, highlightbackground="white", command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, highlightbackground="white", command=lambda: b_click(b9))

# Grid our buttons to the screen
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


#reset the game
# def reset():
#   pass
# # create menu
# my_menu = Menu(root)
# root.config(menu=my_menu)

# #create Options Menu
# options_menu = Menu(my_menu, tearoff=False)
# my_menu.add_cascade(Label="Options", menu=options_menu)
# options_menu.add_command(Label="Reset Game", command=reset)

root.mainloop()