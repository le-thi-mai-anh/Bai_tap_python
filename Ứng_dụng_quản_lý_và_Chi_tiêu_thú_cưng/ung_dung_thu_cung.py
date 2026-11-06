import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import csdl_thu_cung as db

DANH_SACH_LOAI = ["Cho", "Meo", "Chim", "Ca", "Khac"]

class UngDungThuCung(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Chi tieu Thu cung")
        self.geometry("580x500")
        self.resizable(False, False)

        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        # Khung nhập
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Ten thu cung:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ten = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ten.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Loai:").grid(row=1, column=0, sticky="w", pady=5)
        self.chon_loai = ttk.Combobox(khung_nhap, values=DANH_SACH_LOAI, width=27, state="readonly")
        self.chon_loai.current(0)
        self.chon_loai.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Chi phi (VNĐ):").grid(row=2, column=0, sticky="w", pady=5)
        self.o_nhap_chi_phi = tk.Entry(khung_nhap, width=30)
        self.o_nhap_chi_phi.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Them chi phi", command=self.xu_ly_them).grid(
            row=3, column=0, columnspan=2, pady=10
        )

        # Khung danh sách
        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox = tk.Listbox(khung_danh_sach, width=75, height=12)
        self.listbox.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=thanh_cuon.set)

        # Khung nút thao tác
        khung_nut = tk.Frame(self)
        khung_nut.pack(pady=10)

        tk.Button(khung_nut, text="Danh dau da thanh toan", command=self.xu_ly_danh_dau).grid(row=0, column=0, padx=5)
        tk.Button(khung_nut, text="Xoa mục", command=self.xu_ly_xoa).grid(row=0, column=1, padx=5)
        tk.Button(khung_nut, text="Thong ke chi phi", command=self.xu_ly_thong_ke).grid(row=0, column=2, padx=5)

    def tai_lai_danh_sach(self):
        self.listbox.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo()
        for item in self.danh_sach_hien_tai:
            id_tc, ten, loai, chi_phi, da_tt = item
            trang_thai = "[Da tt]" if da_tt == 1 else "[Chua tt]"
            self.listbox.insert(tk.END, f"{trang_thai} {ten} ({loai}) - Chi phi: {chi_phi:,.0f} VNĐ")

    def xu_ly_them(self):
        ten = self.o_nhap_ten.get().strip()
        loai = self.chon_loai.get()
        chi_phi_str = self.o_nhap_chi_phi.get().strip()

        if not ten or not chi_phi_str:
            messagebox.showerror("Loi", "Vui long nhap day du ten va chi phi.")
            return

        try:
            chi_phi = float(chi_phi_str)
        except ValueError:
            messagebox.showerror("Loi", "Chi phi phai la mot so hop le.")
            return

        db.them_thu_cung(ten, loai, chi_phi)
        self.o_nhap_ten.delete(0, tk.END)
        self.o_nhap_chi_phi.delete(0, tk.END)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thanh cong", f"Da them chi phi cho {ten}")

    def xu_ly_xoa(self):
        lua_chon = self.listbox.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon 1 dong de xoa.")
            return
        id_tc = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_thu_cung(id_tc)
        self.tai_lai_danh_sach()

    def xu_ly_danh_dau(self):
        lua_chon = self.listbox.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon 1 dong.")
            return
        id_tc = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.danh_dau_thanh_toan(id_tc)
        self.tai_lai_danh_sach()

    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_chi_phi()
        if not du_lieu:
            messagebox.showinfo("Thong bao", "Chua co du lieu de thong ke.")
            return

        loai = [d[0] for d in du_lieu]
        tong_tien = [d[1] for d in du_lieu]

        plt.figure(figsize=(6, 4))
        plt.bar(loai, tong_tien, color="orange")
        plt.title("Tong chi phi theo loai thu cung")
        plt.xlabel("Loai")
        plt.ylabel("Chi phi (VNĐ)")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = UngDungThuCung()
    app.mainloop()