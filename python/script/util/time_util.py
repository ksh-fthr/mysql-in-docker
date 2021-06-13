from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), 'JST')

def jst_time(current_time):
    return datetime.fromtimestamp(current_time, JST)

def elapsed_time(start, end):
    return end - start
