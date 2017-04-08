from tkinter import *
from tkinter import filedialog
#from tkinter import messagebox
master = Tk()
master.title("ItsSimple")
master.geometry("400x300")

text = Text(master, width=400, height=300, font=("Adobe Source Code Pro", 12), highlightthickness=2, bd=1)
text.pack()


# methods

def new():
    ans = messagebox.askquestion(title="Save File",message="Would you like to save this file")
    if ans == 'yes' :
        #save_as()
        messagebox.showwarning(title="About File",message="file saved")

    delete_all()

def opennewfile():
    pass
def open_file():
    sh = messagebox.askquestion(title="Is File Saved?",message="Have you saved the current file?")
    if sh == 'yes':
        file = filedialog.askopenfile()
        text.insert(INSERT, file.read())
    else:
        messagebox.showwarning(title="Save file",message="save the current file first")
        save_as()
        file = filedialog.askopenfile()
        text.insert(INSERT,file.read())



def save_as():
    path = filedialog.asksaveasfilename()
    file_handler = open(path, 'w')
    file_handler.write(text.get("1.0", END))


def rename():
    pass


def close():
    save_as()
    master.quit()


def cut():
    master.clipboard_clear()
    text.clipboard_append(string=text.selection_get())
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)


def copy():
    master.clipboard_clear()
    text.clipboard_append(string=text.selection_get())


def paste():
    text.insert(INSERT, master.clipboard_get())


def delete():
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)


def select_all():
    text.tag_add(SEL,"1.0",END)


def delete_all():
    text.delete(1.0,END)


# file menu
menu = Menu(master)
master.config(menu=menu)
file_menu = Menu(menu)

menu.add_cascade(label="File", menu= file_menu)
file_menu.add_command(label="New",command=new)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save",command=save_as)
file_menu.add_command(label="Rename",command=rename)
file_menu.add_separator()
file_menu.add_command(label="Close",command=close)


# edit menu

edit_menu = Menu(menu)

menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Undo",command=text.edit_undo())
edit_menu.add_command(label="Redo",command=text.edit_redo())
edit_menu.add_separator()
edit_menu.add_command(label="Cut",command=cut)
edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_command(label="Paste",command=paste)
edit_menu.add_command(label="Delete",command=delete)
edit_menu.add_separator()
edit_menu.add_command(label="Select All",command=select_all)
master.mainloop()
