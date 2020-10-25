# having the days of the week in the form of
# "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
# given a string s indicating a day of the week and a number k
# return what day of the week will be k days
# example s="Sat" k = 9 should return "Mon"
# example s="Mon" k = 3 should return "Thu"

def solution(s, k):
    days_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    week_length = 7
    current_index = days_of_the_week.index(s)
    remaining = (k + current_index) % week_length
    return days_of_the_week[remaining]


assert solution("Sat", 9) == "Mon"
assert solution("Wed", 210) == "Wed"
assert solution("Thu", 2) == "Sat"

print("Ok")
