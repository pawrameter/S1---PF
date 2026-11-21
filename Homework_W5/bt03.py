# Bài 3 - Kiến trúc sư nhí: vẽ dãy phố bằng turtle

import turtle as t

def draw_square(size, wall_color='yellow'):

    t.fillcolor(wall_color)
    t.begin_fill()

    for i in range (4):
        t.forward(size)
        t.left(90)

    t.end_fill()

    t.left(90)
    t.forward(size)
    t.right(90)

def draw_triangle(size, roof_color='red'):

    t.fillcolor(roof_color)
    t.begin_fill()

    for i in range(3):
        t.forward(size)
        t.left(120)

    t.end_fill()

    t.forward(size)

def draw_house(size, wall_color='yellow', roof_color='red'):
    t.speed(0)
    draw_square(size, wall_color)
    draw_triangle(size, roof_color)

def draw_street(n_houses, size, gap=20):
    
    for i in range(n_houses):
        draw_house(size) if i % 2 == 0 else draw_house(size, wall_color='light blue', roof_color='orange')
    
        t.penup()

        t.forward(gap)
        t.right(90)
        t.forward(size)
        t.left(90)

        t.pendown()

    t.exitonclick()

def main():
    n_houses = int(input('Nhập số nhà (1-8): '))
    size = int(input('Kích thước nhà (20-150): '))

    if n_houses < 1 or n_houses > 8 or size < 20 or size > 150:
        print('Dữ liệu không hợp lệ')
        exit()

    else:
        draw_street(n_houses, size)

main()