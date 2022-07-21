class Vector:
    def __init__(self, arr=[]):
        self.arr = arr

    def add(self, other):
        assert(len(self.arr) == len(other.arr))
        new_vector = Vector([])

        for i in range(len(self.arr)):
            new_vector.arr.append(self.arr[i]+other.arr[i])

        return new_vector

    def subtract(self, other):
        assert(len(self.arr) == len(other.arr))
        new_vector = Vector([])

        for i in range(len(self.arr)):
            new_vector.arr.append(self.arr[i]-other.arr[i])

        return new_vector

    def dot(self, other):
        assert(len(self.arr) == len(other.arr))
        new_vector = Vector([])

        for i in range(len(self.arr)):
            new_vector.arr.append(self.arr[i]*other.arr[i])

        return new_vector

    def norm(self):
        total = 0

        for num in self.arr:
            total += num**2

        return total**.5

    def equals(self, other):
        if len(self.arr) == len(other.arr) and self.arr == other.arr:
            return True

        return False
