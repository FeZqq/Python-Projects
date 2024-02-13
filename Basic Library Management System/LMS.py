import tkinter as tk

# Functions #

global message 
message = " "

def find():
    f = open("books.txt","r")
    for book in f.readlines():
        if  find_or_remove.get() in book:
            main.insert(tk.END,book + "\n")
            break
        else:
            continue

def remove_book():
    new_database = []
    f = open("books.txt","r")
    for book in f.readlines():
        if find_or_remove.get() in book:
            main.insert(tk.END,"Succsesfully removed" + "\n")
            continue
        else:
            new_database.append(book)
            
    f.close()
    f = open("books.txt","w")
    f.write("")
    f.close()
    f = open("books.txt","a+")
    for book in new_database:
        f.write(book)
    f.close()

        

def show_all():
    books = []
    f = open("books.txt","r")
    for book in f:
        books.append(book)
    f.close()
    i = 0
    for book in books:
        i = i + 1
        main.insert(tk.END,str(i) + "-")
        main.insert(tk.END,book + "\n")


def new_book():
    
    n = name.get()
    a = author.get()
    r = release.get()
    p = page.get()
    if n != "" and a != "" and r != "" and p != "":    
        new_book =  n + " " + a + " " + r + " "+ p
        f = open("books.txt","a+")
        f.write(new_book +"\n")
        f.close()
        main.insert(tk.END,"Succsessfully Added" + " ")
    else:
        message = "You have to fill all of the spaces"
        main.insert(tk.END,message + " ")


# Window Configurations #
window = tk.Tk()
window.title("Library Management System")
window.configure(bg="#527a7a")
window.geometry("800x600")
window.resizable(width=False,height=False)
##########################


# Entries to add,find,remove books #
main = tk.Text(width=97,height=25,bg="#a3c2c2")
name = tk.Entry()
author = tk.Entry()
release = tk.Entry()
page = tk.Entry()
find_or_remove = tk.Entry()

main.place(x=10,y=50)
name.place(x=100,y=470)
author.place(x=100,y=500)
release.place(x=100,y=530)
page.place(x=100,y=560)
find_or_remove.place(x=460 ,y=480)
#####################################


# Button Configurations #
Show_button = tk.Button(text="Show All Books",command=show_all,width=14,height=5)
Add_button = tk.Button(text="Add Book",command=new_book,width=14,height=5)
find_button = tk.Button(text="Find",command=find,width=6,height=2)
remove_button = tk.Button(text="Remove",command=remove_book,width=6,height=2)

Show_button.place(x=680,y=480)
Add_button.place(x=250,y=480 )
find_button.place(x=460,y=520)
remove_button.place(x=530,y=520)
##########################


# Labels #
title_label=tk.Label(text="Book Name / Author / Release Date / Number of Page",bg="#a3c2c2")
name_label = tk.Label(text="Book Name:",bg="#527a7a")
author_label = tk.Label(text="Author Name:",bg="#527a7a")
release_label = tk.Label(text="Release Date:",bg="#527a7a")
page_label = tk.Label(text="Num. of Pages:",bg="#527a7a")
name_label_2 = tk.Label(text="Book Name",bg="#527a7a")

title_label.place(x=10,y=15)
name_label.place(x=25,y=470)
author_label.place(x=17,y=500)
release_label.place(x=25,y=530)
page_label.place(x=10,y=560)
name_label_2.place(x=485,y=455)
##########

window.mainloop()
