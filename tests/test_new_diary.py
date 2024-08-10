from diary.new_diary import Diary
from diary.daily import daily_note
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

