class Time:
    """time of day"""

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def mul_time(time, x):
    seconds = time_to_int(time) * x
    return int_to_time(int(seconds))

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

t = Time()
t.hour = 0
t.minute = 58
t.second = 35

def find_rate(distance, time):
    return mul_time(time, 1/distance)

print_time(find_rate(10, t))
