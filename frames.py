from pytube import YouTube
from typing import List
from tkinter import *
from tkinter import filedialog
import tkinter as tk



class Frame_Toolkit:
    """Widget toolkit for all frames.

    Attributes:
        button:
            Creates a standard button widget.

        label:
            Creates a label widget to display text.
    """

    def label(self, frame, msg: str, row: int, column: int):
        """Creates a label widget.

        Args:
            frame -- Residing frame of the widget
            msg -- Text to be displayed
            row -- Row placement of button
            column -- Column placement of button

        Returns:
            A label widget.
        """

        self.lbl = tk.Label(frame, text=msg)
        self.lbl.grid(row=row, column=column)

        return self.lbl

    def button(self, frame, msg: str, row: int, column: int):
        """Creates a button widget.

        Args:
            frame -- Residing frame of the widget
            msg -- Text to be displayed
            row -- Row placement of button
            column -- Column placement of button

        Returns:
            A button widget.
        """

        self.btn = tk.Button(frame, text=msg)
        self.btn.grid(row=row, column=column)

    def canvas(self, frame, image, width: int, height: int):
        """Canvas for the thumbnail.

        Args:
            frame -- Residing frame of the widget
            width -- Width of the canvas
            height -- Height of the canvas
        """

        img = PhotoImage(file=image)

        self.video_img = tk.Canvas(self.frame, width=width, height=height)
        self.thumbnail = self.video_img.create_image(image=img)


# Derived Class: Search Bar
class Search(Frame_Toolkit):
    """Creates a search bar that lookups the URL.

    Attributes:
    """

    def entry(self, frame, txt_var, row: int, column: int, col_span: int):
        """Creates an entry widget.

        Attributes:
            frame -- residing frame the entry widget
            txt_var -- Enter text variable
            row -- Row placement of button
            column -- Column placement of button
            col_span -- Span of columns
        """

        self.entry_lbl = tk.Entry(frame, textvariable=txt_var)
        self.entry_lbl.grid(row=row, column=column, columnspan=col_span)

    def button(self, frame, msg: str, link, row: int, column: int):
        """Creates a button widget.

        Args:
            frame -- residing frame the entry widget
            msg -- Text to be displayed
            row -- Row placement of button
            column -- Column placement of button

        Returns:
            A button widget.
        """

        # self.btn = tk.Button(frame, text=msg, command=lambda: self.search_url(link))
        self.btn = tk.Button(frame, text=msg, command=lambda: self.search_url(link))
        self.btn.grid(row=row, column=column)

    # def hello(self, link):
    #     print(type(link))

    def search_url(self, link: str):
        """Searches the video via link.

        Args:
            link -- Link of the video
        """

        yt_video = YouTube(link)
        thumbnail = yt_video.thumbnail_url
        title = yt_video.title
        author = yt_video.author

        # Find video information
        video_info = {
            'Thumbnail': thumbnail,
            'Title': title,
            'Author': author
        }

        print(video_info)


# Derived Class: Video Bar
class Video(Frame_Toolkit):
    """Creates a frame that holds all videos that has been searched by the
    user.

    Attributes:
        video():
            Creates a frame block to display the thumbnail, title and author
            of the video searched.
    """

    # Method to create a frame to display a video when an event occurs
    def video(self):
        """Displays the video that has been searched by the user.

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
class Downloader(Frame_Toolkit):
    """Toolkit for the frame that downloads the specified video.

    Attributes:
        btn_radio():
            Creates a frame that holds a radio button and the stream of the
            YouTube video that can be downloaded.
    """

    def radio_button(self, frame, text: str, variable, value: str,
                     row: int, column: int):
        """Creates a radio button"""

        self.radio = tk.Radiobutton(frame, text=text, variable=variable, value=value)
        self.radio.grid(row=row, column=column)

    # new radio_button function. Create a list of tuples conataining the download
    # information and use a for loop to create a radio button instead of calling
    # a function everytime
    def new_radio(self, stream_list: List[str]):
        """Creates a list of radio buttons from a list.

        Args:
        """
        pass

    # Save_To cmd
    def save_to(self):
        """Allows the user to choose the folder path to store the
        downloaded video(s).
        """

        dirname = filedialog.askdirectory()

        return dirname

    # Download cmd
    def download(self):
        """Downloads the video.

        Args:

        """
        # Progress bar

        pass


