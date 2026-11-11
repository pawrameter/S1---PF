# Bài 3 - Xếp loại học lực

gpa = float(input('Nhập điểm trung bình (thang 10): '))

if gpa < 0 or gpa > 10:
    print('Điểm không hợp lệ')

elif gpa >= 8.5:
    print('Xếp loại: Giỏi')

elif gpa >= 7.0:
    print('Xếp loại: Khá')

elif gpa >= 5.0:
    print('Xếp loại: Trung bình')
    
else:
    print('Xếp loại: Yếu')