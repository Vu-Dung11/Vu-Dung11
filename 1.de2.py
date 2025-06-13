def khoi_tao_ds_sinh_vien(n):
    ds = []
    for i in range(n):
        print(f"\nNhập thông tin sinh viên thứ {i + 1}:")
        ma = input("  Mã sinh viên: ")
        ten = input("  Họ tên: ")
        nam_sinh = input("  Năm sinh: ")
        gioi_tinh = input("  Giới tính: ")
        que_quan = input("  Quê quán: ")
        while True:
            try:
                diem = float(input("  Điểm thi: "))
                break
            except ValueError:
                print("  Điểm phải là số!")
        sv = {
            "ma": ma,
            "ten": ten,
            "nam_sinh": nam_sinh,
            "gioi_tinh": gioi_tinh,
            "que_quan": que_quan,
            "diem": diem
        }
        ds.append(sv)
    return ds


def tim_sv_diem_cao_nhat(ds):
    if not ds:
        return []
    max_diem = max(sv['diem'] for sv in ds)
    return [sv for sv in ds if sv['diem'] == max_diem]


def xoa_sv_theo_ma(ds, ma_sv):
    for sv in ds:
        if sv['ma'] == ma_sv:
            ds.remove(sv)
            return True
    return False


def hien_thi_ds(ds):
    print("\nDanh sách sinh viên:")
    for sv in ds:
        print(f"  Mã: {sv['ma']}, Tên: {sv['ten']}, Năm sinh: {sv['nam_sinh']}, "
              f"Giới tính: {sv['gioi_tinh']}, Quê quán: {sv['que_quan']}, Điểm: {sv['diem']}")


def main():
    while True:
        try:
            n = int(input("Nhập số lượng sinh viên (n ≥ 5): "))
            if n >= 5:
                break
            else:
                print("Số lượng phải ≥ 5.")
        except ValueError:
            print("Vui lòng nhập số nguyên.")

    ds_sv = khoi_tao_ds_sinh_vien(n)

    # Hiển thị sinh viên điểm cao nhất
    sv_max = tim_sv_diem_cao_nhat(ds_sv)
    print("\nSinh viên có điểm cao nhất:")
    for sv in sv_max:
        print(f"  Mã: {sv['ma']}, Tên: {sv['ten']}, Điểm: {sv['diem']}")

    # Xóa theo mã
    ma_xoa = input("\nNhập mã sinh viên cần xóa: ")
    if xoa_sv_theo_ma(ds_sv, ma_xoa):
        print(f"Đã xóa sinh viên có mã {ma_xoa}.")
    else:
        print("Không tìm thấy sinh viên cần xóa.")

    hien_thi_ds(ds_sv)


if __name__ == "__main__":
    main()
