# ============================================
# MINI PROJECT 1
# QUẢN LÝ DANH SÁCH SINH VIÊN
# ============================================

# Danh sách sinh viên
# Mỗi sinh viên có dạng: (điểm, tên)

danh_sach_sv = [
    (8.5, "An"),
    (7.0, "Binh"),
    (9.2, "Chi"),
    (6.5, "Dung")
]

print("DANH SÁCH SINH VIÊN BAN ĐẦU:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


# ============================================
# 1. THÊM SINH VIÊN MỚI
# ============================================

danh_sach_sv.append((8.0, "Em"))

print("\nSAU KHI THÊM SINH VIÊN:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


# ============================================
# 2. XÓA SINH VIÊN
# ============================================

danh_sach_sv.remove((7.0, "Binh"))

print("\nSAU KHI XÓA SINH VIÊN BINH:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


# ============================================
# 3. SỬA ĐIỂM SINH VIÊN
# ============================================

# Sửa điểm sinh viên ở vị trí 0
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])

print("\nSAU KHI SỬA ĐIỂM SINH VIÊN:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


# ============================================
# 4. KIỂM TRA SINH VIÊN CÓ TRONG DANH SÁCH
# ============================================

print(
    "\nChi có trong danh sách không?",
    (9.2, "Chi") in danh_sach_sv
)


# ============================================
# 5. SẮP XẾP TĂNG DẦN THEO ĐIỂM
# ============================================

danh_sach_sv.sort()

print("\nDANH SÁCH SAU KHI SẮP XẾP TĂNG DẦN:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


# ============================================
# 6. SẮP XẾP GIẢM DẦN THEO ĐIỂM
# ============================================

danh_sach_sv.sort(reverse=True)

print("\nDANH SÁCH SAU KHI SẮP XẾP GIẢM DẦN:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")