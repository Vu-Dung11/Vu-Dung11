
def init_students():
    students = [
        {"ma_sv": "001", "ho_ten": "Vu Van Dung", "ngay_sinh": "18/9/2004", "gioi_tinh" :"nam", "que_quan" :"Thai Binh", "diem": 5},
        {"ma_sv": "002", "ho_ten": "Vu Van Dung2", "ngay_sinh": "18/9/2004", "gioi_tinh" :"nam", "que_quan" :"Thai Binh", "diem": 6},
        {"ma_sv": "003", "ho_ten": "Vu Van Dung3", "ngay_sinh": "18/9/2004", "gioi_tinh" :"nam", "que_quan" :"Thai Binh", "diem": 7},
        {"ma_sv": "004", "ho_ten": "Vu Van Dung4", "ngay_sinh": "18/9/2004", "gioi_tinh" :"nam", "que_quan" :"Thai Binh", "diem": 10},
        {"ma_sv": "005", "ho_ten": "Vu Van Dung5", "ngay_sinh": "18/9/2004", "gioi_tinh" :"nam", "que_quan" :"Thai Binh", "diem": 10}
    ]
    return students

def findstudent(students):
    return [i for i in students if i["diem"] >=5]

def findMax(students):
    b = max(i["diem"] for i in students )
    return b




def main():
    # khởi tạo các student tự động, sẵn có
    student = init_students()
    
    list = findstudent(student)

    print('danh sach sinh vien:')
    for sv in student:
        print(sv)

    print('max point: ')
    b = findMax(student)
    print(b)

    for i in student[:]:
        if i["diem"] == b:
            print(i)




    student = [i for i in student if i["diem"] != b]

    print('danh sach sinh vien:')
    for sv in student:
        print(sv)


main()











