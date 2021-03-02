# given the integer N - the number of minutes that is passed since midnight - how many hours
# and minutes are displayed on the 24th digital clock?
N = int(input('Enter the number of minutes:'))
Hour = N//60
Min = N%60
print(f'The time is',Hour,':',Min)