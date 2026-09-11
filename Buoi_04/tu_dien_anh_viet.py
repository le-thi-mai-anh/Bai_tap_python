# HOAT DONG 5: TU DIEN ANH - VIET
print("\n========= HOẠT ĐÔNG 5  =======")
# Tao tu dien Anh - Viet
print("[Tạo tuừ điển Anh- Việt]")
tu_dien_anh_viet = {
    "hello": "xin chao",
    "book": "quyen sach",
    "table": "cai ban"
}

# Tim tu "hello"
print("[Tim tu Hello]")
print(tu_dien_anh_viet.get("hello", "Khong tim thay tu nay"))

# Tim tu "computer"
print("[Tim từ computer]")
# Tu "computer" chua co trong tu dien
print(tu_dien_anh_viet.get("computer", "Khong tim thay tu nay"))

# Them tu "computer" vao tu dien
tu_dien_anh_viet["computer"] = "may tinh"

# Xoa tu "table"
print("[ Xóa từ table]")
tu_dien_anh_viet.pop("table")

# In tu dien hien tai
print("[ In từ điển hiện tại ]")
print("Tu dien hien tai:")

for tu_anh, tu_viet in tu_dien_anh_viet.items():
    print(f"{tu_anh} - {tu_viet}")