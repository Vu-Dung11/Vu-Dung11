class GiaoDich:
    def __init__(self, ma, loai, ngay, gia_tri, loai_ts):
        self.ma = ma
        self.loai = loai
        self.ngay = ngay
        self.gia_tri = gia_tri
        self.loai_ts = loai_ts

    def __str__(self):
        return f"Mã: {self.ma}, Loại: {self.loai}, Ngày: {self.ngay}, Giá trị: {self.gia_tri} triệu, Loại TS: {self.loai_ts}"

    def __gt__(self, other):
        if self.loai_ts.lower() == other.loai_ts.lower():
            return self.gia_tri > 500 and self.gia_tri > other.gia_tri
        return False

def nhap_danh_sach_gd():
    ds = []
    n = int(input("Nhập số lượng giao dịch (n > 3): "))
    for i in range(n):
        print(f"\nNhập thông tin giao dịch thứ {i+1}:")
        try:
            ma = input("  Mã GD: ")
            loai = input("  Loại GD (Mua/Bán): ")
            ngay = input("  Ngày GD (dd/mm/yyyy): ")
            gia = float(input("  Giá trị GD (triệu đồng): "))
            loai_ts = input("  Loại tài sản (Vàng/BĐS/CP...): ")
            gd = GiaoDich(ma, loai, ngay, gia, loai_ts)
            ds.append(gd)
        except ValueError as ve:
            print(f"Lỗi: {ve}. Bỏ qua giao dịch này.")
            continue
    return ds

def main():
    danh_sach = nhap_danh_sach_gd()

    # Lọc giao dịch loại Vàng
    vang_list = [gd for gd in danh_sach if gd.loai_ts.lower() == "vàng"]

    # Sắp xếp tăng dần theo giá trị
    vang_list.sort(key=lambda x: x.gia_tri)

    # In ra màn hình
    print("\nDanh sách giao dịch VÀNG sau khi sắp xếp theo giá trị tăng dần:")
    for gd in vang_list:
        print(gd)

    # Ghi ra file
    with open("VANG.TXT", "w", encoding="utf-8") as f:
        for gd in vang_list:
            f.write(str(gd) + "\n")

if __name__ == "__main__":
    main()
