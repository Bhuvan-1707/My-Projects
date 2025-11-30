import tkinter as tk

# .pack()
# .place()
# .grid()

window = tk.Tk()

frame_1 = tk.Frame(master=window,height=200,width=50,bg="red")
frame_2 = tk.Frame(master=window,height=100,width=50,bg="white")
frame_3 = tk.Frame(master=window,height=50,width=50,bg="blue")

frame_1.pack(fill=tk.X)
frame_2.pack(fill=tk.X)
frame_3.pack(fill=tk.X)


window.mainloop()