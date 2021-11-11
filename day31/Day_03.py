class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(args):
        hour, minute, second = map(int, args.split(':'))
        return hour <= 24 and minute <= 59 and second <= 60

    @classmethod
    def from_string(cls, args):
        hour, minute, second = map(int, args.split(':'))
        t = cls(hour, minute, second)
        return t

time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')
