import pytest
from diary.monthly import monthly_note,modify_monthly_month,modify_monthly_description,switch_do_monthly
import datetime
from dateutil import tz
import calendar


def test_monthly_note():
    name = 'Test monthly'
    description = ''
    year = 2023
    month = 7
    do = False

    start_date = datetime.date(year, month, 1)
    and_date = datetime.date(year, month, calendar.monthrange(year, month)[1])

    expected_result = {
        'name': name,
        'description':description,
        'date start': datetime.date.strftime(start_date, '%d %B %Y'),
        'date and': datetime.date.strftime(and_date, '%d %B %Y'),
        'do': do,
        'repeat': False,
        'calendar': [calendar.month(year, month)]
    }

    assert monthly_note(name,description,year,month,do) == expected_result