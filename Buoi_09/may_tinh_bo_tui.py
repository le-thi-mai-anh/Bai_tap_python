# Bài tập mở rộng - Máy tính bỏ túi
import tkinter as tk
from tkinter import messagebox
import re


# Ham them ky tu vao o hien thi
def them_ky_tu(ky_tu):
    hien_thi.insert(tk.END, ky_tu)


# Ham xoa toan bo bieu thuc
def xoa():
    hien_thi.delete(0, tk.END)


# Ham thuc hien phep tinh
def tinh_ket_qua():
    bieu_thuc = hien_thi.get().strip()

    if bieu_thuc == "":
        messagebox.showerror("Loi", "Vui long nhap bieu thuc!")
        return

    # Chi cho phep so, dau cham, phep tinh va dau ngoac
    if not re.fullmatch(r"[0-9+\-*/(). ]+", bieu_thuc):
        messagebox.showerror("Loi", "Bieu thuc khong hop le!")
        return

    try:
        ket_qua = eval(bieu_thuc, {"__builtins__": {}}, {})
        hien_thi.delete(0, tk.END)
        hien_thi.insert(0, str(ket_qua))

    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho 0!")

    except (SyntaxError, TypeError, ValueError):
        messagebox.showerror("Loi", "Bieu thuc khong hop le!")


# Tao cua so
cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("320x400")
cua_so.resizable(False, False)

# O hien thi bieu thuc va ket qua
hien_thi = tk.Entry(
    cua_so,
    font=("Arial", 18),
    justify="right",
    width=22
)
hien_thi.grid(
    row=0, column=0, columnspan=4,
    padx=10, pady=15
)

# Danh sach cac phim may tinh
cac_phim = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Tao cac nut bam
for phim, hang, cot in cac_phim:
    if phim == "=":
        nut = tk.Button(
            cua_so,
            text=phim,
            font=("Arial", 14),
            width=5,
            height=2,
            command=tinh_ket_qua
        )
    else:
        nut = tk.Button(
            cua_so,
            text=phim,
            font=("Arial", 14),
            width=5,
            height=2,
            command=lambda k=phim: them_ky_tu(k)
        )

    nut.grid(
        row=hang, column=cot,
        padx=4, pady=4
    )

# Nut xoa bieu thuc
tk.Button(
    cua_so,
    text="C - Xoa",
    font=("Arial", 12),
    command=xoa
).grid(
    row=5, column=0, columnspan=4,
    sticky="ew", padx=8, pady=8
)

# Chay chuong trinh
if __name__ == "__main__":
    cua_so.mainloop()
