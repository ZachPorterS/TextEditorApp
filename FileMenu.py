import sys
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *


class File():
  def __init__(self, text, root):
    ''' A class to handle file management of the
        text editor application.
    '''
    self.file_name = None
    self.text = text
    self.root = root
  
  def New_File(self):
    self.file_name = "Untitled"
    self.text.delete(0.0, END)
  
  def Save_File(self):
    try:
      text = self.text.get(0.0, END)
      file = open(self.file_name, 'w')
      file.write(text)
      file.close()
    except:
      self.Save_As()
  
  def Save_As(self):
    file = asksaveasfile(mode='w', defaultextension='.txt')
    text = self.text.get(0.0, END)
    try:
      file.write(text.rstrip())
    except:
      showerror(title="ERROR: File Failed to Save", message="Oops! The file was unable to be saved...")
    
  def Open_File(self):
    file = askopenfile(mode='r')
    self.file_name = file.name
    text = file.read()
    self.text.delete(0.0, END)
    self.text.insert(0.0, END)

  def Quit(self):
    entry = askyesno(title='Quit', message='Sure you want to quit?')
    if entry:
      self.root.destroy()
  

def main(root, text, menu_bar):

