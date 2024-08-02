import datetime
import time
import calendar
from dateutil import tz
def _daily_note(year,month,day,description,do):
    time_zone = tz.tzutc()
    #region = tz.gettz('Europe/Paris')
    d_d = datetime.datetime(year,month,day,tzinfo=time_zone)
    date_diary = datetime.datetime.strftime(d_d,'%Y-%m-%d %H:%M:%S')
    obj_diary = {'date':date_diary,'description':description,'do':do,'calendar':calendar.month(year,month)}
    return obj_diary


def get_daily_diary(year,month,day,description,do):
    '''
        :param year: year of date daily diary
        :param month: month of date daily diary
        :param day: day of date daily diary
        :param description: description of daily diary
        :param do: do of daily diary and to be True of False
        :return: Return a string of daily diary
    '''
    obj_daily = _daily_note(year, month, day, description, do)
    str_daily = (f"Month of:\n{obj_daily['calendar']}\n"
                 f"{obj_daily['date']}:\n{obj_daily['description']}\n"
                 f"Do: {obj_daily['do']}")
    
    return str_daily


print(get_daily_diary(2024,9,10,'Compleanno Angelo',False))



