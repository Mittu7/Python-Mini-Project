import os
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar
import pytube

#Creating class for the UI
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.video_url = tk.StringVar()

        # Create the UI elements
        self.video_url_label = tk.Label(self, text="Video URL:")
        self.video_url_entry = tk.Entry(self, textvariable=self.video_url)
        self.download_button = tk.Button(
            self, text="Download", command=self.download_video
        )
        self.progress_bar = Progressbar(self, mode="determinate")

        # Layout the UI elements
        self.video_url_label.grid(row=0, column=0)
        self.video_url_entry.grid(row=0, column=1)
        self.download_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.progress_bar.grid(row=2, column=0, columnspan=2, sticky="we")

        # Set the window size
        self.geometry("400x200")

    #Video Download Function When The Buttom is Clicked
    def download_video(self):
        # Get the video URL from the user
        video_url = self.video_url.get()

        # Default download path to current directory
        download_path = os.getcwd()

        # Download the video
        try:
            video = pytube.YouTube(video_url)
            stream = video.streams.get_highest_resolution()
            if stream:
                stream.download(output_path=download_path)
                print("Download completed!")
            else:
                print("No video available")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = App()
    app.mainloop()
