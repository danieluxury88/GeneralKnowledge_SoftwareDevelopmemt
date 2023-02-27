# Python arrays are dynamic by default, but this is an exanmple of resizing


class MyArray:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2

    # Insert n in the latest position of the array
    def pushback(self, n):
        print(f"Capacity {self.capacity} Len: {len(self.arr)} Length: {self.length}")
        if self.length == self.capacity:
            self.resize()

        # insert at the next empty position
        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        # copy elements to newArr
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr
        # print(f"Capacity {self.capacity} Len: {len(self.arr)}")

    # Remove the last element in the array
    def popback(self):
        if self.length > 0:
            self.length -= 1


array = MyArray()
array.pushback(2)
array.pushback(1)
print(array.length)
array.pushback(2)
array.pushback(1)
print(array.length)
array.pushback(3)
print(len(array.arr))
