#Hoạt động 7: Mini project – Ứng dụng Ghi chú công việc (To - do list)
import tkinter as tk
from tkinter import messagebox

# Danh sach luu (noi_dung, da_hoan_thanh)
danh_sach_cong_viec = []


# Cap nhat lai danh sach cong viec tren Listbox
def lam_moi_listbox():
    listbox_cong_viec.delete(0, tk.END)

    for noi_dung, da_hoan_thanh in danh_sach_cong_viec:
        tien_to = "[Da xong] " if da_hoan_thanh else "[Chua xong] "
        listbox_cong_viec.insert(tk.END, tien_to + noi_dung)


# Them cong viec moi
def them_cong_viec():
    noi_dung = bien_cong_viec_moi.get().strip()

    if noi_dung == "":
        messagebox.showerror(
            "Loi",
            "Vui long nhap noi dung cong viec truoc khi them."
        )
        return

    danh_sach_cong_viec.append((noi_dung, False))
    bien_cong_viec_moi.set("")
    lam_moi_listbox()


# Xoa cong viec duoc chon
def xoa_cong_viec():
    lua_chon = listbox_cong_viec.curselection()

    if not lua_chon:
        messagebox.showerror(
            "Loi",
            "Vui long chon mot cong viec trong danh sach de xoa."
        )
        return

    vi_tri = lua_chon[0]
    danh_sach_cong_viec.pop(vi_tri)
    lam_moi_listbox()


# Danh dau cong viec da hoan thanh
def danh_dau_hoan_thanh():
    lua_chon = listbox_cong_viec.curselection()

    if not lua_chon:
        messagebox.showerror(
            "Loi",
            "Vui long chon mot cong viec de danh dau hoan thanh."
        )
        return

    vi_tri = lua_chon[0]
    noi_dung, _ = danh_sach_cong_viec[vi_tri]
    danh_sach_cong_viec[vi_tri] = (noi_dung, True)
    lam_moi_listbox()


# Tao cua so chinh
cua_so = tk.Tk()
cua_so.title("Ung dung Ghi chu cong viec")
cua_so.geometry("420x400")
cua_so.resizable(False, False)

# Bien dieu khien cho o nhap cong viec
bien_cong_viec_moi = tk.StringVar()

# O nhap cong viec
entry_cong_viec = tk.Entry(
    cua_so,
    textvariable=bien_cong_viec_moi,
    width=30
)
entry_cong_viec.grid(
    row=1, column=0, columnspan=2, padx=10, pady=5
)

# Nut Them
tk.Button(
    cua_so,
    text="Them",
    command=them_cong_viec
).grid(row=1, column=2, padx=10, pady=5)

# Danh sach cong viec
listbox_cong_viec = tk.Listbox(
    cua_so,
    width=45,
    height=12
)
listbox_cong_viec.grid(
    row=2, column=0, columnspan=3, padx=10, pady=10
)

# Nut Danh dau hoan thanh
tk.Button(
    cua_so,
    text="Danh dau hoan thanh",
    command=danh_dau_hoan_thanh
).grid(row=3, column=0, padx=10, pady=10)

# Nut Xoa cong viec
tk.Button(
    cua_so,
    text="Xoa cong viec",
    command=xoa_cong_viec
).grid(row=3, column=1, padx=10, pady=10)

# Chay chuong trinh
if __name__ == "__main__":
    cua_so.mainloop()