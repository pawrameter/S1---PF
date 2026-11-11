# Bài 7 - Gợi ý món ăn theo ngân sách

budget = int(input('Nhập ngân sách: '))
diet_type = input('Nhập chế độ ăn (veg/normal): ').lower()

if budget < 0 or diet_type not in ['veg', 'normal']:
    print('Dữ liệu không hợp lệ')

elif diet_type == 'veg' and budget >= 50:
    print('Gợi ý: Cơm chay thập cẩm')

elif diet_type == 'veg' and budget < 50:
    print('Gợi ý: Bánh mì rau')

elif diet_type == 'normal' and budget >= 80000:
    print('Gợi ý: Cơm gà')

elif diet_type == 'normal'and budget >= 30000:
    print('Gợi ý: Bánh mì thịt')

else:
    print('Không đủ tiền, nhịn đói!')