from cProfile import label
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.font import Font, families
from tkinter.scrolledtext import *

import time
import sys


class Format():
  def __init__(self, text):
    ''' Class to handle the formatting of the text for the application. '''
    self.text = text
  
  def ChangeBG(self):
    (triple, hexstr) = askcolor()
    if hexstr:
      self.text.config(bg=hexstr)
  
  def ChangeFC(self):
    (triple, hexstr) = askcolor()
    if hexstr:
      self.text.config(fg=hexstr)
  
  def Bold(self, *args):
    try:
      current_tags = self.tag_names("selected.first")
      if "bold" in current_tags:
        self.text.tag_remove("bold", "selected.first", "selected.last")
      else:
        self.text.tag_add("bold", "selected.first", "selected.last")
        bold_font = Font(self.text, self.text.cget("Font"))
        bold_font.configure(weight='bold')
        self.text.tag_configure('bold', font=bold_font)
    except:
      pass
  
  def Italic(self, *args):
    try:
      current_tags = self.text.tag_names("selected.first")
      if "italic" in current_tags:
        self.text.tag_remove("italic", "select.first", "select.last")
      else:
        self.text.tag_add("italic", "select.first", "select.last")
        italic_font = Font(self.text, self.text.cget("font"))
        italic_font.configure(slant="italic")
        self.text.tag_configure("italic", font=italic_font)
    except:
      pass
  
  def Underline(self, *args):
    try:
      current_tags = self.text.tag_names("selected.first")
      if "underline" in current_tags:
        self.text.tag_remove("underline", "select.first", "select.last")
      else:
        self.text.tag_add("underline", "select.first", "select.last")
        underline_font = Font(self.text, self.text.cget("font"))
        underline_font.configure(underline=1)
        self.text.tag_configure("underline", font=underline_font)
    except:
      pass

  def Overstrike(self, *args):
    try:
      current_tags = self.text.tag_names("select.first")
      if "overstrike" in current_tags:
        self.text.tag_remove("overstrike", "select.first", "select.last")
      else:
        self.text.tag_add("overstike", "select.first", "select.last")
        overstrike_font = Font(self.text, self.text.cget("font"))
        overstrike_font.configure(overstrike=1)
        self.text.tag_configure("overstrike", font=overstrike_font)
    except:
      pass

  def AddDate(self):
    full_date = time.localtime()
    day = str(full_date.tm_mday)
    month = str(full_date.tm_mon)
    year = str(full_date.tm_year)
    date = day + '-' + month + '-' + year
    self.text.insert(INSERT, date, 'a')


def main(root, text, menu_bar):
  object_format = Format(text)

  font_option = families(root)
  font = Font(family="Courier", size=10)
  text.configure(font=font)

  format_menu = Menu(menu_bar)

  font_sub_menu = Menu(format_menu, tearoff=0)  # Font Family
  size_sub_menu = Menu(format_menu, tearoff=0)  # Font Size

  for option in font_option:
    font_sub_menu.add_command(label=option, command=lambda option=option: font.configure(family=option))
  
  for value in range(1, 31):
    size_sub_menu.add_command(label=str(value), command=lambda value=value: font.configure(size=value))

  format_menu.add_command(label="Change Background Colour", command=object_format.ChangeBG)
  format_menu.add_command(label="Change Font Colour", command=object_format.ChangeFC)
  format_menu.add_command(label="Font Family", underline=0, menu=font_sub_menu)
  format_menu.add_command(label="Font Size", underline=0, menu=size_sub_menu)
  format_menu.add_command(label="Bold", command=object_format.Bold, accelerator="Ctrl+B")
  format_menu.add_command(label="Italic", command=object_format.Italic, accelerator="Ctrl+I")
  format_menu.add_command(label="Underline", command=object_format.Underline, accelerator="Ctrl+U")
  format_menu.add_command(label="Overstrike", command=object_format.Overstrike, accelerator="Ctrl+T")
  format_menu.add_command(label="Add Date", command=object_format.AddDate)
  menu_bar.add_cascade(label="Format", menu=format_menu)

  root.bind_all("<Control-b>", object_format.Bold)
  root.bind_all("<Control-i>", object_format.italic)
  root.bind_all("<Control-u>", object_format.Underline)
  root.bind_all("<Control-t>", object_format.Overstrike)
  root.grid_columnconfigure(0, weight=1)
  root.resizeable(True, True)
  root.config(menu=menu_bar)

if __name__ == '__main__':
  print("This is not the correct main, run main.py.")