# Насколько мне известно, существует два основных способа создания циклического буфера,
# а именно: 1. с помощью очереди (односвязной или двусвязной), 2. с помощью массива.

# Первая реализация (RingBuffer) в качестве хранилища использует ограниченную очередь,
# что позволяет избежать проверки заполнения хранилища,
# но доступ к произвольному элементу в худшем случае за линейное время от длины очереди.

# Вторая реализация (RingBuffer2) в качестве хранилища использует ограниченный массив
# (в данном случае list), что требует дополнительной проверки на заполненность хранилища,
# но доступ к произвольному элементу в худшем случае за константное время от длины массива.


from collections import deque


class RingBuffer(object):
    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.data = deque(maxlen=maxlen)

    def __len__(self):
        return self.length()

    def __getitem__(self, idx):
        if idx < 0 or idx >= self.length():
            raise KeyError()
        return self.data[idx]

    def append(self, v):
        self.data.append(v)

    def get(self):
        return self.data

    def length(self):
        return len(self.data)


class RingBuffer2:
    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.data = []

    def __len__(self):
        return self.length()

    def __getitem__(self, idx):
        if idx < 0 or idx >= self.length():
            raise KeyError()
        return self.data[idx]

    class __Full:
        def append(self, x):
            self.data[self.cur] = x
            self.cur = (self.cur + 1) % self.maxlen

        def get(self):
            return self.data[self.cur:] + self.data[:self.cur]

    def append(self, x):
        self.data.append(x)
        if len(self.data) == self.maxlen:
            self.cur = 0
            self.__Full.__len__ = self.__class__.__len__
            self.__Full.length = self.__class__.length
            self.__Full.__getitem__ = self.__class__.__getitem__
            self.__class__ = self.__Full

    def get(self):
        return self.data

    def length(self):
        return len(self.data)


