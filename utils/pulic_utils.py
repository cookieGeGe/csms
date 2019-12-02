import datetime


def timeformat(str1):
    newstr = str1[:10] + ' ' + str1[11:19]
    return datetime.datetime.strptime(newstr, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=8)


def str_to_datetime(time_str):
    temptime = datetime.datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    return temptime + datetime.timedelta(hours=8)


def str_to_date(newstr):
    # newstr = str1[:10] + ' ' + str1[11:19]
    return datetime.datetime.strptime(newstr, "%Y-%m-%d")


def month_year_to_date(newstr):
    return datetime.datetime.strptime(newstr, "%Y-%m")


def date_to_datetime(time_str):
    return datetime.datetime.strptime(time_str, "%Y-%m-%d")
