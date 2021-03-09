''' You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops
on the way. How long will the bus journey take? Alternatively, you could run to university. You jog the first
mile at 7mph; then run the next two at 15mph; before jogging the last at 7mph again. Will this be quicker or slower
 than the bus? '''

living_miles_apart =  4
bus_speed = 25
time_taken = ((living_miles_apart/bus_speed)*60)
# 2 minutes in each stop
time_spends = 20
total_time = time_taken + time_spends
print(f'Total time taken by bus is {total_time}')

first_jog = (1/7)* 60
second_jog = (2/15) * 60
third_jog = (1/7) * 60
total_jog = first_jog + second_jog + third_jog
print('Total time taken by jogging is', total_jog)

if total_jog < total_time:
    print("Jogging is faster than taking bus.")
else:
    print("Taking bus is faster than jogging")
