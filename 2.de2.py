class Nguoi:
    def __init__(self, ho_ten, tuoi, quoc_tich):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.quoc_tich = quoc_tich

class CauLacBo:
    def __init__(self, ten_clb, ma_clb, hlv, nam_thanh_lap):
        self.ten_clb = ten_clb
        self.ma_clb = ma_clb
        self.hlv = hlv
        self.nam_thanh_lap = nam_thanh_lap

class CauThu(Nguoi):
    def __init__(self, ho_ten, tuoi, quoc_tich, ma_ct, vi_tri, so_ao, clb: CauLacBo):
        super().__init__(ho_ten, tuoi, quoc_tich)
        self.ma_ct = ma_ct
        self.vi_tri = vi_tri
        self.so_ao = so_ao
        self.clb = clb

    def hien_thi(self):
        print(f"Mã: {self.ma_ct}, Tên: {self.ho_ten}, Tuổi: {self.tuoi}, Quốc tịch: {self.quoc_tich}, "
              f"Vị trí: {self.vi_tri}, Số áo: {self.so_ao}, CLB: {self.clb.ten_clb}")

def khoi_tao_san_ds():
    clb1 = CauLacBo("Real Madrid", "RM01", "Ancelotti", 1902)
    clb2 = CauLacBo("Man United", "MU01", "Erik Ten Hag", 1878)
    clb3 = CauLacBo("Barcelona", "BAR01", "Xavi", 1899)

    ds = [
        CauThu("Cristiano Ronaldo", 39, "Bồ Đào Nha", "CR7", "Tiền đạo", 9, clb2),
        CauThu("Jude Bellingham", 21, "Anh", "JB22", "Tiền vệ", 5, clb1),
        CauThu("Pedri", 19, "Tây Ban Nha", "PD16", "Tiền vệ", 8, clb3),
        CauThu("Gavi", 18, "Tây Ban Nha", "GV30", "Tiền vệ", 6, clb3),
        CauThu("Marcus Rashford", 27, "Anh", "MR10", "Tiền đạo", 10, clb2)
    ]
    return ds

def sua_so_ao_cr7(ds):
    for ct in ds:
        if ct.ho_ten.lower() == "cristiano ronaldo":
            ct.so_ao = 7
            print("  → Đã cập nhật số áo của Cristiano Ronaldo thành 7.")
            return
    print("  → Không có cầu thủ tên Cristiano Ronaldo.")

def dem_cau_thu_tuoi_nho(ds):
    return sum(1 for ct in ds if ct.tuoi < 20)

def sap_xep_theo_so_ao(ds):
    return sorted(ds, key=lambda ct: ct.so_ao)

def hien_thi_danh_sach(ds):
    print("\n Danh sách cầu thủ:")
    for ct in ds:
        ct.hien_thi()

def main():
    print("📌 Dùng dữ liệu mẫu được khởi tạo sẵn.")
    ds_cau_thu = khoi_tao_san_ds()

    hien_thi_danh_sach(ds_cau_thu)

    print("\n Sửa số áo cho Cristiano Ronaldo (nếu có):")
    sua_so_ao_cr7(ds_cau_thu)

    so_nho_20 = dem_cau_thu_tuoi_nho(ds_cau_thu)
    print(f"\n Số cầu thủ có tuổi nhỏ hơn 20: {so_nho_20}")

    print("\n Danh sách cầu thủ sắp xếp theo số áo tăng dần:")
    ds_sap_xep = sap_xep_theo_so_ao(ds_cau_thu)
    hien_thi_danh_sach(ds_sap_xep)

if __name__ == "__main__":
    main()
