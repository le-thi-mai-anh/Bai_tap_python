import sqlite3

# Tên file cơ sở dữ liệu SQLite
TEN_FILE_CSDL = "tu_sach.db"

def ket_noi_csdl():
    """Tạo kết nối tới file CSDL SQLite"""
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    """Tạo bảng 'sach' nếu bảng này chưa tồn tại trong CSDL"""
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS sach (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_sach TEXT NOT NULL,
            tac_gia TEXT NOT NULL,
            the_loai TEXT NOT NULL,
            da_doc INTEGER NOT NULL DEFAULT 0
        )
    """)
    ket_noi.commit()
    ket_noi.close()

def them_sach(ten_sach, tac_gia, the_loai):
    """Thêm một cuốn sách mới vào CSDL"""
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO sach (ten_sach, tac_gia, the_loai, da_doc) VALUES (?, ?, ?, 0)",
        (ten_sach, tac_gia, the_loai)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_sach():
    """Lấy danh sách tất cả cuốn sách trong CSDL"""
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, ten_sach, tac_gia, the_loai, da_doc FROM sach ORDER BY id")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_sach(id_sach):
    """Xóa cuốn sách theo id"""
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM sach WHERE id = ?", (id_sach,))
    ket_noi.commit()
    ket_noi.close()

def danh_dau_da_doc(id_sach):
    """Cập nhật trạng thái da_doc = 1 cho cuốn sách theo id"""
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("UPDATE sach SET da_doc = 1 WHERE id = ?", (id_sach,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_theo_the_loai():
    """Gộp nhóm và đếm số lượng sách theo từng thể loại"""
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT the_loai, COUNT(*) FROM sach GROUP BY the_loai")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua