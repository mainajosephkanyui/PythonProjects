starting_hour = int(input("Starting Hour: "))
starting_minute = int(input("Starting Minute: "))
stopping_hour = int(input("Stopping Hour: "))
stopping_minute = int(input("Stopping Minute: "))
hourly_rate = int(input("Hourly Rate: "))

working_hrs = stopping_hour - starting_hour
working_mins = (stopping_minute - starting_minute) / 60
time_worked = working_hrs + working_mins
payment = time_worked * hourly_rate

print(f"Worked {starting_hour}:{starting_minute:02d} to {stopping_hour}:{starting_minute:02d}")
print(f"Total Hours:{time_worked:.1f}")
print(f"Payment: ${payment:.2f}")