import tkinter
import tkinter.messagebox
from tkinter import *

import cryptocode
from PIL import ImageTk

window = Tk()
window.title("Top Secret Notes")
window.geometry("400x600")
window.resizable(height=False, width=False)


app_logo = ImageTk.PhotoImage(file="top_secret1.png")

my_font = ("Arial",12,"bold")




def encode_note():

    msg = msg_text.get("1.0",END)

    key = key_entry.get()

    title= msg_title_text.get("1.0",END)

    encoded = cryptocode.encrypt(msg, key)

    file = open("Encrypt Messages.txt", "a")
    file.write("\n\n")
    file.write(f"{title}\n{encoded}")
    file.close()

    msg_text.delete("1.0", END)
    msg_title_text.delete("1.0", END)
    key_entry.delete("0", END)

def decode_note():

    encode_msg = msg_text.get("1.0",END)
    key = key_entry.get()
    decode_msg = cryptocode.decrypt(encode_msg, key)

    if decode_msg == False:

        tkinter.messagebox.showerror("Wrong Key","The key is incorrect!")



    else:
        msg_text.delete("1.0",END)
        key_entry.delete("0", END)
        msg_text.insert(tkinter.END,decode_msg)


logo_label = Label(image=app_logo,)
logo_label.pack(side="top")

msg_title_label = Label(text="Title", font=my_font)
msg_title_label.place(x=200-19, y=120)


msg_title_text = Text(window, height=1, width=35)
msg_title_text.place(x=200-142,y=160)


msg_label = Label(text="Your Secret", font=my_font)
msg_label.place(x=200-47.5,y=200)
msg_label.update()



msg_text = Text(window, height=10, width=35, bg="light yellow")
msg_text.place(x=200-142,y=240)


key_label = Label(text="Enter Master Key", font=my_font)
key_label.place(x=200-68,y=420)



key_entry = Entry(width=47)
key_entry.place(x=200-143,y=450)



encrypt_button = Button(text="Save & Encrypt",command=encode_note)
encrypt_button.place(x=200-45.5,y=480)


decrypt_button = Button(text="Decrypt",command=decode_note)
decrypt_button.place(x=200-26,y=510)







window.mainloop()