# Bài 5 - Ứng dụng sức khỏe: phân loại BMI

weight = float(input('Nhập cân nặng (kg): '))
heigth = float(input('Nhập chiều cao (m): '))

bmi = weight / heigth ** 2

if weight <= 0 or heigth <= 0:
    print('Dữ liệu không hợp lệ')

else: 
    if bmi >= 30:
        category = 'Béo phì'

    elif bmi >= 25:
        category = 'Thừa cân'

    elif bmi >= 18.5:
        category = 'Bình thường'

    else:
        category = 'Thiếu cân'

    print(f'BMI = {bmi:.2f} => {category}')