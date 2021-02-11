from pytube import YouTube
from tkinter import *
import tkinter as tk


# Class: Window
# class Window:
#     """All frames shall be ruled by this root window.o

#     Attributes:
#         master -- tk.Tk()
#         title -- Title of the window
#     """

#     def __init__(self, master, title: str):
#         self.master = master
#         self.title = title
#         self.master.title(self.title)

#     def __repr(self) -> str:
#         return f'{self.__class__.__name__}({self.master}, {self.title!r})'


class Window_Frame:
    """Base Class for creating frames within the window.

    Attributes:
        window -- Frame name
        x_grid -- Row placement within the window
        y_grid -- Column placemnet within the window

        entry:
            Creates an entry widget for any user input.

        button:
            Creates a standard button widget.

        label:
            Creates a label widget to display text.
    """

    def __init__(self, window: str, x_grid: int, y_grid: int):
        self.window = window
        self.x_grid = x_grid
        self.y_grid = y_grid

        # Create a frame upon instantiation
        self.frame = tk.Frame(self.window)
        self.frame.pack(padx=10, pady=10)

    def entry(self, txt_var=None):
        """Creates an entry widget.

        Attributes:
            txt_var -- Enter text variable
        """

        self.entry_lbl = tk.Entry(self.frame, textvariable=txt_var)

        return self.entry_lbl

    def label(self, msg: str, x_grid: int, y_grid: int):
        """Creates a label widget.

        Args:
            msg -- Text to be displayed
            x_grid -- Row placement of button
            y_grid -- Column placement of button

        Returns:
            A label widget.
        """

        self.lbl = tk.Label(self.frame, text=msg)
        self.lbl.grid(row=x_grid, column=y_grid)

        return self.lbl

    def button(self, msg: str, x_grid: int, y_grid: int):
        """Creates a button widget.

        Args:
            msg -- Text to be displayed
            x_grid -- Row placement of button
            y_grid -- Column placement of button

        Returns:
            A button widget.
        """

        self.btn = tk.Button(self.frame, text=msg)
        self.btn.grid(row=x_grid, column=y_grid)


# Derived Class: Search Bar
class Search_Frame(Window_Frame):
    """Creates a search bar that lookups the URL.

    Attributes:
        x_grid -- Row placement within the window
        y_grid -- Column placemnet within the window
    """

    def __init__(self, window: str, x_grid: int, y_grid: int):
        super().__init__(window, x_grid, y_grid)

        # Grid placement
        self.window.grid(row=x_grid, column=y_grid)

        # URL Search bar
        url = StringVar()
        self.entry_label = self.entry(url)
        self.entry_label.grid(row=1, column=1)

        self.button('Search', 1, 2)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x_grid}, {self.y_grid})'

    def button(self, msg: str, x_grid: int, y_grid: int):
        """Creates a button widget.

        Args:
            msg -- Text to be displayed
            x_grid -- Row placement of button
            y_grid -- Column placement of button

        Returns:
            A button widget.
        """

        self.btn = tk.Button(self.frame, text=msg, command=lambda: print('Hello'))
        self.btn.grid(row=x_grid, column=y_grid)


# Derived Class: Video Bar
class Video_Frame(Window_Frame):
    """Creates a frame that holds all videos that has been searched by the
    user.

    Attributes:
        x_grid -- Row placement within the window
        y_grid -- Column placemnet within the window

    """

    def __init__(self, window: str, x_grid: int, y_grid: int):
        super().__init__(window, x_grid, y_grid)

        # Grid placement
        self.window.grid(row=x_grid, column=y_grid)

    # Method to create a frame to display a video when an event occurs
    def video(self):
        """Displays the video that has been serached by the user.

        Args:
            frame -- The frame where the object will reside
            title -- Title of the video
            author -- Author of the video
        """
        self.title = self.label('Title', 1, 2)
        self.author = self.label('Author', 2, 2)


# Derived Class: Downloader
# Dropdown btn widget
# Check btn widget

# Save_To cmd
# Download cmd

# File path window (Dialog Windows)
# Progress bar

