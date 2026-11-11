# Bài 9 - Xét học bổng

gpa = float(input('Nhập GPA (thang 4.0): '))
ren_luyen = int(input('Nhập điểm rèn luyện (0-100): '))
ky_luat = input('Đã từng bị kỷ luuạt (y/n): ')

has_discipline = ky_luat == 'y'

if gpa < 0 or gpa > 4 or ren_luyen < 0 or ren_luyen > 100:
    print('Dữ liệu không hợp lệ')

else: 
    if has_discipline:
        print ('Không đủ điều kiện xét học bổng')

    else:
        if gpa >= 3.6 and ren_luyen >= 90:
            print('Học bổng toàn phần')

        elif gpa >= 3.2 and ren_luyen >= 80:
            print('Học bổng 50%')

        elif gpa >= 2.8 or ren_luyen >= 90:
            print('Khuyến khích học tập')

        else:
            print('Không đạt')