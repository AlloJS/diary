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

def test_set_data_creation():
    data_creazione = _set_data_creation()
    assert isinstance(data_creazione, datetime.datetime)
    assert data_creazione.tzinfo is not None
    assert data_creazione.tzinfo.tzname(data_creazione) == 'CEST'  # Central European Summer Time



def test_create_diary():
    name = "Test Diary"
    diary = create_diary(name)

    assert isinstance(diary, dict)
    assert diary['name'] == name
    assert isinstance(diary['diary'], list)
    assert isinstance(diary['date_creation'], datetime.datetime)
    assert len(diary['id_diary']) > 0  # Assumendo che l'ID non sia una stringa vuota


def test_put_event_diary():
    diary = create_diary("Test Diary")
    event = {
        'name': 'Meeting',
        'description': 'Discussione importante',
        'date start': '2024-08-20 15:30:00',
        'date and': '2024-08-20 16:30:00',
        'do': False
    }

    updated_diary = put_event_diary(diary, event)

    assert len(updated_diary['diary']) == 1
    assert updated_diary['diary'][0] == event


def test_convert_diary_str():
    diary = create_diary("Test Diary")
    event = {
        'name': 'Meeting',
        'description': 'Discussione importante',
        'date start': '2024-08-20 15:30:00',
        'date and': '2024-08-20 16:30:00',
        'do': False
    }
    put_event_diary(diary, event)

    diary_str = convert_diary_str(diary)

    assert isinstance(diary_str, str)
    assert "PERIODO: dal: 20 August 2024 15:30:00" in diary_str
    assert "NOME: Meeting" in diary_str
    assert "DESCRIZIONE: Discussione importante" in diary_str
    assert "SVOLTO: Da svolgere" in diary_str


def test_orderby_startdata():
    diary = create_diary("Test Diary")
    event1 = {
        'name': 'Meeting 1',
        'description': 'Discussione importante',
        'date start': '2024-08-19 14:30:00',
        'date and': '2024-08-19 15:30:00',
        'do': False
    }
    event2 = {
        'name': 'Meeting 2',
        'description': 'Altro incontro',
        'date start': '2024-08-20 16:00:00',
        'date and': '2024-08-20 17:00:00',
        'do': False
    }
    put_event_diary(diary, event1)
    put_event_diary(diary, event2)

    # Test ordine crescente
    diary_sorted = orderby_startdata(diary, 'crescente')
    assert diary_sorted['diary'][0]['name'] == 'Meeting 1'

    # Test ordine decrescente
    diary_sorted = orderby_startdata(diary, 'decrescente')
    assert diary_sorted['diary'][0]['name'] == 'Meeting 2'

    # Test errore con ordine non valido
    with pytest.raises(ErrorAllowedValue):
        orderby_startdata(diary, 'non valido')




def test_orderby_name_event():
    diary = create_diary("Test Diary")
    event1 = {
        'name': 'Zeta Meeting',
        'description': 'Discussione importante',
        'date start': '2024-08-19 14:30:00',
        'date and': '2024-08-19 15:30:00',
        'do': False
    }
    event2 = {
        'name': 'Alpha Meeting',
        'description': 'Altro incontro',
        'date start': '2024-08-20 16:00:00',
        'date and': '2024-08-20 17:00:00',
        'do': False
    }
    put_event_diary(diary, event1)
    put_event_diary(diary, event2)

    # Test ordine crescente
    diary_sorted = orderby_name_event(diary, 'crescente')
    assert diary_sorted['diary'][0]['name'] == 'Alpha Meeting'

    # Test ordine decrescente
    diary_sorted = orderby_name_event(diary, 'decrescente')
    assert diary_sorted['diary'][0]['name'] == 'Zeta Meeting'

    # Test errore con ordine non valido
    with pytest.raises(ErrorAllowedValue):
        orderby_name_event(diary, 'non valido')
