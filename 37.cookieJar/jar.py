class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError("Exceed capacity")
        return self.size

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("There are not enough cookies")
        self.size -= n
        return self.size

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity should be a non-negative integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size

def main():
    jar = Jar(int(input("Capacity: ")))
    jar.deposit(int(input("deposit: ")))
    jar.withdraw(int(input("withdraw: ")))
    print(jar.size)
    print(jar)

if __name__ == "__main__":
    main()