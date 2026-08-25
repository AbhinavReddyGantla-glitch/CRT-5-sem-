#Count no. of objects created for a class
class A:
    count = 0
    def __init__(self):
        A.count += 1


a = A()
b = A()
c = A()
print("Object count is:",A.count)

#1603. Design Parking System
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big > 0:
            self.big -= 1
            return True
        elif carType == 2 and self.medium > 0:
            self.medium -= 1
            return True
        elif carType == 3 and self.small > 0:
            self.small -= 1
            return True
        else:
            return False

#1845. Seat Reservation Manager
class SeatManager:
    def __init__(self, n: int):
        self.seats = [i for i in range(1,n+1)]

    def reserve(self) -> int:
        return self.seats.pop(0)

    def unreserve(self, seatNumber: int) -> None:
        self.seats.append(seatNumber)
        self.seats.sort()
        