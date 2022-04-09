'''
ID успешной посылки 58715158

--ПРИНЦИП РАБОТЫ--
Я реализовала дек на кольцевом буфере. Есть два указателя:
head - индекс, по которому можно добавлять элемент в начало дека
tail - индекс, по которому можно добавлять элемент в конец дека
Соответственно, обращаясь к этим же указателям, отнимая единицу, можно извлекать элемент из дека
Если дек переполняется, то выводится сообщение об ошибке: "error"

--ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ--
Из описания алгоритма следует, что при необходимости положить элемент в дек или извлечь его от туда,
программа не использует дополнительную память и не проходится по всему массиву. Поскольку указатель
head всегда указывает на ячейку, которая расположена перед ячейкой верхушки дека, а указатель tail
всегда указывает на ячейку, которая расположена за конечной заполненной ячейкой дека. Поэтому действия
извлечения и добавления элемента осуществляется на О(1)

--ВРЕМЕННАЯ СЛОЖНОСТЬ--
Добавление и извлечение элемента из дека стоит О(1). Поскольку количество операций с деком равно n,
чтобы произвести все эти n операций, каждое из которых затрачивает О(1) по времени, временная сложность
программы будет О(n)

--ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ--
В условии задачи задано число m - максимальный размер дека. Так как реализация дека строится на массиве,
длина которого фиксирована и равна m, а другая память не выделяется для реализации извлечения и добавления
элемента, то пространственная сложность программы составит O(m)
'''

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