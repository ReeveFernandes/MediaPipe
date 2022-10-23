import tkinter

root = tkinter.Tk()


root.title("Just Exercise")
root.geometry("500x500")

#Configure the rows and columns
tkinter.Grid.rowconfigure(root,0,weight=1)
tkinter.Grid.rowconfigure(root,1,weight=1)
tkinter.Grid.columnconfigure(root,0,weight=1)
tkinter.Grid.columnconfigure(root,1,weight=1)





#create 4 buttons
curls=tkinter.Button(root,text="CURLS COUNTER", )
curls.grid(sticky="nsew")
push=tkinter.Button(root,text="PUSH UPS COUNTER")
push.grid(sticky="nsew")
squats=tkinter.Button(root,text="SQUATS COUNTER")
squats.grid(sticky="nsew")
lunges=tkinter.Button(root,text="LUNGES COUNTER")
lunges.grid(sticky="nsew")


#Grid the buttons onto the screen

curls.grid(row=0,column=0)
push.grid(row=0, column=1)
squats.grid(row=1,column=0)
lunges.grid(row=1,column=1)



root.mainloop()
