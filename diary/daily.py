try:
    from .diary_except import ErrorDate  # Importazione relativa per Sphinx
except ImportError:
    from diary_except import ErrorDate   # Importazione assoluta per l'esecuzione normale

import datetime
import calendar
from dateutil import tz

def daily_note(year,month,day,description,do):
    '''
           :param year: year of date daily diary
           :param month: month of date daily diary
           :param day: day of date daily diary
           :param description: description of daily diary
           :param do: do of daily diary and to be True of False
           :return: Return a string of daily diary
    '''
    try:
        if month not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            raise ErrorDate('Month is not real')

        if day not in range(1,31):
            raise ErrorDate('Day is not real')

        time_zone = tz.gettz('Europe/Paris')
        d_d = datetime.datetime(year,month,day,tzinfo=time_zone)
        date_diary = datetime.datetime.strftime(d_d,'%Y-%m-%d %H:%M:%S')
        obj_diary = {'date':date_diary,'description':description,'do':do,'calendar':calendar.month(year,month)}
        return obj_diary
    except ErrorDate as ed:
        print(ed.message)


def modify_daily_date(obj_daily,year,month,day):
    '''
        :param obj_daily: Objec daily diary to modify
        :param year: new year to change
        :param month: new month to change
        :param day: new day to change
        :return: Object diary modify
    '''
    try:
        if month not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            raise ErrorDate('Month is not real')

        if day not in range(1,31):
            raise ErrorDate('Day is not real')

        time_zone = tz.gettz('Europe/Paris')
        d_d = datetime.datetime(year, month, day, tzinfo=time_zone)
        date_diary = datetime.datetime.strftime(d_d, '%Y-%m-%d %H:%M:%S')
        obj_daily['calendar']= calendar.month(year,month)
        obj_daily['date'] = date_diary
        return obj_daily
    except ErrorDate as ed:
        print(ed.message)

def modify_desription_daily(obj_daily,description):
    '''
        :param obj_daily: Object daily to modify
        :param description: New description to change
        :return: Object daily modify
    '''
    obj_daily['description'] = description
    return obj_daily

def switch_do_daily(obj_daily):
    '''
        :param obj_daily: Object daily to modify
        :return: Object daily modify to do
    '''
    if obj_daily['do'] == True:
        obj_daily['do'] = False
    else:
        obj_daily['do'] = True

def convert_obj_to_string(obj_daily):
    '''
    :param obj_daily:
    :return:
    '''
    str_daily = (f"{obj_daily['calendar']}\n"
                 f"{obj_daily['date']}:\n{obj_daily['description']}\n"
                 f"Do: {obj_daily['do']}")

    return str_daily


