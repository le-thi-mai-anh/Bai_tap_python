#Hoạt động 6: messagebox – validate dữ liệu form
import tkinter as tk
from tkinter import messagebox


def xu_ly_submit():
    ho_ten = entry_ho_ten.get().strip()
    tuoi_nhap = entry_tuoi.get().strip()
    email = entry_email.get().strip()

    # Kiem tra ho ten
    if ho_ten == "":
        messagebox.showerror("Loi", "Ho ten khong duoc de trong.")
        return

    # Kiem tra tuoi bang try-except
    try:
        tuoi = int(tuoi_nhap)
    except ValueError:
        messagebox.showerror("Loi", "Tuoi phai la mot so nguyen.")
        return

    # Kiem tra email
    if "@" not in email:
        messagebox.showerror(
            "Loi",
            "Email khong hop le (thieu ky tu @)."
        )
        return

    # Thong bao thanh cong
    messagebox.showinfo(
        "Thanh cong",
        f"Da nhan thong tin: {ho_ten} - {tuoi} tuoi - {email}"
    )


cua_so = tk.Tk()
cua_so.title("Form nhap thong tin")
cua_so.geometry("400x280")
cua_so.resizable(False, False)

# O nhap ho ten
tk.Label(cua_so, text="Ho ten:").grid(
    row=0, column=0, padx=10, pady=10, sticky="w"
)
entry_ho_ten = tk.Entry(cua_so, width=25)
entry_ho_ten.grid(row=0, column=1, padx=10, pady=10)

# O nhap tuoi
tk.Label(cua_so, text="Tuoi:").grid(
    row=1, column=0, padx=10, pady=10, sticky="w"
)
entry_tuoi = tk.Entry(cua_so, width=25)
entry_tuoi.grid(row=1, column=1, padx=10, pady=10)

# O nhap email
tk.Label(cua_so, text="Email:").grid(
    row=2, column=0, padx=10, pady=10, sticky="w"
)
entry_email = tk.Entry(cua_so, width=25)
entry_email.grid(row=2, column=1, padx=10, pady=10)

# Nut Submit
nut_submit = tk.Button(
    cua_so,
    text="Submit",
    command=xu_ly_submit
)
nut_submit.grid(row=3, column=0, columnspan=2, pady=15)

cua_so.mainloop()
