import heapq

class SeatManager:
    def __init__(self, n):
        self.last = 0
        self.pq = []

    def reserve(self):
        if not self.pq:
            self.last += 1
            return self.last
        return heapq.heappop(self.pq)

    def unreserve(self, seatNumber):
        if seatNumber == self.last:
            self.last -= 1
        else:
            heapq.heappush(self.pq, seatNumber)

if __name__ == '__main__':
    seat_manager = SeatManager(5)

    result = []
    result.append(None)
    result.append(seat_manager.reserve())
    result.append(seat_manager.reserve())
    result.append(seat_manager.unreserve(2))
    result.append(seat_manager.reserve())
    result.append(seat_manager.reserve())
    result.append(seat_manager.reserve())
    result.append(seat_manager.reserve())
    result.append(seat_manager.reserve())
    result.append(seat_manager.unreserve(5))

    print("Results:", result)
