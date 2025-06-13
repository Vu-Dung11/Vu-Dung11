class Nguoi:
    def __init__(self, ho_ten, ngay_sinh, dia_chi):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.dia_chi = dia_chi

class GiaoVien(Nguoi):
    def __init__(self, ho_ten, ngay_sinh, dia_chi, mon_day, trinh_do, so_nam_ct):
        super().__init__(ho_ten, ngay_sinh, dia_chi)
        self.mon_day = mon_day
        self.trinh_do = trinh_do
        self.so_nam_ct = so_nam_ct

    def __lt__(self, other):  # Toán tử so sánh <
        return self.so_nam_ct < other.so_nam_ct

    def __str__(self):
        return (f"Họ tên: {self.ho_ten}, Ngày sinh: {self.ngay_sinh}, Địa chỉ: {self.dia_chi}, "
                f"Môn dạy: {self.mon_day}, Trình độ: {self.trinh_do}, Số năm công tác: {self.so_nam_ct}")

def nhap_danh_sach(n):
    ds = []
    for i in range(n):
        print(f"\nNhập thông tin giáo viên thứ {i+1}:")
        ho_ten = input("  Họ tên: ")
        ngay_sinh = input("  Ngày sinh: ")
        dia_chi = input("  Địa chỉ: ")
        mon_day = input("  Môn dạy: ")
        trinh_do = input("  Trình độ (Cử nhân/Thạc sĩ/Tiến sĩ): ")
        so_nam_ct = int(input("  Số năm công tác: "))

        gv = GiaoVien(ho_ten, ngay_sinh, dia_chi, mon_day, trinh_do, so_nam_ct)
        ds.append(gv)
    return ds

def in_danh_sach(ds, ten_file):
    with open(ten_file, "w", encoding="utf-8") as f:
        print("\n📋 Danh sách giáo viên sau sắp xếp:")
        for gv in ds:
            print(gv)
            f.write(str(gv) + "\n")

def main():
    while True:
        try:
            n = int(input("Nhập số lượng giáo viên (n > 3): "))
            if n > 3:
                break
            else:
                print("Vui lòng nhập n > 3.")
        except ValueError:
            print("Nhập số nguyên hợp lệ!")

    danh_sach = nhap_danh_sach(n)
    danh_sach.sort()  # Sắp xếp tăng dần theo số năm công tác

    in_danh_sach(danh_sach, "GIAOVIEN.TXT")

if __name__ == "__main__":
    main()
