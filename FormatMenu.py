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
  
  def Change_BG(self):
    (triple, hexstr) = askcolor()
    if hexstr:
      self.text.config(bg=hexstr)
  
  def Change_FG(self):
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