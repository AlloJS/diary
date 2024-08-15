import pytest
from diary.monthly import monthly_note,modify_monthly_month,modify_monthly_description,switch_do_monthly
import datetime
import calendar

def test_monthly_note():
    name = 'Test monthly'
    description = ''
    year = 2023
    month = 7
    do = False

    start_date = datetime.date(year, month, 1)
    and_date = datetime.date(year, month, calendar.monthrange(year, month)[1])
    obj_monthly = monthly_note(name,description,year,month,do)
    expected_result = {
        'univoc_id' : obj_monthly['univoc_id'],
        'name': name,
        'description':description,
        'date start': datetime.date.strftime(start_date, '%Y-%m-%d %H:%M:%S'),
        'date and': datetime.date.strftime(and_date, '%Y-%m-%d %H:%M:%S'),
        'do': do,
        'repeat': False,
        'calendar': [calendar.month(year, month)]
    }

    assert obj_monthly == expected_result


def test_modify_monthly_month():
    name = 'Test monthly'
    description = ''
    year = 2023
    month = 7
    do = False

    obj_monthly = monthly_note(name, description, year, month, do)

    new_year = 2005
    new_month = 1
    expected_result = modify_monthly_month(obj_monthly,new_year,new_month)

    start_date = datetime.date(new_year,new_month,1)
    end_date = datetime.date(new_year,new_month,calendar.monthrange(new_year,new_month)[1])

    assert expected_result['date start'] == datetime.date.strftime(start_date, '%Y-%m-%d %H:%M:%S')
    assert expected_result['date and'] == datetime.date.strftime(end_date, '%Y-%m-%d %H:%M:%S')


def test_modify_monthly_description():
    name = 'Test monthly'
    description = ''
    year = 2023
    month = 7
    do = False

    obj_monthly = monthly_note(name, description, year, month, do)
    new_description = 'Change Description'

    expected_result = modify_monthly_description(obj_monthly,new_description)

    assert expected_result['description'] == new_description


def test_switch_do_monthly():
    name = 'Test monthly'
    description = ''
    year = 2023
    month = 7
    do = False

    obj_monthly = monthly_note(name, description, year, month, do)
    expected_result = switch_do_monthly(obj_monthly)
    assert expected_result['do'] == True

    expected_result = switch_do_monthly(obj_monthly)
    assert expected_result['do'] == False
