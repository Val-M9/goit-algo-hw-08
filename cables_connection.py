import heapq


def connect_cables_with_min_cost(cables):
    heapq.heapify(cables)
    print(cables)
    total_cost = 0

    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        total_cost += cable1 + cable2
        heapq.heappush(cables, cable1 + cable2)

    return total_cost


cables = [8, 4, 6, 12, 2, 5]
print(connect_cables_with_min_cost(cables))
