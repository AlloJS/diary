import pytest
import datetime
import pytz.tzinfo
from ..diary.new_diary import (
    _set_data_creation,
    create_diary,
    put_event_diary,
    convert_diary_str,
    orderby_startdata,
    orderby_name_event
)
from ..diary.diary_except import ErrorAllowedValue

def test_create_diary():
    name = "Test Diary"
    diary = create_diary(name)
    assert diary['name'] == name
    assert diary['diary'] == []
    assert isinstance(diary['date_creation'], datetime.datetime)
    assert isinstance(diary['id_diary'], str)
    assert len(diary['id_diary']) > 0

def test_put_event_diary():
    diary = create_diary("Test Diary")
    event = {
        'name': 'Test Event',
        'description': 'This is a test event',
        'date_start': '2024-08-15 14:30:00',
        'date_and': '2024-08-15 15:30:00',
        'do': False
    }
    updated_diary = put_event_diary(diary, event)
    assert len(updated_diary['diary']) == 1
    assert updated_diary['diary'][0] == event

def convert_diary_str(diary):
    """
    Converte il diario in una stringa.
    :param diary: Il diario da convertire.
    :return: Diario in una stringa.
    """
    str_diary = ''
    for event in diary['diary']:
        try:
            data_start_parsed = datetime.datetime.strptime(event['date_start'], '%Y-%m-%d %H:%M:%S')
            dsf = datetime.datetime.strftime(data_start_parsed, '%d %B %Y %H:%M:%S')
            data_and_parsed = datetime.datetime.strptime(event['date_and'], '%Y-%m-%d %H:%M:%S')
            daf = datetime.datetime.strftime(data_and_parsed, '%d %B %Y %H:%M:%S')
        except ValueError as e:
            print(e)
            continue

        do = 'Fatto' if event['do'] else 'Da svolgere'

        str_diary += (
            f"PERIODO: dal: {dsf} "
            f"al: {daf}\n"
            f"NOME: {event['name']}\n"
            f"DESCRIZIONE: {event['description']}\n"
            f"SVOLTO: {do}\n"
            f"-------------------------------------------\n"
        )

    return str_diary


def test_orderby_startdata():
    diary = [
        {
            'name': 'Event 1',
            'description': 'First event description',
            'date_start': '2024-08-16 16:00:00',
            'date_and': '2024-08-16 17:00:00',
            'do': False
        },
        {
            'name': 'Event 2',
            'description': 'Second event description',
            'date_start': '2024-08-15 14:30:00',
            'date_and': '2024-08-15 15:30:00',
            'do': True
        }
    ]

    # Test crescente
    sorted_diary = orderby_startdata(diary, 'crescente')
    assert sorted_diary[0]['name'] == 'Event 2'

    # Test decrescente
    sorted_diary = orderby_startdata(diary, 'decrescente')
    assert sorted_diary[0]['name'] == 'Event 1'

def test_orderby_startdata_invalid_order():
    diary = []
    with pytest.raises(ErrorAllowedValue):
        orderby_startdata(diary, 'invalid_order')

def test_orderby_name_event():
    diary = {
        'diary': [
            {
                'name': 'Z Event',
                'description': 'Event description',
                'date_start': '2024-08-16 16:00:00',
                'date_and': '2024-08-16 17:00:00',
                'do': False
            },
            {
                'name': 'A Event',
                'description': 'Event description',
                'date_start': '2024-08-15 14:30:00',
                'date_and': '2024-08-15 15:30:00',
                'do': True
            }
        ]
    }

    # Test crescente
    sorted_diary = orderby_name_event(diary, 'crescente')
    assert sorted_diary['diary'][0]['name'] == 'A Event'

    # Test decrescente
    sorted_diary = orderby_name_event(diary, 'decrescente')
    assert sorted_diary['diary'][0]['name'] == 'Z Event'

def test_orderby_name_event_invalid_order():
    diary = {'diary': []}
    with pytest.raises(ErrorAllowedValue):
        orderby_name_event(diary, 'invalid_order')
