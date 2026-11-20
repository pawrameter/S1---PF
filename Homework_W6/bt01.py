# Bài 1 – Trạm thời tiết: nhiệt độ cao nhất trong tuần

DAYS = ['Thứ 2', 'Thứ 3', 'Thứ 4', 'Thứ 5', 'Thứ 6', 'Thứ 7', 'Chủ nhật']
TEMPS = [31.5, 33.0, 34.2, 32.8, 29.6, 30.4, 35.1]


def calc_average(temps):
    total = 0
    for t in temps:
        total += t
    return total / len(temps)


def find_hottest(temps):
    best_index = 0
    for i in range(1, len(temps)):
        if temps[i] > temps[best_index]: 
            best_index = i
    return temps[best_index], best_index


def count_above(temps, threshold):
    count = 0
    for t in temps:
        if t > threshold:
            count += 1
    return count


def main():
    for i in range(len(TEMPS)):
        print(f'{DAYS[i]:<9}: {TEMPS[i]:.1f} độ')

    print(f'Trung bình tuần: {calc_average(TEMPS):.1f} độ')

    hottest_temp, hottest_index = find_hottest(TEMPS)
    print(f'Nóng nhất: {DAYS[hottest_index]} ({hottest_temp:.1f} độ)')

    diff = TEMPS[-1] - TEMPS[0]
    print(f'{DAYS[-1]} so với {DAYS[0]}: {diff:+.1f} độ')

    threshold = float(input('Nhập ngưỡng nắng nóng (độ C): '))
    if threshold < -10 or threshold > 50:
        print('Ngưỡng không hợp lệ')
        return
    print(f'Số ngày trên {threshold:.1f} độ: {count_above(TEMPS, threshold)}')

main()