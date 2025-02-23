import time
import psutil
import sys
from collections import deque


def dfs_solve(maze, player_pos, stones, targets, stone_weights, timeout=30):
    start_time = time.time()
    process = psutil.Process()
    start_memory = process.memory_info().rss / (1024 * 1024)  # Memory in MB

    stack = deque()
    initial_state = (player_pos, frozenset(stones))
    stack.append(initial_state)
    frontier_set = set([initial_state])
    closed_set = set()
    parents = {}
    nodes = 0

    directions = [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]

    while stack:
        if time.time() - start_time > timeout:
            print("Timeout reached. No solution found.")
            return None

        state = stack.pop()
        player, stones = state
        frontier_set.remove(state)
        closed_set.add(state)
        nodes += 1

        if all(stone in targets for stone in stones):
            end_time = time.time()
            memory_used = process.memory_info().rss / (1024 * 1024) - start_memory
            path = []
            cost = 0
            steps = 0
            while state in parents:
                state, move, weight = parents[state]
                path.append(move)
                cost += weight
                steps += 1
            path.reverse()
            
            return {
                "steps": steps,
                "weight": cost,
                "nodes": nodes,
                "time": (end_time - start_time) * 1000,
                "memory": memory_used,
                "path": "".join(path)
            }

        for dx, dy, move in directions:
            new_player = (player[0] + dx, player[1] + dy)
            if new_player in stones:
                pushed = (new_player[0] + dx, new_player[1] + dy)
                if pushed not in maze and pushed not in stones:
                    new_stones = set(stones)
                    new_stones.remove(new_player)
                    new_stones.add(pushed)
                    new_state = (new_player, frozenset(new_stones))

                    if new_state not in closed_set and new_state not in frontier_set:
                        stack.append(new_state)
                        frontier_set.add(new_state)
                        parents[new_state] = (state, move.upper(), stone_weights.get(pushed, 0))
            else:
                if new_player not in maze:
                    new_state = (new_player, stones)
                    if new_state not in closed_set and new_state not in frontier_set:
                        stack.append(new_state)
                        frontier_set.add(new_state)
                        parents[new_state] = (state, move, 0)

    return None  # No solution found