import sqlite3

TEN_FILE_CSDL = "quan_ly_thu_cung.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS thu_cung (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_thu_cung TEXT NOT NULL,
            loai TEXT NOT NULL,
            chi_phi REAL NOT NULL,
            da_thanh_toan INTEGER NOT NULL DEFAULT 0
        )
    """)
    ket_noi.commit()
    ket_noi.close()

def them_thu_cung(ten, loai, chi_phi):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO thu_cung (ten_thu_cung, loai, chi_phi, da_thanh_toan) VALUES (?, ?, ?, 0)",
        (ten, loai, chi_phi)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, ten_thu_cung, loai, chi_phi, da_thanh_toan FROM thu_cung ORDER BY id")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_thu_cung(id_tc):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM thu_cung WHERE id = ?", (id_tc,))
    ket_noi.commit()
    ket_noi.close()

def danh_dau_thanh_toan(id_tc):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("UPDATE thu_cung SET da_thanh_toan = 1 WHERE id = ?", (id_tc,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_chi_phi():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT loai, SUM(chi_phi) FROM thu_cung GROUP BY loai")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua