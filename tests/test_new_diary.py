from diary.new_diary import Diary
from diary.daily import daily_note
from unittest.mock import patch
from diary.diary_except import ErrorAllowedValue
import datetime
from dateutil import tz
import calendar

def test_put_event_diary():
    obj_diary = Diary('Diary test')
    event = daily_note('Event','Descr event',2024,10,1,18,45,60,False)
    obj_diary.put_event_diary(event)
    assert len(obj_diary.diary) != 0
    assert obj_diary.diary[0] == event

def test_convert_diary_str():
    obj_diary = Diary('Diary test')
    event = daily_note('Event', 'Descr event', 2024, 10, 1, 18, 45, 60, False)
    obj_diary.put_event_diary(event)
    string = obj_diary.convert_diary_str()

    assert type(string) == str


def test_set_data_creation():
    # Istanzia la tua classe
    obj = Diary('Diary test')
    # Definisci la data e ora fittizia che il mock restituirà
    mock_now = datetime.datetime(2024, 8, 15, 10, 30, tzinfo=datetime.timezone.utc)
    # Usa patch per mockare datetime.datetime.now
    with patch('diary.new_diary.datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value = mock_now
        # Chiama la funzione da testare
        result = obj._set_data_creation()
    # Verifica che la data creata sia quella mockata
    assert result == mock_now
    assert obj.date_creation == mock_now

def test_orderby_startdata():
    obj = Diary('Diary test')
    obj2 = Diary('Diary Order Test')
    event1 = {
        'univoc_id': '212121',
        'name': 'E1',
        'description': 'description e1',
        'date start': '2024-08-15 15:00:00',
        'date and': '2024-08-15 16:00:00',
        'do': True,
        'repeat': False,
        'calendar': [calendar.month(2024, 8)]
    }
    event2 = {
        'univoc_id': '212121',
        'name': 'E2',
        'description': 'description e2',
        'date start': '2023-08-15 15:00:00',
        'date and': '2023-08-15 16:00:00',
        'do': True,
        'repeat': False,
        'calendar': [calendar.month(2023, 8)]
    }

    obj.put_event_diary(event1)
    obj.put_event_diary(event2)
    obj.orderby_startdata('decrescente')
    obj2.put_event_diary(event2)
    obj2.put_event_diary(event1)

    assert obj.diary[0] == obj2.diary[0]

def test_orderby_name_event():
    obj = Diary('Diary test')
    obj2 = Diary('Diary Order Test')
    event1 = {
        'univoc_id': '212121',
        'name': 'E1',
        'description': 'description e1',
        'date start': '2024-08-15 15:00:00',
        'date and': '2024-08-15 16:00:00',
        'do': True,
        'repeat': False,
        'calendar': [calendar.month(2024, 8)]
    }
    event2 = {
        'univoc_id': '212121',
        'name': 'E2',
        'description': 'description e2',
        'date start': '2023-08-15 15:00:00',
        'date and': '2023-08-15 16:00:00',
        'do': True,
        'repeat': False,
        'calendar': [calendar.month(2023, 8)]
    }

    obj.put_event_diary(event1)
    obj.put_event_diary(event2)
    obj.orderby_name_event('crescente')
    obj2.put_event_diary(event2)
    obj2.put_event_diary(event1)

    assert obj.diary[0] == obj2.diary[0]
