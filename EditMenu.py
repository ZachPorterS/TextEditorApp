from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
from tkinter.messagebox import *

class Edit():
  def __init__(self, text, root):
    ''' A class to handle the editing methods of the
        text editing application.
    '''
    self.clipboard = None
    self.text = text
    self.rightClick = Menu(root)
  
  def Popup(self, event):
    self.rightClick.post(event.x_root, event.y_root)

  def Copy (self, *args):
    selected = self.text.selection_get()
    self.clipboard = selected
  
  def Cut(self, *args):
    selected = self.text.selection_get()
    self.clipboard = selected
    self.text.delete(SEL_FIRST, SEL_LAST)
  
  def Paste(self, *args):
    self.text.insert(INSERT, self.clipboard)
  
  def Select_All(self, *args):
    self.text.tag_add(SEL, "1.0", END)
    self.text.mark_set(0.0, END)
    self.text.see(INSERT)
  
  def Undo(self, *args):
    self.text.edit_undo()
  
  def Redo(self, *args):
    self.text.edit_redo()
  
  def Find(self, *args):
    self.text.tag_remove('found', '1.0', END)
    target = askstring('Find', 'Search String: ')

    if target:
      index = '1.0'
      while 1:
        index = self.text.search(target, index, nocase=1, stopindex=END)
        if not index: break
        last_index = '%s+%dc' % (index, len(target))
        self.text.tag_add('found', index, last_index)
        index = last_index
      self.text.tag_config('found', foreground='white', background='blue')


def main(root, text, menu_bar):
  object_edit = Edit(text, root)

  edit_menu = Menu(menu_bar)
  edit_menu.add_command(label='Copy', command=object_edit.Copy, accelerator='Ctrl+C')
  edit_menu.add_command(label='Cut', command=object_edit.Cut, accelerator="Ctrl+X")
  edit_menu.add_command(label='Paste', command=object_edit.Paste, accelerator="Ctrl+V")
  edit_menu.add_command(label='Redo', command=object_edit.Redo, accelerator="Ctrl+Y")
  edit_menu.add_command(label='Undo', command=object_edit.Undo, accelerator="Ctrl+Z")
  edit_menu.add_command(label="Find", command=object_edit.Find, accelerator="Ctrl+F")
  edit_menu.add_separator()
  edit_menu.add_command(label="Select All", command=object_edit.Select_All, accelerator="CTRL+A")

  menu_bar.add_cascade(label="Edit", menu=edit_menu)
  
  root.bind_all("<Control-z>", object_edit.Undo)
  root.bind_all("<Control-y>", object_edit.Redo)
  root.bind_all("<Control-f>", object_edit.Find)
  root.bind_all("<Control-a>", object_edit.Select_All)

  object_edit.rightClick.add_command(label='Copy', command=object_edit.Copy)
  object_edit.rightClick.add_command(label='Cut', command=object_edit.Cut)
  object_edit.rightClick.add_command(label='Paste', command=object_edit.Paste)
  object_edit.rightClick.add_separator()
  object_edit.rightClick.add_command(label='Select All', command=object_edit.Select_All)
  object_edit.rightClick.bind("<Control-q", object_edit.Select_All)

  text.bind("Button-3", menu_bar)
  root.config(menu=menu_bar)

if __name__ == "__main__":
  print("please run: 'main.py'.")
    