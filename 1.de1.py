def khoi_tao_ds_tour(n):
    danh_sach = []
    for i in range(n):
        print(f"\nNhập tour thứ {i+1}:")
        ma = input("  Mã tour: ")
        ten = input("  Tên tour: ")
        dia_diem = input("  Địa điểm: ")
        ngay_khoi_hanh = input("  Ngày khởi hành: ")
        so_ngay = int(input("  Số ngày: "))
        tour = {
            "ma": ma,
            "ten": ten,
            "dia_diem": dia_diem,
            "ngay_khoi_hanh": ngay_khoi_hanh,
            "so_ngay": so_ngay,
            "gia_ve": None  # ban đầu chưa có giá vé
        }
        danh_sach.append(tour)
    return danh_sach

def them_gia_ve(danh_sach):
    for tour in danh_sach:
        if tour["gia_ve"] is None:
            while True:
                try:
                    gia = float(input(f"Nhập giá vé cho tour {tour['ten']}: "))
                    tour["gia_ve"] = gia
                    break
                except ValueError:
                    print("Giá vé phải là số!")

def tinh_gia_ve_tb(danh_sach):
    tong = 0
    dem = 0
    for tour in danh_sach:
        if tour["gia_ve"] is not None:
            tong += tour["gia_ve"]
            dem += 1
    return tong / dem if dem > 0 else 0

def main():
    while True:
        try:
            n = int(input("Nhập số lượng tour (n >= 5): "))
            if n >= 5:
                break
            else:
                print("Phải nhập ít nhất 5 tour!")
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")

    ds_tour = khoi_tao_ds_tour(n)
    them_gia_ve(ds_tour)

    trung_binh = tinh_gia_ve_tb(ds_tour)
    print(f"\nGiá vé trung bình của các tour là: {trung_binh:.2f} VND")

if __name__ == "__main__":
    main()
