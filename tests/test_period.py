import pytest
from ..diary.period import get_period_from,get_period_to,period_note,modify_period_description,change_period,switch_do_period
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
    date_from_format = datetime.datetime.strftime(date_from, '%Y-%m-%d %H:%M:%S')
    date_to = datetime.datetime(period_to['year'], period_to['month'], period_to['day'], period_to['hour'],
                                period_to['minute'], tzinfo=time_zone)
    date_to_format = datetime.datetime.strftime(date_to, '%Y-%m-%d %H:%M:%S')
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

    obj_period = period_note(name,description,period_from,period_to,do,'67890')

    expected_result = {
        'univoc_id' : obj_period['univoc_id'],
        'id_diary' : obj_period['id_diary'],
        'name': name,
        'description': description,
        'date start': date_from_format,
        'date and': date_to_format,
        'do': do,
        'repeat': False,
        'calendar': calendar_period
    }

    assert obj_period == expected_result

def test_change_period():
    period_from = get_period_from(2024, 11, 10, 10, 30)
    period_to = get_period_to(2027, 3, 1, 23, 30)
    obj = period_note('Test periodo', 'Test evento periodo da a', period_from, period_to, False,'78909')

    period_from2 = get_period_from(2023, 12, 9, 9, 0)
    period_to2 = get_period_to(2029, 5, 18, 7, 40)
    obj = change_period(obj,period_from2,period_to2)

    time_zone = tz.gettz('Europe/Paris')
    date_from = datetime.datetime(period_from2['year'], period_from2['month'], period_from2['day'], period_from2['hour'],period_from2['minute'], tzinfo=time_zone)
    date_from_format = datetime.datetime.strftime(date_from, '%Y-%m-%d %H:%M:%S')
    date_to = datetime.datetime(period_to2['year'], period_to2['month'], period_to2['day'], period_to2['hour'],period_to2['minute'], tzinfo=time_zone)
    date_to_format = datetime.datetime.strftime(date_to, '%Y-%m-%d %H:%M:%S')
    calendar_period = []

    if period_from2['year'] == period_to2['year']:
        calendar_period = [calendar.month(period_from2['year'], month) for month in range(period_from2['month'],period_to2['month'] + 1)]
    else:
        for year in range(period_from2['year'], period_to2['year'] + 1):
            if year == period_from2['year']:
                for month in range(period_from2['month'], 13):
                    calendar_period.append(calendar.month(year, month))

            if year != period_to2['year'] and year != period_from2['year']:
                calendar_period.append(calendar.calendar(year))

            if year == period_to2['year']:
                for month in range(1, period_to2['month'] + 1):
                    calendar_period.append(calendar.month(year, month))


    assert obj['date start'] == date_from_format
    assert obj['date and'] == date_to_format
    assert obj['calendar'] == calendar_period


def test_modify_period_description():
    description = 'New description'
    new_event_period_from = get_period_from(2024, 11, 10, 10, 30)
    new_event_period_to = get_period_to(2027, 3, 1, 23, 30)
    obj = period_note('Test periodo','Test evento periodo da a',new_event_period_from,new_event_period_to,False,'987654')
    modify_period_description(obj,description)
    assert obj['description'] == description

def test_switch_do_period():
    new_event_period_from = get_period_from(2024, 11, 10, 10, 30)
    new_event_period_to = get_period_to(2027, 3, 1, 23, 30)
    obj = period_note('Test periodo', 'Test evento periodo da a', new_event_period_from, new_event_period_to, False,'765435')
    switch_do_period(obj)
    assert obj['do'] == True