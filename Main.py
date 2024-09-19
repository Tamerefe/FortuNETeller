import random
from tkinter import *
from tkinter import ttk
from Hala import FortuneList  # Assuming this is correctly imported from your module

# Create the main application window
window = Tk()
window.geometry("1000x600")
window.title('FortuNETeller')

# Load and set the background image
bg = PhotoImage(file="../FortuNETeller/fortune.png")
myL = Label(window, image=bg)
myL.place(x=0, y=0, relwidth=1, relheight=1)

# Title label
myT = Label(window, text="FortuNETeller", font=("Helvetica", 24, "bold"), fg="#ffcc00", bg="#333333")
myT.pack(pady=20)

# Frame to hold the fortune text and buttons
frame = Frame(window, bg="#333333")
frame.pack(pady=20)

# Label to display the fortune text
fortune_label = Label(frame, text="Click the button to see your fortune!", font=("Arial", 16), wraplength=600, bg="#ffffff", fg="#333333", padx=20, pady=20, borderwidth=2, relief="solid")
fortune_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

# Function to update the fortune text
def tell_fortune():
    random_fortune = random.choice(FortuneList)
    fortune_label.config(text=random_fortune)

# Styling for buttons
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 14), padding=10)
style.map('TButton', foreground=[('active', '#ffcc00')], background=[('active', '#333333')])

# Button to get a new fortune with cursor change on hover
fortune_button = ttk.Button(frame, text='Düğmeye Bas Ve Kaderini Öğren', command=tell_fortune, style='TButton', cursor="hand2")
fortune_button.grid(row=1, column=0, padx=20, pady=20)

# Exit button with cursor change on hover
exit_button = ttk.Button(frame, text='Çıkış', command=window.quit, style='TButton', cursor="hand2")
exit_button.grid(row=1, column=1, padx=20, pady=20)

# Start the main loop
window.mainloop()
