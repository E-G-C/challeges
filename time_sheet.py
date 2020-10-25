# given a string where each line resprest a day of work
# and each day is represented by an interval of working hours 
# calculate the total number of hours in the timesheet.
# the intervals can be in 24 hours format or not example:
# one day (like shown in the example below) can be
# 10-14, 17:30-21:30
# and other day can be represented in 12 hours format like:
# 11-1, 2:30-4


time_sheet = """9-2
10-11
10-3, 6-8
11-3, 8-10
1-2:30, 6-9
11-2
10-1
11-1, 2:30-4
12-1
10-4, 6-8
9-11, 3-6
8-9, 11-12, 4-6
10-12, 6-9
11-8
11-1:30
11-1, 2-5
11-12
12-6
10-10:30, 11-12, 10-11:30"""


# time_sheet = """10-11, 11:30-4, 5-6
# 7:45-8:30, 10-2
# 8-11:30
# 6-9
# 10:30-12, 1:30-2
# 11-1:30, 5-8, 9-10
# 10-14, 17:30-21:30"""
# # print(time_sheet)

# time_sheet = """7:45-8:30, 10-2
# 10:30-12, 1:30-2
# 11-1:30, 5-8, 9-10
# 10-14, 17:30-21:30
# """

lines = time_sheet.splitlines()


def time_to_minutes(t):
    time_parts = t.split(':') if ':' in t else [t, 0]
    hour = time_parts[0]
    minutes = time_parts[1]
    total = int(hour) * 60 + int(minutes)
    return total


def normalize_hours(t1, t2):
    _t1 = time_to_minutes(t1)
    _t2 = time_to_minutes(t2)

    return _t1, _t2 + (12 * 60) if _t2 < _t1 else _t2


total_hours = 0
for l in lines:
    print('---')
    hours_ranges = l.split(',')
    for hour_range in hours_ranges:
        start_time_str, end_time_str = hour_range.strip().split('-')
        start_time, end_time = normalize_hours(start_time_str, end_time_str)
        minutes_in_range = end_time - start_time
        print(f'{start_time_str=}, {end_time_str=}')
        total_hours += minutes_in_range

print(f'Total hours:{total_hours/60}')
