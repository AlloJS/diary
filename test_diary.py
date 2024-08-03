from diary.new_diary import Diary
from diary import monthly
from diary import daily

# Creo nuovo diario
d = Diary('Diary of Angelo')
# Creo evento del giorno
event = daily.daily_note('Test Event','Test to insert invent on diary',2024,7,29,16,15,90,True)
# Inserisco evento nel diario
d.put_event_diary(event)
# Modifico evento cambio data
modify_event = daily.modify_daily_date(event,2025,5,29,10,0,190)
# Verifio evento nel diario
print(d.diary)
