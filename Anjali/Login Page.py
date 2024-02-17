from tkinter import *
from PIL import Image, ImageTk 
from tkinter import messagebox 
def signin():
    username=user.get()
    Password=pw.get()
    if username =='admin' and  Password == '1234':
        screen=Toplevel(root)
        screen.title('App')
        screen.geometry('925x500+300+200')
        screen.config(bg='white')
        Label(screen,text='Welcome TO KASA Project!',bg='#fff', font=('Calibri(Body)',50,'bold')).pack(expand=True)
        screen.mainloop()
        
    elif username != 'admin' and Password == '1234':
        error_screen = Toplevel(root)
        error_screen.title("Invalid Username and Password")
        error_screen.geometry('400x400+400+300')
        Label(error_screen, text="Invalid username and password").pack()
        error_screen.mainloop()

    elif Password != "1234":
        error_screen = Toplevel(root)
        error_screen.title("Invalid Password")
        error_screen.geometry('400x400+400+300')
        Label(error_screen, text="Invalid password").pack()
        error_screen.mainloop()

    elif username != 'admin':
        error_screen = Toplevel(root)
        error_screen.title("Invalid Username")
        error_screen.geometry('400x400+400+300')
        Label(error_screen, text="Invalid username").pack()
        error_screen.mainloop()
    # elif username!='admin' and Password=='1234' :
    #     messagebox.showerror("Invalid username and password ") 
    # elif  Password!="1234":
    #     messagebox.showerror("Invalid password ")
    # elif username!='admin':
    #      messagebox.showerror("Invalid username ")


            # print('Kasa College Event Management System')



def on_enter_username(e):
    user.delete(0, 'end')

def on_leave_username(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

def on_enter_password(e):
    pw.delete(0, 'end')

def on_leave_password(e):
    name = pw.get()
    if name == '':
        pw.insert(0, 'Password')

root = Tk()
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(0, 0)

image = Image.open('KASA.png')
img = ImageTk.PhotoImage(image)
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=500, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI light', 23, 'bold'))
heading.place(x=100, y=5)

# create username entry box
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter_username)
user.bind('<FocusOut>', on_leave_username)
# user.bind('<Key>', on_enter_username )

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# for password
pw = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11), show='*')
pw.place(x=30, y=150)
pw.insert(0, 'Password')
pw.bind('<FocusIn>', on_enter_password)
pw.bind('<FocusOut>', on_leave_password)
# pw.bind('<Key>', on_enter_password)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# create a button for Sign in
btn = Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin)
btn.place(x=35, y=204)

# create label for Don't have an account
lbl = Label(frame, text="Don't Have An Account?", fg='black', bg='white', font=('Arial', 9))
lbl.place(x=40, y=260)

# create Sign up button
sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=180, y=260)

root.mainloop()