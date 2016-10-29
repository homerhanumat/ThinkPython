class Time(object):
    """Represents the time of day.

    attributes: hour, minute, second
    """
    def __init__(self, seconds=0):
        self.second = seconds

    def __str__(self):
        time2 = int_to_time(self.second)
        return '%.2d:%.2d:%.2d' % (time2.hour, time2.minute, time2.second)

    def print_time(self):
        time2 = int_to_time(self.second)
        print(str(time2))

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        return self.second

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.time_to_int() > other.time_to_int()

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.time_to_int() + other.time_to_int()
        return Time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.time_to_int()
        return Time(seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if self.second < 0:
            return False
        return True

class Time2:
    def __init__(self, hour = 0, minute = 0 , second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def print_time(self):
        print(str(self))

def int_to_time(seconds):
    """Makes a Time2 object from an integer.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time2(hour, minute, second)
    return time


def main():
    start = Time(9 * 3600 + 45 * 60 + 0)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)
    start = Time(9 * 3600 + 45 * 60)
    duration = Time(1 * 3600 + 35 * 60)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7 * 3600 + 43)
    t2 = Time(7 * 3600 + 41)
    t3 = Time(7 * 3600 + 37)
    total = sum([t1, t2, t3])
    print(total)

if __name__ == '__main__':
    main()
