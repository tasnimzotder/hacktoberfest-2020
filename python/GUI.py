#Plying around with graphic user interface with python is a thrill , in this we will discuss a simple login GUI:)



import tkinter

window = tkinter.Tk()

window.title("GUI")

# creating 2 text labels and input labels

tkinter.Label(window, text = "Username").grid(row = 0) # this is placed in 0 0

# 'Entry' is used to display the input-field

tkinter.Entry(window).grid(row = 0, column = 1) # this is placed in 0 1

tkinter.Label(window, text = "Password").grid(row = 1) # this is placed in 1 0

tkinter.Entry(window).grid(row = 1, column = 1) # this is placed in 1 1

# 'Checkbutton' is used to create the check buttons

tkinter.Checkbutton(window, text = "Keep Me Logged In").grid(columnspan = 2) # 'columnspan' tells to take the width of 2 columns

# you can also use 'rowspan' in the similar manner

window.mainloop()

#space between each line ---(Social distancing XDXD) 
