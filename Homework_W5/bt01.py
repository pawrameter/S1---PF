# Bài 1 - Ứng dụng sức khỏe: tính chỉ số BMI

def is_valid(weight, height):

    if weight <= 0 or weight > 300 or height <= 0 or height > 2.5:
        print('Dữ liệu không hợp lệ')

    else:
        bmi = calc_bmi(weight, height)
        classify = classify_bmi(bmi)
        print(f'BMI = {bmi:.1f} -> {classify}')

def calc_bmi(weight, height):
    bmi = weight/(height**2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:  
        return 'Thiếu cân'
    elif bmi < 23:
        return 'Bình thường'
    elif bmi < 25:
        return 'Thừa cân'
    else:
        return 'Béo phì'

weight = float(input('Nhập cân nặng: '))
height = float(input('Nhập chiều cao: '))

is_valid(weight, height)