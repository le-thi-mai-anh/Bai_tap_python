# Hoạt động 1:Dictionary cơ bản - khai báo, truy xuất, thêm/sửa/xóa
print("\n========== HOAT DONG 1 ==========")

#Bài tập 1.1 - Khai báo & truy xuất
print("[Bài tập 1.1 - Khai báo & truy xuất]")
sinh_vien = {
 "ho_ten": "Lê Thị Mai Anh ",
 "nam_sinh": 2006,
 "diem_tb": 9.0
}
print(sinh_vien["ho_ten"]) # truy xuat theo khoa
print(sinh_vien.get("diem_tb")) # truy xuat an toan bang get()
print(sinh_vien.get("lop", "Chua co")) # get() voi gia tri mac dinh neu khong co khoa

#Bài tập 1.2 - Thêm, sửa , xóa
print("[Bài tập 1.2 - Thêm,sửa ,xóa]")
sinh_vien["lop"] = "CNTTDH14C1"
sinh_vien["diem_tb"] = 9.0

print(sinh_vien)

diem_cu = sinh_vien.pop("diem_tb")

print(sinh_vien, "- diem da xoa:", diem_cu)

sinh_vien.update({
    "nam_sinh": 2006,
    "email": "lma146626@gmail.com"
})

print(sinh_vien)

#Hoạt động 2: Duyệt Dictionary bằng for - keys/values/items
print("\n========== HOAT DONG 2  ==========")
# Hoat dong 2: Duyet Dictionary bang for - keys/values/items

diem_mon_hoc = {
    "Toan": 9.0,
    "Ly": 9.5,
    "Hoa": 9.0,
    "Van": 8.5
}

# Duyet cac key (ten mon hoc)
for mon in diem_mon_hoc.keys():
    print(mon)

# Duyet cac value (diem)
for diem in diem_mon_hoc.values():
    print(diem)

# Duyet ca key va value
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")

# Tinh tong diem
tong_diem = 0

for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem

# Tinh diem trung binh
print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))

#Hoạt động 3: Dictionary comprehension & giới thiệu Set
print("\n========== HOAT DONG 3 ==========")

#Bài tập 3.1 - Dictionary comprehension:
print("[Bài tập 3.1 - Dictionary comprehension]")
diem_mon_hoc = {
    "Toan": 9.0,
    "Ly": 9.5,
    "Hoa": 9.0,
    "Van": 8.5
}

# Cong them 0.5 diem cho tat ca cac mon
diem_cong_diem = {
    mon: round(diem + 0.5, 2)
    for mon, diem in diem_mon_hoc.items()
}

print(diem_cong_diem)

# Chuyen ten mon hoc thanh chu in hoa
ten_mon_viet_hoa = {
    mon.upper(): diem
    for mon, diem in diem_mon_hoc.items()
}

print(ten_mon_viet_hoa)

# Bai tap 3.2 - So sanh nhanh voi Set
print("[Bai tap 3.2 - So sanh nhanh voi Set]")
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}

# Giao: mon hoc chung cua 2 hoc ky
print(mon_hoc_ky1 & mon_hoc_ky2)

# Hop: tat ca mon hoc cua 2 hoc ky
print(mon_hoc_ky1 | mon_hoc_ky2)

# Hieu: mon chi co o hoc ky 1
print(mon_hoc_ky1 - mon_hoc_ky2)
