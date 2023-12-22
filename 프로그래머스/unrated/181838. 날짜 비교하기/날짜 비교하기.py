import datetime

def solution(date1, date2):
    return int(datetime.datetime(date1[0], date1[1], date1[2]) < datetime.datetime(date2[0], date2[1], date2[2])) 
