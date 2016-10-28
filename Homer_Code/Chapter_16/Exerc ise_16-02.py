import datetime as dt
import calendar

current = dt.datetime.now()

print('Today is ' + calendar.day_name[current.weekday()] + '.')

def bday_report(mm,dd,year):
    bday = dt.datetime(year = year, month = mm, day = dd)
    current = dt.datetime.now()
    bday_this_year = bday.replace(year = current.year)
    next_bday_year = current.year
    if bday_this_year < current:
       age = current.year - bday.year
       next_bday_year += 1 # wait til next year for bday
    else:
        age = current.year - bday.year - 1
    print('You are ' + str(age) + ' year(s) old.')
    next_bday = bday.replace(year = next_bday_year)
    diff = next_bday - current
    days = str(diff.days)
    hours, seconds = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    hours = str(hours)
    minutes = str(minutes)
    seconds = str(seconds)
    print('Time until next birthday is ' +
                days + ' days, ' +
                hours + ' hours, ' +
                minutes + ' minutes and ' +
                seconds + ' seconds.')


bday_report(mm=3, dd=14, year = 1963)
