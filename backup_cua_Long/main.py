import pygame


# Kích thước mỗi ô
TILE_SIZE = 50

# Ký tự trong bản đồ và hình ảnh tương ứng
TILE_MAP = {
    ' ': 'image/floor.png',  # Sàn
    '#': 'image/wall.png',  # Tường
    '.': 'image/goal.png',  # Điểm đến
    '@': 'image/player.png',  # Nhân vật
    '$': 'image/box.png'  # Hòn đá
}

def load_map(filename):
    """ Đọc bản đồ từ file văn bản và trả về danh sách hàng """
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Lấy danh sách trọng số từ dòng đầu tiên
    weights = list(map(int, lines[0].strip().split()))

    # Lấy bản đồ từ các dòng tiếp theo
    game_map = [line.rstrip() for line in lines[1:]]

    return weights, game_map

def draw_map(screen, game_map, images, weights):
    font = pygame.font.Font(None, 30)
    weight_index = 0

    for y, row in enumerate(game_map):
        for x, tile in enumerate(row):
            # Luôn vẽ sàn trước
            if ' ' in images:
                screen.blit(images[' '], (x * TILE_SIZE, y * TILE_SIZE))

            # Vẽ các đối tượng khác lên trên sàn
            if tile in images:
                screen.blit(images[tile], (x * TILE_SIZE, y * TILE_SIZE))

                # Nếu là hòn đá ($) thì hiển thị trọng số
                if tile == '$' and weight_index < len(weights):
                    text_surface = font.render(str(weights[weight_index]), True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=(x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2))
                    screen.blit(text_surface, text_rect)
                    weight_index += 1


def main():
    pygame.init()

    # Đọc bản đồ từ file
    weights, game_map = load_map('map.txt')

    # Xác định kích thước cửa sổ
    width, height = len(game_map[0]) * TILE_SIZE, len(game_map) * TILE_SIZE
    screen = pygame.display.set_mode((width, height))

    # Load hình ảnh
    images = {}
    for key in TILE_MAP:
        try:
            img = pygame.image.load(TILE_MAP[key])  # Tải ảnh gốc
            images[key] = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))  # Resize về TILE_SIZE
        except pygame.error as e:
            print(f"Lỗi: Không thể tải {TILE_MAP[key]}. Chi tiết: {e}")
            images[key] = pygame.Surface((TILE_SIZE, TILE_SIZE))  # Tạo ảnh trống
            images[key].fill((255, 0, 0))  # Đổ màu đỏ để dễ phát hiện lỗi

    running = True
    while running:
        screen.fill((255, 255, 255))  # Xóa màn hình với nền trắng
        draw_map(screen, game_map, images, weights)  # Vẽ bản đồ
        pygame.display.flip()  # Cập nhật màn hình

        # Xử lý sự kiện thoát
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
