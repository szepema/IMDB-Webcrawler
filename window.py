import tkinter

root = tkinter.Tk()

#középre helyezi az ablakot
root.eval('tk::PlaceWindow . center')

#az ablak nevét határozza meg
root.title("IMDB Search")

#az input box paraméterei

#az input box adatinak bekérése
def myClick():
    sName.get()


#a szöveg, input box és gomb paraméteri
sName = tkinter.Entry(root, width=50, borderwidth=5, font=('Arial', 12))
myLabel = tkinter.Label(root, text="Please enter the search term", font=('Arial', 16))
myButton = tkinter.Button(root, text="Search", command=myClick, font=('Arial', 14))

#ablakon belüli elhelyezés
myLabel.grid(row=0, column=0, pady=5)
sName.grid(row=1, column=0, padx=20, pady=5)
myButton.grid(row=2, column=0, pady=5)


root.mainloop()