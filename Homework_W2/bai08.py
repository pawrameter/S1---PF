# Bài 08 - Vẽ sơ đồ mặt bằng căn hộ bằng turtle

length = int(input('Nhập chiều dài căn hộ: '))
width = int(input('Nhập chiều rộng căn hộ: '))
angle = 90
color = input('Nhập màu: ')

if length <=0 or width <= 0:
    print('Invalid length or width')
    exit()

else:
    print(f'Nhập chiều dài: {length}')
    print(f'Nhập chiều rộng: {width}')
    print(f'Nhập màu nền: {color}')
    
    total_area = length * width
    living_room = total_area * 2/3
    bed_room = total_area * 1/3
    
    print(f'Phòng khách: {living_room:.2f}')
    print(f'Phòng ngủ: {bed_room:.2f}')
    print(f'Tổng diện tích: {total_area:.2f}')

    import turtle as t

    t.fillcolor(color)
    t.begin_fill()

    t.forward(length)
    t.left(angle)
    t.forward(width)
    t.left(angle)
    t.forward(length)
    t.left(angle)
    t.forward(width)

    t.end_fill()

    t.penup()

    t.left(angle)
    t.forward(length * 2 / 3)

    t.pendown()

    t.left(angle)
    t.forward(width)

    t.exitonclick()