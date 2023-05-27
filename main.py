from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

hunians = []
hunians.append(Apartemen("Talitha Syahla", 3, 3, "Jalan Durian Blok E-160"))
hunians.append(Rumah("Park Jimin", 5, 2, "Jalan Semangka Blok J-131"))
hunians.append(Indekos("PD Nim", "Kim Taehyung", "Jalan Strawberry Blok T-123"))
hunians.append(Rumah("Min Yoongi", 4, 1, "Jalan Jeruk Blok Y-93"))
hunians.append(Apartemen("Park Jeongwoo", 2, 3, "Jalan Anggur Blok W-289"))

root = Tk()
root.title("Praktikum DPBO Python")
root.geometry("420x420")

Landing = Label(root, text="Welcomee!", font=("Arial", 18), padx=10, pady=10)
Landing.pack(padx=10, pady=10)

picture = ImageTk.PhotoImage(Image.open("assets/pict1.jpg").resize((200,200)))

pict = Label(root, image=picture, padx=50, pady=50)
pict.pack(padx=0, pady=25)

page_residen = Button(root, text="Lihat List Residen Disini!", command=lambda: daftarHunian(), padx=15, pady=15, width=50)
page_residen.pack()


def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_alamat() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w")

    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)

def daftarHunian():
    root.destroy()
    
    list = Tk()
    list.title("Daftar Residen")
    
    frame = LabelFrame(list, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)
    
    opts = LabelFrame(list, padx=10, pady=10)
    opts.pack(padx=10, pady=10)
    
    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)
    
    b_exit = Button(opts, text="Exit", command=list.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

root.mainloop()