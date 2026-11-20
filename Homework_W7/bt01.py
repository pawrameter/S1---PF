# Bài 1 - Lớp học: thống kê điểm quiz

SCORES = [7, 9, 6, 10, 8, 9, 5, 10, 9, 7, 4, 8]

def calc_average(SCORES):
    average_scores = sum(SCORES) / len(SCORES)
    return average_scores

print(f'Số bài: {len(SCORES)}')

calc_average(SCORES)
print(f'Điểm trung bình: {calc_average(SCORES):.2f}')

print(f'Điểm cao nhất: {max(SCORES)}')
print(f'Điểm thấp nhất: {min(SCORES)}')

tang_dan = sorted(SCORES)
giam_dan = list(reversed(tang_dan))

print(f'Tăng dần: {tang_dan}')
print(f'Giảm dần: {giam_dan}')

print(f'Top 3: {giam_dan[0]}, {giam_dan[1]}, {giam_dan[2]}')

print(f'Danh sách gốc: {SCORES}')

def find_score(SCORES, x):
    position = None
    for score in SCORES:
        if score == x:
            position = SCORES.index(x) + 1
    return position

def count_score(SCORES, x):
    count = 0
    for i in range(len(SCORES)):
        if SCORES[i] == x:
            count += 1
    return count

x = int(input('Nhập điểm cần tra: '))
pos = find_score(SCORES, x)
count = count_score(SCORES, x)

if x < 0 or x > 10:
    print('Điểm không hợp lệ')
if pos is None:
    print(f'Không có bài nào đạt {x} điểm')
else: 
    print(f'Có {count} bài đạt {x} điểm, bài đầu tiên ở vị trí số {pos}')

# Nếu dùng SCORES.sort() thay cho sorted(SCORES) thì danh sách gốc sẽ in ra danh sách tăng dần
# Nguyên nhân: SCORES.sort() là method với lệnh sấp xếp đối tượng là SCORES