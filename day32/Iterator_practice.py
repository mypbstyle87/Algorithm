class TimeIterator:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __getitem__(self, index):
        if index + self.current < self.stop:
            r = self.current + index
            self.hour = r // 3600 % 24
            self.minute = r // 60 % 60
            self.second = r % 60
            return f'{self.hour:02}:{self.minute:02}:{self.second:02}'
        else:
            raise IndexError

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     if self.current < self.stop:
    #         r = self.current
    #         self.current += 1
    #         self.hour = r // 3600 % 24
    #         self.minute = r // 60 % 60
    #         self.second = r % 60
    #         return f'{self.hour:02}:{self.minute:02}:{self.second:02}'
    #     else:
    #         raise StopIteration


start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')
