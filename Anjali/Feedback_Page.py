from tkinter import *
from tkinter import messagebox

def submit_feedback():
    feedback = text_feedback.get("1.0", "end-1c")
    if feedback.strip() == "":
        messagebox.showwarning("Warning", "Please provide feedback!")
    else:
        messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
        # Here you can add code to save the feedback to a file or database

# Create the main window
root = Tk()
root.title("Feedback Form")
root.geometry("950x500")
root.minsize(width=950, height=500)
root.maxsize(width=100, height=500)

Feedback= Label(root, text='Feedback', fg='black',font=('Times', 23, 'bold'))
Feedback.place(x=350, y=5)
# Create a label
name_feedback=Label(root, text="Name:",fg='black', font=('Times', 12,'bold'))
name_feedback.place(x=300,y=75)
Email_feedback=Label(root, text="Email:",fg='black', font=('Times', 12,'bold'))
Email_feedback.place(x=300,y=135)
message_feedback=Label(root, text="Message: ",fg='black', font=('Times', 12,'bold'))
message_feedback.place(x=300,y=200)

# Create a text box for feedback
text_feedback = Text(root, height=1.5, width=40,fg='black', border=0, bg='#D9D9D9', font=('Times', 11))
text_feedback.place(x=300,y=100)
text_feedback_Emailbox = Text(root, height=1.5, width=40,fg='black', border=0, bg='#D9D9D9', font=('Times', 11))
text_feedback_Emailbox.place(x=300,y=160)

message_feedback_box = Text(root, height=5, width=40,fg='black', border=0, bg='#D9D9D9', font=('Times', 11))
message_feedback_box.place(x=300,y=230)

# Create a submit button
btn_submit = Button(root, text='Submit Feedback',fg='black',bg='#276B80', command= submit_feedback)
btn_submit.place(x=380,y=355)

def show_features():
    # Create a new window to display features
    features_window = Toplevel(root)
    features_window.title("Features")
    features_window.geometry("200x200+800+213")

    # Add buttons for features
    upcoming_events_btn = Button(features_window, text="Upcoming Events")
    upcoming_events_btn.pack(pady=5, fill=X, expand=True)

    attendance_btn = Button(features_window, text="Attendance")
    attendance_btn.pack(pady=5, fill=X, expand=True)

    events_calendar_btn = Button(features_window, text="Events Calendar")
    events_calendar_btn.pack(pady=5, fill=X, expand=True)

    more_btn = Button(features_window, text="More")
    more_btn.pack(pady=5, fill=X, expand=True)


def toggle_menu():
    if features_button.winfo_viewable():
        features_button.pack_forget()
    else:
        features_button.place(x=10,y=2)

# Create a button to show features
features_button = Button(root, text="☰", command=show_features)
features_button.place(x=900,y=10)

notification_button = Button(root, text="🔔")#command=show_features
notification_button.place(x=870,y=10)


root.mainloop()