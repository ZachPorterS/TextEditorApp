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
  file_menu = Menu(menu_bar)
  object_file = File(text, root)
  file_menu.add_command(label='New', command=object_file.New_File)
  file_menu.add_command(label='Open', command=object_file.Open_File)
  file_menu.add_command(label='Save', command=object_file.Save_File)
  file_menu.add_command(label='Save As...', command=object_file.Save_As)
  file_menu.add_separator()

  file_menu.add_command(label='Quit', command=object_file.Quit)
  menu_bar.add_cascade(label='File', menu=file_menu)
  root.config(menu=menu_bar)


if __name__ == "__main__":
  print("This is not the correct main, run main.py.")
  
