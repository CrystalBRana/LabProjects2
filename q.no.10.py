# Write a python program to convert seconds to day, hour, minutes and seconds.

seconds = int(input('Insert second:'))
seconds_in_day = 60*60*24
seconds_in_hour = 60*60
seconds_in_minute = 60

days = seconds // seconds_in_day
hours = (seconds - (days * seconds_in_day))// seconds_in_hour
minutes = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute
print(days, hours)
