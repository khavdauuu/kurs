import datetime

days, seconds = int(input()), int(input())

def shift_time(days: int, seconds: int):
    # YOUR CODE HERE
    date_time = datetime.datetime(2023, 1, 1, 12, 30, 0)
    result_date_time = date_time + datetime.timedelta(days=days, seconds=seconds)
    result = (result_date_time.day, result_date_time.second)
    return result

print(shift_time(days, seconds))