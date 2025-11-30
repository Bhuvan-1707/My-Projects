import tkinter as tk

# Window of the Application
window = tk.Tk()
window.title("Math-Pix")

frame_a = tk.Frame(master=window)

button = tk.Button(frame_a,text="Click here!",
                   fg="yellow",
                   bg='blue',
                   width=10,
                   height=5)


button.pack()

entry = tk.Entry(frame_a,fg="yellow", bg="blue", width=50)
entry.pack()


label = tk.Label(window,text="Hello",
                 fg="white",
                 bg='black',
                 width=30,
                 height=20)

label.pack()

textbox = tk.Text()
textbox.pack()

frame_a.pack()

window.mainloop()