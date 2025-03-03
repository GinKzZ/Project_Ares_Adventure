import heapq
import time
import tracemalloc
import copy
from . import weight

def DIJKSTRA_solve(matrix, stone_weight):
    start_time = time.time()
    tracemalloc.start()

    rows, cols = len(matrix), len(matrix[0])
    pq = []
    visited = set()
    temp_matrix = copy.deepcopy(matrix)

    # Tìm vị trí của Ares và các viên đá
    ares = None
    stones = {}
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == "@":
                ares = (r, c)
            elif matrix[r][c] == "$":
                stones[(r, c)] = stone_weight[len(stones)]
            elif matrix[r][c] == "+":
                ares = (r, c)
                matrix[r][c] = "."
            elif matrix[r][c] == "*":
                stones[(r, c)] = stone_weight[len(stones)]
                matrix[r][c] = "."

    # Thêm trạng thái ban đầu vào priority queue
    heapq.heappush(pq, (0, ares, frozenset(stones.keys()), ""))
    visited.add((ares, frozenset(stones.keys())))

    directions = [(-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")]  # Lên, xuống, trái, phải
    node_count = 0

    while pq:
        cost, ares_pos, stone_pos, path = heapq.heappop(pq)
        node_count += 1

        # Kiểm tra nếu tất cả viên đá đã vào vị trí mục tiêu
        if all(matrix[r][c] == "." for (r, c) in stone_pos):
            end_time = time.time()
            mem_usage = tracemalloc.get_traced_memory()[1] / (1024 * 1024)
            tracemalloc.stop()

            total_weight = weight.count_total_weight(path, temp_matrix, stone_weight)

            move = "Dijkstra\nSteps: " + str(len(path)) + ", Weight: " + str(total_weight) + ", Node: " + str(node_count) + ", Time (ms): " + str(round((end_time - start_time) * 1000, 2)) + ", Memory (MB): " + str(round(mem_usage, 2))
            return move + '\n' + path

        for dr, dc, move in directions:
            new_ares = (ares_pos[0] + dr, ares_pos[1] + dc)

            new_stone_pos = stone_pos  # Giữ nguyên nếu không đẩy đá

            if new_ares in stone_pos:  # Nếu Ares đẩy một viên đá
                new_stone_pos = set(stone_pos)
                new_stone = (new_ares[0] + dr, new_ares[1] + dc)

                if new_stone in stone_pos or matrix[new_stone[0]][new_stone[1]] == "#":
                    continue  # Không thể đẩy hai viên đá cùng lúc hoặc đẩy vào tường

                new_stone_pos.remove(new_ares)
                new_stone_pos.add(new_stone)
                new_state = (new_ares, frozenset(new_stone_pos))

                # Tính trọng số dựa trên viên đá bị đẩy
                stone_cost = stone_weight[len(stone_pos) - 1] if len(stone_pos) > 0 else 1
                new_cost = cost + 1 + stone_cost  # Di chuyển + đẩy đá
            else:
                new_state = (new_ares, stone_pos)
                new_cost = cost + 1  # Chỉ di chuyển, không đẩy đá

            if new_state not in visited and matrix[new_ares[0]][new_ares[1]] != "#":
                visited.add(new_state)
                heapq.heappush(pq, (new_cost, new_ares, new_state[1], path + move.upper() if new_ares in stone_pos else path + move))

    print("Không tìm thấy đường đi.")
    return None
