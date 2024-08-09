import pytest
from diary.period import get_period_from,get_period_to,period_note
import datetime
from dateutil import tz
import calendar

def test_get_period_from():
    year = 2023
    month = 10
    day = 14
    hour = 12
    minute = 35

    expected_result = {'year':year,'month':month,'day':day,'hour':hour,'minute':minute}

    assert get_period_from(year,month,day,hour,minute) == expected_result


def test_get_period_to():
    year = 2023
    month = 10
    day = 14
    hour = 12
    minute = 35

    expected_result = {'year':year,'month':month,'day':day,'hour':hour,'minute':minute}

    assert get_period_to(year,month,day,hour,minute) == expected_result

def test_period_note():
    name = 'Test period'
    description = 'Test period description'
    period_from = get_period_from(2024,10,11,13,15)
    period_to = get_period_to(2025,1,1,14,0)
    do = False

    time_zone = tz.gettz('Europe/Paris')
    date_from = datetime.datetime(period_from['year'], period_from['month'], period_from['day'], period_from['hour'],
                                  period_from['minute'], tzinfo=time_zone)
    date_from_format = datetime.datetime.strftime(date_from, '%d %B %Y %H:%M:%S')
    date_to = datetime.datetime(period_to['year'], period_to['month'], period_to['day'], period_to['hour'],
                                period_to['minute'], tzinfo=time_zone)
    date_to_format = datetime.datetime.strftime(date_to, '%d %B %Y %H:%M:%S')
    calendar_period = []

    if period_from['year'] == period_to['year']:
        calendar_period = [calendar.month(period_from['year'], month) for month in
                           range(period_from['month'], period_to['month'] + 1)]
    else:
        for year in range(period_from['year'], period_to['year'] + 1):
            if year == period_from['year']:
                for month in range(period_from['month'], 13):
                    calendar_period.append(calendar.month(year, month))

            if year != period_to['year'] and year != period_from['year']:
                calendar_period.append(calendar.calendar(year))

            if year == period_to['year']:
                for month in range(1, period_to['month'] + 1):
                    calendar_period.append(calendar.month(year, month))

    expected_result = {
        'name': name,
        'description': description,
        'date start': date_from_format,
        'date and': date_to_format,
        'do': do,
        'repeat': False,
        'calendar': calendar_period
    }

    assert period_note(name,description,period_from,period_to,do) == expected_result