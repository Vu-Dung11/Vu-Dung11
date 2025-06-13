def khoi_tao_mon_hoc():
    ds_mon = {}
    try:
        n = int(input("Nhập số lượng môn học (n >= 5): "))
        if n < 5:
            raise ValueError("Số lượng môn không hợp lệ. Số lượng môn học phải >= 5")
        for i in range(n):
            print(f"Nhập thông tin môn học thứ {i + 1}:")
            ma_mon = input("Nhập mã môn học: ")
            ten_mon = input("Nhập tên môn học: ")
            so_tin_chi = int(input("Nhập số tín chỉ: "))
            hoc_ky = input("Nhập học kỳ: ")
            giang_vien = input("Nhập tên giảng viên: ")

            ds_mon[ma_mon] = [ten_mon, so_tin_chi, hoc_ky, giang_vien]
    except ValueError as e:
        print(f"Lỗi: {e }")
        return None
    return ds_mon


def nhap_so_dang_ky(ma_mon, ds_mon):
    try:
        if ma_mon not in ds_mon:
            raise KeyError("Mã môn không tồn tại trong danh sách môn học")
        so_dang_ky = int(input(f"Nhập số lượng đăng ký cho môn {ma_mon}: "))
        ds_mon[ma_mon].append(so_dang_ky)
    except ValueError:
        print("Lỗi: Số lượng đăng ký phải là số nguyên")
    except KeyError as e:
        print(f"Lỗi: {e}")


def kiem_tra_dang_ky(ma_mon, ds_mon):
    try:
        if ma_mon not in ds_mon:
            raise KeyError("Mã môn không tồn tại trong danh sách môn học")
        if len(ds_mon[ma_mon]) == 5:
            return True
        return False
    except KeyError as e:
        print(f"Lỗi: {e}")
        return False


if __name__ == "__main__":
    ds_mon = khoi_tao_mon_hoc()
    if not ds_mon:
        print("Không thể khởi tạo danh sách môn học.")
    else:
        for ma_mon in ds_mon:
            if not kiem_tra_dang_ky(ma_mon, ds_mon):
                print(f"Môn {ma_mon} chưa có số lượng đăng ký")
                nhap_so_dang_ky(ma_mon, ds_mon)
            else:
                print(f"Môn {ma_mon} đã có số lượng đăng ký: {ds_mon[ma_mon][4]}")
        tong_dang_ky = 0
        for ma_mon in ds_mon:
            if kiem_tra_dang_ky(ma_mon, ds_mon):
                tong_dang_ky += ds_mon[ma_mon][4]
        print(f"Tổng số lượt đăng ký: {tong_dang_ky}")
