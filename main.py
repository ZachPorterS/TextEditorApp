from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *

import HelpMenu
import FileMenu
import EditMenu
import FormatMenu

root = Tk()

root.title("TextEditorApp")
root.geometry("300x400+400+400")
root.minsize(width=400, height=400)

text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=2)
text.pack(fill=Y, expand=1)
text.focus_set()

menu_bar = Menu(root)

FileMenu.main(root, text, menu_bar)
EditMenu.main(root, text, menu_bar)
HelpMenu.main(root, text, menu_bar)
FormatMenu.main(root, text, menu_bar)
root.mainloop()