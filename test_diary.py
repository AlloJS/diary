from diary.new_diary import Diary
from diary import monthly
from diary import daily

d = Diary('Diary of Angelo')
print(d)
event = daily.daily_note('Test Event','Test to insert invent on diary',2024,7,29,16,15,True)
d.put_event_diary(event)
print(d.diary)
