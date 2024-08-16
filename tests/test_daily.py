import pytest
from diary.daily import daily_note,modify_daily_date,modify_description_daily,switch_do_daily
import datetime
from dateutil import tz
import calendar

def test_daily_note():
    name = 'name'
    description = 'description'
    year = 2023
    month = 2
    day = 10
    hour = 20
    minute = 35
    minut_duration = 45
    do = False

    time_zone = tz.gettz('Europe/Paris')
    start_datetime = datetime.datetime(year, month, day, hour, minute, 0, tzinfo=time_zone)
    end_datetime = start_datetime + datetime.timedelta(minutes=minut_duration)
    obj_daily = daily_note(name,description,year,month,day,hour,minute,minut_duration,do,'456789')
    expected_result = {
        'univoc_id': obj_daily['univoc_id'],
        'id_diary': obj_daily['id_diary'],
        'name': name,
        'description': description,
        'date start': start_datetime.strftime('%Y-%m-%d %H:%M:%S'),
        'date and': end_datetime.strftime('%Y-%m-%d %H:%M:%S'),
        'do': do,
        'repeat': False,
        'calendar': [calendar.month(year, month)]
    }


    assert obj_daily == expected_result

def test_modify_daily_date():
    name = 'name'
    description = 'description'
    year = 2023
    month = 2
    day = 10
    hour = 20
    minute = 35
    minut_duration = 45
    do = False

    obj_daily = daily_note(name,description,year,month,day,hour,minute,minut_duration,do,'456789')

    year_change = 2024
    month_hange = 3
    day_change = 7
    hour_change = 10
    minute_change = 15
    minut_duraction_change = 120


    time_zone = tz.gettz('Europe/Paris')
    start_datetime2 = datetime.datetime(year_change, month_hange, day_change, hour_change,minute_change, 0, tzinfo=time_zone)
    end_datetime2 = start_datetime2 + datetime.timedelta(minutes=minut_duraction_change)

    new_obj_changed = {
        'univoc_id': obj_daily['univoc_id'],
        'id_diary': obj_daily['id_diary'],
        'name': name,
        'description': description,
        'date start': start_datetime2.strftime('%Y-%m-%d %H:%M:%S'),
        'date and': end_datetime2.strftime('%Y-%m-%d %H:%M:%S'),
        'do': do,
        'repeat': False,
        'calendar': [calendar.month(year_change, month_hange)]
    }

    assert modify_daily_date(obj_daily, year_change, month_hange, day_change,hour_change,minute_change,minut_duraction_change) == new_obj_changed

def test_modify_description_daily():
    name = 'name'
    description = 'description'
    year = 2023
    month = 2
    day = 10
    hour = 20
    minute = 35
    minut_duration = 45
    do = False

    obj_daily = daily_note(name, description, year, month, day, hour, minute, minut_duration, do,'456789')

    new_descriptio = 'New desription to test'
    new_obj = modify_description_daily(obj_daily, new_descriptio)


    assert new_obj['description'] == new_descriptio

def test_switch_do_daily():
    name = 'name'
    description = 'description'
    year = 2023
    month = 2
    day = 10
    hour = 20
    minute = 35
    minut_duration = 45
    do = False

    obj_daily = daily_note(name, description, year, month, day, hour, minute, minut_duration, do,'456789')

    new_obj = switch_do_daily(obj_daily)
    assert new_obj['do'] == True

    new_obj = switch_do_daily(obj_daily)
    assert new_obj['do'] == False