from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
#all functions
def Cut():
    text.event_generate(('<<Cut>>'))
def Copy():
    text.event_generate(('<<Copy>>'))
def Paste():
    text.event_generate(('<<Paste>>'))
def Delet():
    text.event_generate(('<<Delet>>'))
def About():
    showinfo('Notepad','This Notepad is made by Gautam Kumar as a project')
def New():
    global file
    root.title('Untitled - Notepad')
    file=None
    text.delete(1.0,END)
def Open():
    global file
    file=askopenfilename(defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
    if file=='':
        file=None
    else:
        root.title(os.path.basename(file) + ' - Notepad')
        text.delete(1.0,END)
        f = open(file,"r")
        text.insert(1.0,f.read())
        f.close()
def Saveas():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untilted.txt',defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
        if file=='':
            file=None
        else:
            f=open(file,'w')
            f.write(text.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + ' - Notepad')
    else:
        f = open(file, 'w')
        f.write(text.get(1.0, END))
        f.close()
def Statusbar():
    frame1=Frame(root)
    frame1.pack(side=BOTTOM)
    lable1=Label(frame1,text='HI').pack()
def abc():
    print('will be there soon..')
root=Tk()
root.geometry('300x200')

#title of GUI
root.title('Untilted - Notepad')
#icon of Title
root.wm_iconbitmap('notepad.ico')

#menu start
menu=Menu(root)
filemenu=Menu(menu,tearoff=0)
root.config(menu=menu)
menu.add_cascade(label='file',menu=filemenu)

filemenu.add_command(label='New',command=New)
filemenu.add_command(label='Open..',command=Open)
filemenu.add_command(label='Save',command=abc)
filemenu.add_command(label='Save As..',command=Saveas)
filemenu.add_separator()
filemenu.add_command(label='Page Setup..',command=abc)
filemenu.add_command(label='Print..',command=abc)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=quit)

editmenu=Menu(menu,tearoff=0)
menu.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Undo',command=abc)
editmenu.add_separator()
editmenu.add_command(label='Cut',command=Cut)
editmenu.add_command(label='Copy',command=Copy)
editmenu.add_command(label='Paste',command=Paste)
editmenu.add_command(label='Delet',command=Delet)
editmenu.add_separator()
editmenu.add_command(label='Replace...',command=abc)

formatmenu=Menu(menu,tearoff=0)
menu.add_cascade(label='Format',menu=formatmenu)
formatmenu.add_command(label='Word Wrap',command=abc)
formatmenu.add_command(label='Font..',command=abc)

viewmenu=Menu(menu,tearoff=0)
menu.add_cascade(label='View',menu=viewmenu)
viewmenu.add_command(label='Status Bar',command=Statusbar)

helpmenu=Menu(menu,tearoff=0)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='View Help',command=abc)
helpmenu.add_separator()
helpmenu.add_command(label='About Notepad',command=About)

#text:
file=None
text=Text(root,font='lucida 13')
text.pack(expand=True,fill=BOTH)

#forscrollbar

scroll_bar=Scrollbar(text)
scroll_bar1=Scrollbar(text,orient=HORIZONTAL)

scroll_bar.pack(side=RIGHT,fill=Y)
scroll_bar1.pack(side=BOTTOM,fill=X)

scroll_bar.config(command=text.yview)
scroll_bar1.config(command=text.xview)

text.config(yscrollcommand=scroll_bar.set,xscrollcommand=scroll_bar1.set)

root.mainloop()