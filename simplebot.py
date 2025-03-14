# WRITE YOUR CODE HERE

import tkinter.scrolledtext as tks #creates a scrollable text window

from datetime import datetime
from tkinter import *


# Create the main application window using Tk()
baseWindow = Tk()

# Set the title of the window
baseWindow.title("The Simple Bot")

# Set the size of the window
baseWindow.geometry("500x250")

# Create the chat window as a ScrolledText widget with "Arial" font
chatWindow = tks.ScrolledText(baseWindow, font="Arial")

# Configure tags for message alignment: 'tag-left' for bot messages, 'tag-right' for user messages
chatWindow.tag_configure('tag-left', justify='left')
chatWindow.tag_configure('tag-right', justify='right')

# Disable the chat window initially (it should not be editable by the user)
chatWindow.config(state=DISABLED)

# Create the send button, with specific font, text, and background color
# The 'command' option is commented out. Uncomment it and replace 'send' with your send function's name
sendButton = Button(
    baseWindow,
    font=("Verdana", 12, 'bold'),
    text="Send",
    bg="#fd94b4",
    activebackground="#ff467e",
    fg='#ffffff',
    # command=send
)

# Create the user entry box where the user types their messages
userEntryBox = Text(baseWindow, bd=1, bg="white", width=38, font="Arial")

# Place the chat window, user entry box, and send button on the main window using specific coordinates and sizes
chatWindow.place(x=1, y=1, height=200, width=500)
userEntryBox.place(x=3, y=202, height=27)
sendButton.place(x=430, y=200)

# Start the main event loop to keep the application running and responsive
baseWindow.mainloop()    