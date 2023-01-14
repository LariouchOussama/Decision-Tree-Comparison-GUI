# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 21:33:56 2022

@author: DELL
"""

import tkinter as tk
from app import App


 
def main():
    # Create the root window
    root = tk.Tk()
    # Create an instance of the App class
    app = App(root)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
