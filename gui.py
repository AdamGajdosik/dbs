#!/usr/bin/python3

import tkinter as tk
import pygubu

class App:
    def __init__(self,root):
        self.root = root
        self.builder = pygubu.Builder()
        builder = self.builder
        builder.add_from_file("heh.ui")
        self.window = builder.get_object("Frame_1",root)

        builder.connect_callbacks(self)

    def on_click(self):
        print("prd")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()