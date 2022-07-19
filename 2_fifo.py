# coding=utf-8
class RingBuffer:
    """
    Очередь на кольцевом буфере.
    """
    def __init__(self, value):
        self.queue = [None] * value
        self.max_value = value
        self.size = 0
        self.head = 0
        self.tail = 0

    def is_empty(self):
        """
        Проверка очереди на пустоту.
        """
        return self.size == 0

    def push(self, var):
        """
        Добавление элемента в следующую ячейку.
        """
        if self.size != self.max_value:
            self.queue[self.tail] = var
            self.tail = (self.tail + 1) % self.max_value
            self.size += 1

    def pop(self):
        """
        Извлечение раньше всех добавленного элемента.
        """
        if self.is_empty():
            return None
        var = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_value
        self.size -= 1
        return var

class MagicRingBuffer:
    """
    Реализация еще не заполненного буфера.
    """
    def __init__(self,size_max):
        self.max = size_max
        self.data = []

    class __Full:
        """
        Реализация заполненного буфера.
        """
        def append(self, x):
            """
            Добавление нового элемента, перезаписывающего старый.
            """
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.max
        def get(self):
            """
            Возвращение списка элементов в правильном порядке.
            """
            return self.data[self.cur:]+self.data[:self.cur]

    def append(self,x):
        """
        Добавление элемента в конец буфера.
        """
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            # Изменение класса буфера с ещё не заполненного, на заполненный.
            self.__class__ = self.__Full

    def get(self):
        """
        Возвращение списка элементов с самого старого по самый новый
        """
        return self.data


if __name__ == '__main__':
    print 'Работаем с объектом класса RingBuffer:'
    buffer = RingBuffer(6)
    buffer.push(1)
    buffer.push(2)
    buffer.push(3)
    buffer.push(4)
    print buffer.queue
    print 'Размер списка =', buffer.size
    buffer.pop()
    print buffer.queue
    buffer.push(5)
    buffer.push(6)
    buffer.push(7)
    print buffer.queue
    print 'Размер списка =',buffer.size
    buffer.push(8)
    print buffer.queue
    print 'Размер списка всё ещё =', buffer.size

    array = MagicRingBuffer(5)
    print 'Работаем с объектом класса MagicRingBuffer:'
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)
    print array.__class__, array.get(  )
    array.append(5)
    print array.__class__, array.get(  )
    array.append(6)
    print array.data, array.get(  )
    array.append(7)
    array.append(8)
    array.append(9)
    array.append(10)
    print array.data, array.get(  )
