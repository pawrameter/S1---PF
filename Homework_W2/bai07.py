# Bài 07 - Điều kiện nhận học bổng

gpa = float(input('Nhập GPA: '))
ren_luyen = int(input('Nhập điểm rèn luyện: '))
nckh = int(input('Có giải NCKH (1/0): '))
ky_luat = int(input('Bị kỷ luật (1/0): '))

if gpa <= 0 or gpa > 4 or ren_luyen <0 or ren_luyen > 100:
    print('Điểm GPA hoặc Điểm rèn luyện không hợp lệ')

elif nckh != 1 and nckh != 0 or ky_luat != 0 and ky_luat != 1:
    print('Giải NCKH và Trạng thái kỷ luật chỉ nhập 1 (có) hoặc 0 (không)')
    exit()

else:
    print(f'Nhập GPA: {gpa:.1f}')
    print(f'Nhập điểm rèn luyện: {ren_luyen}')
    print(f'Có giải NCKH (1/0): {nckh}')
    print(f'Bị kỷ luật (1/0): {ky_luat}')
    print(f'Được học bổng: {bool(gpa >= 3.2 and ren_luyen >= 80 or nckh == 1 and ky_luat == 0)}')

### Dataset 1
# Nhập GPA: 3.8 
# Nhập điểm rèn luyện: 88
# Có giải NCKH (1/0): 1
# Bị kỷ luật (1/0): 0
# Được học bổng (1/0): True

### Dataset 2
# Nhập GPA: 2.8
# Nhập điểm rèn luyện: 80
# Có giải NCKH (1/0): 0
# Bị kỷ luật (1/0): 0
# Được học bổng (1/0): False

### Dataset 3
# Nhập GPA: 3.2 
# Nhập điểm rèn luyện: 75
# Có giải NCKH (1/0): 1
# Bị kỷ luật (1/0): 0
# Được học bổng (1/0): True