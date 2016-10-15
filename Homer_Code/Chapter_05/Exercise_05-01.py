import time

# Get elapsed time since epoch:
my_time = time.time()
# Note:  The epoch is 12am, January 1, 1970, UTC.

#Python gives the time since epoch in seconds, so:

print('Seconds since epoch:  ', my_time,sep='')

# How many complete days have elapsed?
# Let's find out:

seconds_in_day = 60*60*24
days = my_time // seconds_in_day
print('Complete days since epoch:  ',int(days),',',sep='')

# Now get number of seconds in the current day:
seconds = my_time % seconds_in_day

# Now figure how many whole-number hours are in this:
plus_hours = int(seconds // 3600)

# and then how many whole minutes:
minutes = seconds // 60
plus_minutes = int(minutes - 60*plus_hours)

# and finally, how many whole seconds are left over:
plus_seconds = int(seconds-3600*plus_hours - 60*plus_minutes)

# Print the results:
print('\tplus ',plus_hours,' hours, ',
      plus_minutes,' minutes and ',
      plus_seconds,' seconds, UTC.', sep ='')

# This is UTC time, which at time of writing (October 14, 1916)
# is four hours ahead od Eastern Standard Time.

# To get local time directly:

lt = time.localtime()

# Using the command:
#    print(lt)
# you can get a list of the attributes of the object lt.
# Then you can print out the ones you want, for example:

print('Local Time:  ',lt.tm_hour,':',lt.tm_min,':',
      lt.tm_sec,', ',lt.tm_mon,'/',
      lt.tm_mday, '/', lt.tm_year,
      ' Eastern Standard Time.',sep = '')
