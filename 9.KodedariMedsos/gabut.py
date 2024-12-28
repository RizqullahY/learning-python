import tkinter
main_window = tkinter.Tk()

pertanyaan = tkinter.Label(main_window, text="apakah kamu gila?")

tombol1 = tkinter.Button(main_window, text="iya")
tombol2 = tkinter.Button(main_window, text="tidak")



# method positioning
pertanyaan.pack()
tombol1.pack()
tombol2.pack()

# menampilkan GUI
main_window.mainloop()