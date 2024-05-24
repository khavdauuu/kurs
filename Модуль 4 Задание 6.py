import datetime

string_datetime = input()

def parse_time(s):
    # YOUR CODE HERE
    date_time = datetime.datetime.strptime(s, "%Y %m %d %H %M %S")
    result_date_time = date_time + datetime.timedelta(days=1)
    result = result_date_time.day
    return result

print(parse_time(string_datetime))