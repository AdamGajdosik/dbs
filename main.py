#!/usr/bin/python3

import tkinter as tk
import pygubu
from database_controller import *
from config_parser import *


class Application:
    def __init__(self,root_window):

        self.root_window = root_window

        db_acces = ConfigParser.getDatabaseAcces()
        self.database = Database(db_acces["host"],db_acces["user"],db_acces["password"],db_acces["database_name"])
        self.database.connect()

        self.builder = builder = pygubu.Builder()
        self.builder.add_from_file("./gui_xml_files/heh.ui")
        self.window = builder.get_object("Frame_1",root_window)
        builder.connect_callbacks(self)

    def exit_app(self):
        print("Exitting...")
        self.root_window.quit()

    def change_frame(self):
        self.window = self.builder.get_object("Frame_2",self.root_window)
        self.builder.connect_callbacks(self)


def main():
    root_window = tk.Tk()
    app = Application(root_window)
    root_window.mainloop()


if __name__ == "__main__":
    main()