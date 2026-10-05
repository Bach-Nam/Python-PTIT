
import sys
from itertools import permutations
 
 
def solve():
    data = sys.stdin.read().split()
    idx = 0
 
    n = int(data[idx]); idx += 1
 
    # Đọc ma trận chi phí c[i][j], lưu theo chỉ số 0-based
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = int(data[idx]); idx += 1
 
    best_cost = None
    best_tours = []  # danh sách các hành trình đạt chi phí nhỏ nhất
 
    other_cities = list(range(1, n))  # các thành phố 2..n (0-based: 1..n-1)
 
    # Duyệt toàn bộ hoán vị của các thành phố còn lại
    for perm in permutations(other_cities):
        path = [0] + list(perm)  # luôn xuất phát từ thành phố 0 (tức thành phố 1)
 
        cost = 0
        for k in range(n - 1):
            cost += c[path[k]][path[k + 1]]
        cost += c[path[-1]][path[0]]  # quay về điểm xuất phát
 
        if best_cost is None or cost < best_cost:
            best_cost = cost
            best_tours = [path]
        elif cost == best_cost:
            best_tours.append(path)
 
    # In kết quả
    if len(best_tours) == 1:
        print(best_cost)
        print(' '.join(str(x + 1) for x in best_tours[0]))
    else:
        print(best_cost, len(best_tours))
        for tour in best_tours:
            print(' '.join(str(x + 1) for x in tour))
 
 
if __name__ == "__main__":
    solve()
 