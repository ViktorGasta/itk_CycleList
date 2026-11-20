class CycleList:
    def __init__(self, data):
        self._data = list(data)

    def __getitem__(self, index):
        if not self._data:
            raise IndexError("Невозможно получить элемент из пустого CycleList")

        if isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            return [self[i] for i in range(start or 0, stop or len(self), step or 1)]

        cyclic_index = index % len(self._data)
        return self._data[cyclic_index]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return f"CycleList({self._data!r})"


cl = CycleList([1, 2, 3])

print(cl[0])
print(cl[3])
print(cl[5])
print(cl[-1])
print(cl[-4])
print(len(cl))
print(str(cl))
print(list(cl))
