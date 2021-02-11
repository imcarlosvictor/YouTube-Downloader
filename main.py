from pytube import YouTube
from tkinter import *
import tkinter as tk
from frames import *


def main():

    root = tk.Tk()

    # Create a Parent frame for all other subframes
    mainframe = tk.Frame(root)
    mainframe.grid(row=5, column=2)

    Search_Frame(mainframe, 1, 1)
    Video_Frame(mainframe, 2, 1)



    root.mainloop()


if __name__ == '__main__':
    main()
