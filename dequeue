class Dequeue:
    def __init__(self, max_size):
        self.dequeue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.dq_size = 0

    def is_empty(self):
        return self.dq_size == 0

    def push_front(self, item):
        if self.dq_size >= self.max_size:
            raise AssertionError
        self.dequeue[self.head] = item
        if (self.head == 0):
            self.head = self.max_size - 1
            if self.tail == 0 and self.dq_size == 0:
                self.tail = 1
        else:
            self.head = self.head - 1
        self.dq_size += 1

    def push_back(self, item):
        if self.dq_size >= self.max_size:
            raise AssertionError
        if (self.head == 0 and self.tail == 0 and self.dq_size == 0):
            self.head = self.max_size - 1
        self.dequeue[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.dq_size += 1

    def pop_front(self) -> int:
        if self.is_empty():
            raise AssertionError
        self.head = (self.head + 1) % self.max_size
        head_value = self.dequeue[self.head]
        self.dequeue[self.head] = None
        self.dq_size -= 1
        return head_value

    def pop_back(self) -> int:
        if self.is_empty():
            raise AssertionError
        if self.tail == 0:
            self.tail = self.max_size - 1
        else:
            self.tail = self.tail - 1
        tail_value = self.dequeue[self.tail]
        self.dequeue[self.tail] = None
        self.dq_size -= 1
        return tail_value

def main():
    n = int(input())
    m = int(input())
    dequeue = Dequeue(m)
    for i in range(n):
        s = input()
        if (s == "pop_front"):
            try:
                print(dequeue.pop_front())
            except AssertionError:
                print("error")
        elif (s == "pop_back"):
            try:
                print(dequeue.pop_back())
            except AssertionError:
                print("error")
        else:
            command, arg = s.split(' ')
            if (command == "push_front"):
                try:
                    dequeue.push_front(int(arg))
                except AssertionError:
                    print("error")
            else:
                try:
                    dequeue.push_back(int(arg))
                except AssertionError:
                    print("error")

if __name__ == '__main__':
    main()
