# HOAT DONG 7: MINI PROJECT
print("\n ====== HOẠT ĐỘNG 7 ======")
# Tao Dictionary quan ly diem
# Key: Ho ten sinh vien
# Value: Danh sach diem

quan_ly_diem = {
    "Lê Thị Mai Anh": [9.0, 9.5, 9.0],
    "Đinh Bảo Linh": [6.0, 6.5, 5.5],
    "Đinh Đăng Hải Anh": [6.0, 5.5, 4.5]
}

# Them sinh vien moi
quan_ly_diem["Bùi Nhật Tân"] = [8.0, 8.0, 8.5]

# Sua diem mon dau tien cua Đinh Bảo Linh
quan_ly_diem["Đinh Bảo Linh"][0] = 7.0

# Tao Dictionary de luu diem trung binh
diem_trung_binh = {}

# Duyet qua tung sinh vien
for ho_ten, danh_sach_diem in quan_ly_diem.items():

    # Tinh diem trung binh
    diem_trung_binh[ho_ten] = round(
        sum(danh_sach_diem) / len(danh_sach_diem),
        2
    )

# In bang diem trung binh
print("BANG DIEM TRUNG BINH:")

for ho_ten, dtb in diem_trung_binh.items():

    # Kiem tra co dat loai Gioi hay khong
    dat_loai_gioi = dtb >= 8.0

    print(
        f"{ho_ten:<20} - DTB: {dtb:<5} - Dat loai Gioi? {dat_loai_gioi}"
    )