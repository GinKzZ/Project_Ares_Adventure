import numpy as np

def count_total_weight(path, matrix, stone_weight):
  
    rows, cols = len(matrix), len(matrix[0])
    
    # Tìm vị trí của Ares và các viên đá ban đầu
    stone_positions = {}  # Lưu vị trí và trọng số của các viên đá
    weight_index = 0
    ares_pos = None

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == "@":  # Ares
                ares_pos = (r, c)
            elif matrix[r][c] == "$":  # Viên đá
                stone_positions[(r, c)] = stone_weight[weight_index] 
                weight_index += 1
            elif matrix[r][c] == "+":  # Ares
                ares_pos = (r, c)
                matrix[r][c] = "."  # Đổi thành đường đi
            elif matrix[r][c] == "*":  # Viên đá
                stone_positions[(r, c)] = stone_weight[weight_index]
                weight_index += 1
                matrix[r][c] = "."

    total_cost = 0
    directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    # Duyệt qua từng bước di chuyển trong `path`
    for move in path:
        dr, dc = directions[move.upper()]
        new_ares_pos = (ares_pos[0] + dr, ares_pos[1] + dc)

        # Nếu Ares đẩy một viên đá
        if new_ares_pos in stone_positions:
            new_stone_pos = (new_ares_pos[0] + dr, new_ares_pos[1] + dc)

            # Cộng trọng số của viên đá vào tổng chi phí
            total_cost += stone_positions[new_ares_pos]

            # Cập nhật vị trí mới của viên đá
            stone_positions[new_stone_pos] = stone_positions.pop(new_ares_pos)

        # Cập nhật vị trí mới của Ares
        ares_pos = new_ares_pos

    return total_cost