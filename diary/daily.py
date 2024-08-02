import datetime
import time
import calendar

def _daily_note(year,month,day,description,do):

    d_d = datetime.date(year,month,day)
    date_diary = datetime.date.strftime(d_d,'%Y-%m-%d')
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
    str_daily = 'Month of:\n' + obj_daily['calendar'] + '\n' + obj_daily['date'] + ':\n' + obj_daily['description'] + '\n' + 'Do:' + str(obj_daily['do'])
    return str_daily


