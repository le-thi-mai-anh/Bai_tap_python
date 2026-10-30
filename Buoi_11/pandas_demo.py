import pandas as pd

# Bai tap 2.1: Doc CSV va xem tong quan
df = pd.read_csv("diem_sinh_vien.csv")

print("5 dong dau:")
print(df.head())

print("Kich thuoc:")
print(df.shape)

print("Danh sach ten cot:")
print(df.columns.tolist())

# Bai tap 2.2: Thong ke theo mon hoc
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()

print("Diem trung binh theo mon hoc:")
print(diem_trung_binh_mon)

print("Diem trung binh toan bo:", df["diem"].mean())
print("Diem cao nhat:", df["diem"].max())
print("Diem thap nhat:", df["diem"].min())

# Bai tap 2.3: Tinh diem trung binh tung sinh vien
diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)

print("Diem trung binh tung sinh vien:")
print(diem_tb_sv)

# Loc sinh vien dat va khong dat
sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]

sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\nSinh vien dat:")
print(sinh_vien_dat)

print("\nSinh vien khong dat:")
print(sinh_vien_khong_dat)
X