# QUAN LY SINH VIEN

# BUOC 4.1 - KHAI BAO DU LIEU BAN DAU

danh_sach_sinh_vien = [
    {
        "ma_sv": "2411060164",
        "ho_ten": "Lê Thị Mai Anh",
        "nam_sinh": 2006,
        "diem_python": 10.0,
        "diem_csdl": 9.5,
        "diem_lap_trinh": 9.5
    },
    {
        "ma_sv": "SV002",
        "ho_ten": "Tran Thi Binh",
        "nam_sinh": 2006,
        "diem_python": 9.0,
        "diem_csdl": 8.0,
        "diem_lap_trinh": 8.5
    },
    {
        "ma_sv": "SV003",
        "ho_ten": "Le Van Cuong",
        "nam_sinh": 2005,
        "diem_python": 6.5,
        "diem_csdl": 7.0,
        "diem_lap_trinh": 6.0
    }
]

# BUOC 4.2 - HIEN THI VA TIM KIEM

def tinh_diem_trung_binh(sinh_vien):
    """
    Tinh diem trung binh cua sinh vien.
    """
    diem_tb = (
        sinh_vien["diem_python"]
        + sinh_vien["diem_csdl"]
        + sinh_vien["diem_lap_trinh"]
    ) / 3

    return diem_tb


def xep_loai_sinh_vien(diem_tb):
    """
    Xep loai sinh vien dua vao diem trung binh.
    """
    if diem_tb >= 8.5:
        return "Gioi"

    elif diem_tb >= 7.0:
        return "Kha"

    elif diem_tb >= 5.0:
        return "Trung binh"

    else:
        return "Yeu"


def hien_thi_danh_sach_sinh_vien():
    """
    Hien thi toan bo danh sach sinh vien.
    """

    print("\n" + "=" * 105)

    print(
        f"{'Ma SV':<10}"
        f"{'Ho ten':<22}"
        f"{'Nam sinh':<10}"
        f"{'Python':<10}"
        f"{'CSDL':<10}"
        f"{'Lap trinh':<12}"
        f"{'Diem TB':<10}"
        f"{'Xep loai':<12}"
    )

    print("-" * 105)

    for sinh_vien in danh_sach_sinh_vien:

        diem_tb = tinh_diem_trung_binh(sinh_vien)

        xep_loai = xep_loai_sinh_vien(diem_tb)

        print(
            f"{sinh_vien['ma_sv']:<10}"
            f"{sinh_vien['ho_ten']:<22}"
            f"{sinh_vien['nam_sinh']:<10}"
            f"{sinh_vien['diem_python']:<10.1f}"
            f"{sinh_vien['diem_csdl']:<10.1f}"
            f"{sinh_vien['diem_lap_trinh']:<12.1f}"
            f"{diem_tb:<10.2f}"
            f"{xep_loai:<12}"
        )

    print("=" * 105)


def tim_sinh_vien_theo_ma(ma_sv):
    """
    Tim sinh vien theo ma sinh vien.
    """

    for sinh_vien in danh_sach_sinh_vien:

        if sinh_vien["ma_sv"] == ma_sv:

            return sinh_vien

    return None


def tim_sinh_vien():
    """
    Tim va hien thi thong tin sinh vien.
    """

    ma_sv = input(
        "Nhap ma sinh vien can tim: "
    ).strip().upper()

    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:

        print(
            f"-> Khong tim thay sinh vien {ma_sv}."
        )

        return

    diem_tb = tinh_diem_trung_binh(sinh_vien)

    xep_loai = xep_loai_sinh_vien(diem_tb)

    print("\nTHONG TIN SINH VIEN")

    print(
        f"Ma sinh vien: {sinh_vien['ma_sv']}"
    )

    print(
        f"Ho ten: {sinh_vien['ho_ten']}"
    )

    print(
        f"Nam sinh: {sinh_vien['nam_sinh']}"
    )

    print(
        f"Diem Python: {sinh_vien['diem_python']}"
    )

    print(
        f"Diem CSDL: {sinh_vien['diem_csdl']}"
    )

    print(
        f"Diem Lap trinh: {sinh_vien['diem_lap_trinh']}"
    )

    print(
        f"Diem trung binh: {diem_tb:.2f}"
    )

    print(
        f"Xep loai: {xep_loai}"
    )

# BUOC 4.3 - THEM, SUA, XOA SINH VIEN

def them_sinh_vien(
    ma_sv,
    ho_ten,
    nam_sinh,
    diem_python,
    diem_csdl,
    diem_lap_trinh
):
    """
    Them sinh vien moi.
    """

    # Kiem tra ma sinh vien da ton tai hay chua

    if tim_sinh_vien_theo_ma(ma_sv) is not None:

        print(
            f"-> Ma sinh vien {ma_sv} da ton tai, "
            f"khong the them."
        )

        return

    # Them sinh vien moi vao danh sach

    danh_sach_sinh_vien.append(
        {
            "ma_sv": ma_sv,
            "ho_ten": ho_ten,
            "nam_sinh": nam_sinh,
            "diem_python": diem_python,
            "diem_csdl": diem_csdl,
            "diem_lap_trinh": diem_lap_trinh
        }
    )

    print(
        f"-> Da them sinh vien {ma_sv} thanh cong."
    )


def cap_nhat_sinh_vien(ma_sv):
    """
    Cap nhat thong tin sinh vien.
    """

    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    # Kiem tra sinh vien co ton tai khong

    if sinh_vien is None:

        print(
            f"-> Khong tim thay sinh vien {ma_sv}."
        )

        return

    print("\nNHAP THONG TIN MOI")

    ho_ten = input(
        "Nhap ho ten moi: "
    ).strip().title()

    nam_sinh = nhap_so_nguyen(
        "Nhap nam sinh moi: "
    )

    diem_python = nhap_diem(
        "Nhap diem Python moi: "
    )

    diem_csdl = nhap_diem(
        "Nhap diem CSDL moi: "
    )

    diem_lap_trinh = nhap_diem(
        "Nhap diem Lap trinh moi: "
    )

    # Cap nhat du lieu

    sinh_vien["ho_ten"] = ho_ten
    sinh_vien["nam_sinh"] = nam_sinh
    sinh_vien["diem_python"] = diem_python
    sinh_vien["diem_csdl"] = diem_csdl
    sinh_vien["diem_lap_trinh"] = diem_lap_trinh

    print(
        f"-> Da cap nhat sinh vien {ma_sv} thanh cong."
    )


def xoa_sinh_vien(ma_sv):
    """
    Xoa sinh vien khoi danh sach.
    """

    sinh_vien = tim_sinh_vien_theo_ma(ma_sv)

    if sinh_vien is None:

        print(
            f"-> Khong tim thay sinh vien {ma_sv}."
        )

        return

    danh_sach_sinh_vien.remove(sinh_vien)

    print(
        f"-> Da xoa sinh vien {ma_sv} thanh cong."
    )


# BUOC 4.4 - NHAP DU LIEU AN TOAN BANG TRY-EXCEPT

def nhap_so_nguyen(loi_nhac):
    """
    Nhap so nguyen va xu ly loi ValueError.
    """

    while True:

        try:

            return int(input(loi_nhac))

        except ValueError:

            print(
                "-> Du lieu khong hop le, "
                "vui long nhap mot so nguyen."
            )


def nhap_diem(loi_nhac):
    """
    Nhap diem tu 0 den 10.
    """

    while True:

        try:

            diem = float(input(loi_nhac))

            if 0 <= diem <= 10:

                return diem

            print(
                "-> Diem phai nam trong khoang tu 0 den 10."
            )

        except ValueError:

            print(
                "-> Du lieu khong hop le, "
                "vui long nhap mot so."
            )


# BUOC 4.5 - THONG KE SINH VIEN

def thong_ke_sinh_vien():
    """
    Thong ke so luong sinh vien va xep loai.
    """

    if len(danh_sach_sinh_vien) == 0:

        print(
            "-> Danh sach sinh vien dang rong."
        )

        return

    so_gioi = 0
    so_kha = 0
    so_trung_binh = 0
    so_yeu = 0

    for sinh_vien in danh_sach_sinh_vien:

        diem_tb = tinh_diem_trung_binh(sinh_vien)

        xep_loai = xep_loai_sinh_vien(diem_tb)

        if xep_loai == "Gioi":

            so_gioi += 1

        elif xep_loai == "Kha":

            so_kha += 1

        elif xep_loai == "Trung binh":

            so_trung_binh += 1

        else:

            so_yeu += 1

    print("\n===== THONG KE SINH VIEN =====")

    print(
        f"Tong so sinh vien: "
        f"{len(danh_sach_sinh_vien)}"
    )

    print(
        f"So sinh vien Gioi: {so_gioi}"
    )

    print(
        f"So sinh vien Kha: {so_kha}"
    )

    print(
        f"So sinh vien Trung binh: "
        f"{so_trung_binh}"
    )

    print(
        f"So sinh vien Yeu: {so_yeu}"
    )

# BUOC 4.6 - MENU CHINH

def hien_thi_menu():

    print(
        "\n===== QUAN LY SINH VIEN ====="
    )

    print(
        "1. Hien thi danh sach sinh vien"
    )

    print(
        "2. Tim sinh vien theo ma"
    )

    print(
        "3. Them sinh vien moi"
    )

    print(
        "4. Cap nhat thong tin sinh vien"
    )

    print(
        "5. Xoa sinh vien"
    )

    print(
        "6. Thong ke sinh vien"
    )

    print(
        "0. Thoat chuong trinh"
    )


def chay_chuong_trinh():

    while True:

        hien_thi_menu()

        lua_chon = input(
            "Nhap lua chon cua ban: "
        ).strip()

        # CHUC NANG 1: HIEN THI DANH SACH

        if lua_chon == "1":

            hien_thi_danh_sach_sinh_vien()

        # CHUC NANG 2: TIM SINH VIEN

        elif lua_chon == "2":

            tim_sinh_vien()


        # CHUC NANG 3: THEM SINH VIEN


        elif lua_chon == "3":

            ma_sv = input(
                "Nhap ma sinh vien moi: "
            ).strip().upper()

            ho_ten = input(
                "Nhap ho ten: "
            ).strip().title()

            nam_sinh = nhap_so_nguyen(
                "Nhap nam sinh: "
            )

            diem_python = nhap_diem(
                "Nhap diem Python: "
            )

            diem_csdl = nhap_diem(
                "Nhap diem CSDL: "
            )

            diem_lap_trinh = nhap_diem(
                "Nhap diem Lap trinh: "
            )

            them_sinh_vien(
                ma_sv,
                ho_ten,
                nam_sinh,
                diem_python,
                diem_csdl,
                diem_lap_trinh
            )


        # CHUC NANG 4: CAP NHAT SINH VIEN

        elif lua_chon == "4":

            ma_sv = input(
                "Nhap ma sinh vien can cap nhat: "
            ).strip().upper()

            cap_nhat_sinh_vien(ma_sv)

        #  CHUC NANG 5: XOA SINH VIEN


        elif lua_chon == "5":

            ma_sv = input(
                "Nhap ma sinh vien can xoa: "
            ).strip().upper()

            xoa_sinh_vien(ma_sv)

        # CHUC NANG 6: THONG KE


        elif lua_chon == "6":

            thong_ke_sinh_vien()


        # THOAT


        elif lua_chon == "0":

            print(
                "Cam on da su dung chuong trinh. Tam biet!"
            )

            break


        # NHAP SAI MENU


        else:

            print(
                "-> Lua chon khong hop le, "
                "vui long chon lai."
            )



# CHAY CHUONG TRINH


if __name__ == "__main__":
    chay_chuong_trinh()