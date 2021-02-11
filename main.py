from pytube import YouTube
from tkinter import *
import tkinter as tk
from frames import *


def main():

    root = tk.Tk()
    root.geometry("500x200")

    # Create a Parent frame for all other subframes
    mainframe = tk.Frame(root)
    mainframe.grid(row=1, column=10)

    # Framework
    search_bar = tk.Frame(mainframe)
    search_bar.grid(row=1, columnspan=10)

    video_bar = tk.Frame(mainframe)
    video_bar.grid(row=2, column=1)

    # Class variables
    search = Search()
    video = Video()

    # Search_bar widgets
    # url = StringVar()
    url = ''
    search.entry(search_bar, url, 1, 1, 8)
    search.button(search_bar, 'Search', url, 1, 10)


    # Run Application
    root.mainloop()


if __name__ == '__main__':
    main()
