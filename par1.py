
def khoi_tao_mon_hoc():
    ds_mon ={}
    try:
        n = int(input('nhập số lượng môn học(n>=3): '))
        if n<2:
            raise ValueError('số lương môn học k hợp lệ')
        for i in range (n):
            print(f'nhập thông tin sinh viên thứ {i+1}:')
            maMH = input('nhập mã môn học: ')
            tenMH = input('nhập tên môn học: ')
            soTC = input('nhập số tín chỉ: ')
            hocKy = input('nhập học kỳ: ')
            giangVien = input('nhập tên giảng viên: ')


            ds_mon[maMH] = [tenMH, soTC, hocKy, giangVien]


    except ValueError as e:
        print(f"lỗi: {e}")
        return None
    return ds_mon

def nhap_so_dang_ky(ma_mon, ds_mon):

    try:
        if ma_mon not in ds_mon:
            raise ValueError('mã môn này không có trong danh sach')
        sl = int(input(f'nhập số lượng sinh viên đăng ký của môn {ds_mon[ma_mon][0]}: '))
        ds_mon[ma_mon].append(sl)
    except ValueError as e:
        print(f"lỗi: {e}")
    except KeyError as e:
        print(f"lỗi: {e}")

def kiem_tra_dang_ky(ma_mon, ds_mon):

    try:
        if ma_mon not in ds_mon:
            raise ValueError('mã môn này không có trong danh sach')
        if len(ds_mon[ma_mon]) == 5:
            return True
        return False
    except ValueError as e:
        print(f"lỗi: {e}")
    except KeyError as e:
        print(f"lỗi: {e}")

if __name__ == "__main__":

    ds_mon = {
        "MH001": ["Toán cao cấp", 3, 1, "Thầy A"],
        "MH002": ["Vật lý đại cương", 4, 1, "Cô B"],
        "MH003": ["Lập trình Python", 3, 2, "Thầy C"],
        "MH004": ["Cơ sở dữ liệu", 3, 3, "Cô D"],
        "MH005": ["Hệ điều hành", 3, 3, "Thầy E"]
    }

    for maMH in ds_mon:
            if not kiem_tra_dang_ky(maMH, ds_mon):
                print(f'Ma mon {maMH} chua co so luong dang ky')
                nhap_so_dang_ky(maMH, ds_mon)
            else:
                print(f'Môn {maMH} da co so luong dang ky: {ds_mon[maMH][4]}')

    tong=0
    for maMH in ds_mon:
        if len(ds_mon[maMH]) == 5:
             tong += ds_mon[maMH][4]

    print(f'\nTổng số sinh viên đăng ký tất cả các môn: {tong}')

