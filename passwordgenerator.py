from tkinter import*
from random import randint
from tkinter import messagebox

root = Tk()
root.configure(bg="darkolivegreen")
root.title("Password Generator")
root.iconbitmap(r"C:\Users\Administrator\OneDrive\Pictures\Meme Folder\PG2.ico")
root.geometry("500x500")

#This enables the user to press the enter key to generate a password
def on_button_click(event=None):
    """Function to handle button click event."""
    new_rand()

#Generates a random password
def new_rand():
    pw_entry.delete(0, END)

    pw_length = int(entry_box.get())

    my_password = ""

    for i in range(pw_length):
        my_password += chr(randint(33, 126))  

    pw_entry.insert(0, my_password)

#Copies the generated password to the clipboard
def clipper():
    root.clipboard_clear()

    root.clipboard_append(pw_entry.get())

    messagebox.showinfo("Copied to Clipboard!", "Your password has been copied to the clipboard.")

#Label frame for the entry box
lf = LabelFrame(root, text="How Many Characters?", padx=20, pady=20, bg="khaki", fg="burlywood4")
lf.pack(pady=20)

#Creates entry box for the designated password length
entry_box = Entry(lf, width=10, font=("Arial", 24), justify="center", bg="white", fg="burlywood4")
entry_box.pack(pady=20, padx=20) 

#Creates entry box for our returned password
pw_entry = Entry(root, width=30, font=("Arial", 24), justify="center", border=0, bg="khaki", fg="burlywood4")
pw_entry.insert(0, "Your Password Will Appear Here")
pw_entry.pack(pady=20)

#Creates a frame for the buttons
button_frame = Frame(root, bg="darkolivegreen")
button_frame.pack(pady=20)

button = Button(button_frame, text="Generate Password", command=new_rand, bg="khaki1", fg="burlywood4", activeforeground="teal")
button.grid(row=0, column=0, padx=10)

clip_button = Button(button_frame, text="Copy to Clipboard", command=clipper, bg="khaki1", fg="burlywood4", activeforeground="teal")
clip_button.grid(row=0, column=1, padx=10)
root.bind('<Return>', on_button_click) 
root.mainloop() 