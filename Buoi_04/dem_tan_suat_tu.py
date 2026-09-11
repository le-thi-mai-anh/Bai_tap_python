# HOAT DONG 6: DEM TAN SUAT XUAT HIEN CUA TU
print("\n ========= HOẠT ĐỘNG 6  ========")
# Tao doan van
print(" [ Tạo đoạn Văn ]")
doan_van = "python la ngon ngu lap trinh python de hoc python de dung"

# Tach doan van thanh danh sach cac tu
print("[ Tách đoanj văn thành danh sách từ ]")
danh_sach_tu = doan_van.split()

# Tao Dictionary rong de luu tan suat
print("[ Tạo Dictionary rỗng để lưu tần suất]")
tan_suat = {}

# Duyet tung tu trong danh sach
print("[ Duyệt từng từ trong danh sách ]")
for tu in danh_sach_tu:
    tan_suat[tu] = tan_suat.get(tu, 0) + 1

# In ket qua
print("[ In kết qua ]")
print("Tan suat xuat hien cac tu:")

for tu, so_lan in tan_suat.items():
    print(f"{tu}: {so_lan}")