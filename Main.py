from logging import root
from Hala import FortuneList
import random
from tkinter import *

window = Tk()
window.geometry("900x500")
window.title('FortuNETeller')

# # Define image
# bg = PhotoImage(file="C:../Coding Tamer/FortuNETeller/fortune.png")

# # Create a canvas
# my_canvas = Canvas(window, width=200, height=100)
# my_canvas.pack(fill="both", expand=True)
# my_canvas.create_image(0,0, image=bg, anchor="nw")

# Label(text="FortuNETeller",font=("Helvetica", 14)).pack()
# Label(text="Karakolda komser senin haberi çok önce aldığını söyledi o yüzden Karakolda komser senin haberi çok önce aldığını söyledi o yüzdenKarakolda komser senin haberi çok önce aldığını söyledi o yüzdenKarakolda komser senin haberi çok önce aldığını söyledi o yüzdenKarakolda komser senin haberi çok önce aldığını söyledi o yüzden").pack()

bg = PhotoImage(file = "C:../Coding Tamer/FortuNETeller/fortune.png")

myL = Label(image=bg)
myL.place(x=0,y=0,relwidth=1,relheight=1)

myT = Label(text="FortuNETeller",font=("Helvetica", 18), fg="black")
myT.pack(pady=50)

# Random Function
Label(text=random.choice(FortuneList),font=("Arial", 14)).pack()

Button(text='Exit',command=lambda: window.quit()).pack(ipadx=5,ipady=5,expand=True)

window.mainloop()
