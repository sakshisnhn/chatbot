from tkinter import *

# GUI function
def GUI():
    gui=Tk()
    # seting title for the windows
    gui.title("chatbot")
    #seting size for the window
    gui.geometry("390x450")

    # text space to display message
    chatlog=Text(gui,bg="black")
    chatlog.config(state=DISABLED)

    # creating button to send messages
    sendbutton= Button(gui,bg="orange",fg="red",text="SEND")

    # textbox to type messages
    textbox=Text(gui,bg="white")

    # place the component in the window
    chatlog.place(x=6,y=6,height=386,width=370)
    textbox.place(x=6,y=401,height=20,width=265)
    sendbutton.place(x=300,y=401,height=20,width=50)

    # to keep window in loop
    gui.mainloop()

if __name__=="__main__":
    GUI()