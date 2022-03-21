from cProfile import label
from tkinter import *
from tkinter.messagebox import *
import sys


class Help():
  def About(root):
    showinfo(title='About', message="Simple text editor using tkinter.")


def main(root, text, menu_bar):
  help = Help()
  help_menu = Menu(menu_bar)
  help_menu.add_command(label='About', command=Help.About)
  menu_bar.add_cascade(label='Help', menu=help_menu)
  root.config(menu=menu_bar)


if __name__ == "__main__":
  print("This is not the correct main, run main.py.")
