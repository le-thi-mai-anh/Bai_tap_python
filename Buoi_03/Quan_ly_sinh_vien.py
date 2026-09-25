# HOẠT ĐỘNG 6 - MINI PROJECT 1
# QUẢN LÝ DANH SÁCH SINH VIÊN BẰNG LIST
print("\n========== HOAT DONG 6 ==========")
print("[ QUẢN LÝ DANH SACGS SIINH VIÊN BẰNG LIST]")

# Mỗi sinh viên được lưu dưới dạng Tuple:
# (điểm, tên)
#
# Ví dụ:
# (8.5, "An")
#
# Trong đó:
# 8.5  -> điểm
# "An" -> tên sinh viên


# 1. TẠO DANH SÁCH SINH VIÊN
print("[# TẠO DANH SÁCH SINH VIÊN]")

danh_sach_sv = [
    (8.5, "An"),
    (7.0, "Binh"),
    (9.2, "Chi"),
    (6.5, "Dung")
]

print("========== DANH SACH BAN DAU ==========")

for diem, ten in danh_sach_sv:
    print(f"Sinh vien: {ten} - Diem: {diem}")


# 2. THÊM SINH VIÊN MỚI
print("[# 2. THÊM SINH VIÊN MỚI ]")

# Thêm sinh viên Em có điểm 8.0

sinh_vien_moi = (8.0, "Em")

danh_sach_sv.append(sinh_vien_moi)

print("\n========== SAU KHI THEM SINH VIEN ==========")

for diem, ten in danh_sach_sv:
    print(f"Sinh vien: {ten} - Diem: {diem}")


# 3. XÓA MỘT SINH VIÊN
print("[# 3. XÓA MỘT SINH VIÊN]")

# Xóa chính xác sinh viên có điểm 7.0 và tên Binh

sinh_vien_xoa = (7.0, "Binh")

danh_sach_sv.remove(sinh_vien_xoa)

print("\n========== SAU KHI XOA BINH ==========")

for diem, ten in danh_sach_sv:
    print(f"Sinh vien: {ten} - Diem: {diem}")


# ==========================================================
# 4. SỬA ĐIỂM SINH VIÊN
print("# 4. SỬA ĐIỂM SINH VIÊN ]")

# Tuple không thể sửa trực tiếp.
# Vì vậy ta thay Tuple cũ bằng Tuple mới.
#
# Sinh viên ở vị trí 0 là An.
# Đổi điểm của An từ 8.5 thành 9.0.

ten_cu = danh_sach_sv[0][1]

danh_sach_sv[0] = (9.0, ten_cu)

print("\n========== SAU KHI SUA DIEM CUA AN ==========")

for diem, ten in danh_sach_sv:
    print(f"Sinh vien: {ten} - Diem: {diem}")



# 5. KIỂM TRA SINH VIÊN CÓ TRONG DANH SÁCH HAY KHÔNG
print("[ # 5. KIỂM TRA SINH VIÊN CÓ TRONG DANH SÁCH HAY KHÔNG]")

sinh_vien_can_tim = (9.2, "Chi")

print("\n========== KIEM TRA SINH VIEN ==========")

if sinh_vien_can_tim in danh_sach_sv:
    print("Chi co trong danh sach.")
else:
    print("Chi khong co trong danh sach.")


# 6. SẮP XẾP SINH VIÊN THEO ĐIỂM TĂNG DẦN
print("[# 6. SẮP XẾP SINH VIÊN THEO ĐIỂM TĂNG DẦN ]")

# Vì Tuple có điểm đứng trước tên,
# Python sẽ ưu tiên so sánh phần tử đầu tiên.
# Do đó danh sách được sắp xếp theo điểm.

danh_sach_sv.sort()

print("\n========== SAP XEP DIEM TANG DAN ==========")

for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem} diem")


# 7. SẮP XẾP SINH VIÊN THEO ĐIỂM GIẢM DẦN
print("[ #7. SẮP XẾP SINH VIÊN THEO ĐIỂM GIẢM DẦN ]")

danh_sach_sv.sort(reverse=True)

print("\n========== SAP XEP DIEM GIAM DAN ==========")

for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem} diem")



# 8. HIỂN THỊ DANH SÁCH CUỐI CÙNG
print("[# 8. HIỂN THỊ DANH SÁCH CUỐI CÙNG ]")

print("\n========== DANH SACH SINH VIEN CUOI CUNG ==========")

for vi_tri, sinh_vien in enumerate(danh_sach_sv, start=1):
    diem, ten = sinh_vien
    print(f"{vi_tri}. {ten} - {diem} diem")