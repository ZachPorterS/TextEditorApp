from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
from tkinter.messagebox import *

class Edit():
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
        index = self.text.search(target, index, nocase=1, stopindex)