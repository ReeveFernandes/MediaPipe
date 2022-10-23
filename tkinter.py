from tkinter import *

root = Tk()

root.geometry("400x250")
title = Label(root, text="Just Exercise")
curlB = Button(root, text="Curl", padx=10, pady=10)
squatB = Button(root, text="Squats", padx=10, pady=10)
lungeB = Button(root, text="Lunge", padx=10, pady=10)
pushB = Button(root, text="Push Up", padx=10, pady=10)

curlB.place(x=20, y=0)
squatB.place(x=20, y=20)
lungeB.place(x=40, y=0)
pushB.place(x=40, y=20)

root.mainloop()
