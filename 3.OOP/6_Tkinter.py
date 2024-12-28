# import tkinter
# main_window = tkinter.Tk()

# label1 = tkinter.Label(main_window, text="label1")
# label2 = tkinter.Label(main_window, text="label2")


# tombol1 = tkinter.Button(main_window, text="tombol1")
# tombol2 = tkinter.Button(main_window, text="tombol2")


# # method positioning
# label1.pack()
# label2.pack()
# tombol1.pack()
# tombol2.pack()

# # menampilkan GUI
# main_window.mainloop()


import tkinter
main_window = tkinter.Tk()

def iya():
    label1=tkinter.Label(main_window,text="ok")
    label1.pack()
# def tidak():
#     label2=tkinter.Label(main_window,text="ok")
#     label2.pack()

pertanyaan = tkinter.Label(main_window, text="apakah kamu gila?\n")

tombol1 = tkinter.Button(main_window, text="iya\n",command=iya)
tombol2 = tkinter.Button(main_window, text="tidak\n")



# method positioning
pertanyaan.pack()
tombol1.pack()
tombol2.pack()

# menampilkan GUI
main_window.mainloop()