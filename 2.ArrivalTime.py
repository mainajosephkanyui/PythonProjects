current_hour = int(input("Current Hour(0-23): "))
current_minute = int(input("Current Minute(0-60): "))
trip_time = int(input("Trip Time(In Minutes): "))

add_time = current_minute + trip_time
to_hrs = add_time//60
want_hr = current_hour + to_hrs
want_min = add_time % 60

print("Arrival Time: ", want_hr, ":",want_min )
