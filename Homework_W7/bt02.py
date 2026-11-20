# Bài 2 – Ứng dụng nghe nhạc: sửa playlist

playlist = ['Lac Troi', 'See Tinh', 'Hoa No Khong Mau', 'Ngay Dau Tien', 'Waiting For You']


def show_playlist(playlist):
    print(f'Đang phát: {playlist[0]}')
    print('Tiếp theo:')
    for i in range(1, len(playlist)):
        print(f'  {i}. {playlist[i]}')

def main():
    show_playlist(playlist)

    song = input('Thêm bài vào cuối playlist: ')
    if song in playlist:
        print(f'{song} đã có trong playlist')
    else:
        playlist.append(song)
        print(f'Đã thêm {song}')

    song = input('Bài muốn nghe tiếp theo: ')
    if song == playlist[0]:
        print(f'{song} đang được phát')
    else:
        playlist.remove(song)
        playlist.insert(1, song)
        print(f'{song} sẽ phát tiếp theo')

    song = input('Bài muốn xóa: ')
    if song in playlist:
        playlist.remove(song)
        print(f'Đã xóa {song}')
    else:
        print(f'Không có {song} trong playlist')

    if len(playlist) > 0:
        finished = playlist.pop(0)
        print(f'Phát xong: {finished}')
        show_playlist(playlist)
        print(f'Còn {len(playlist)} bài')
    else:
        print('Playlist đang trống, không có bài nào để phát')

main()
