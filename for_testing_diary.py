from diary.new_diary import Diary
from diary import monthly
from diary import daily
from diary import period

# Creo nuovo diario
d = Diary('Diary of Angelo')
# Creo evento del giorno
event = daily.daily_note('Test Event','Test to insert invent on diary',2024,7,29,16,15,90,True)
# Inserisco evento nel diario
d.put_event_diary(event)
# Modifico evento cambio data
daily.modify_daily_date(event,2025,5,29,10,0,190)
# Verifio evento nel diario
#print(d.diary)
new_event_monthly = monthly.monthly_note('Mese test','Test evento mese',2024,9,False)
d.diary.append(new_event_monthly)
#print(d.diary)
monthly.modify_monthly_month(new_event_monthly,2024,8)
new_event_period_from = period.get_period_from(2024,11,10,10,30)
new_event_period_to = period.get_period_to(2027 ,3,1,23,30)
new_period = period.period_note('Test periodo','Test evento periodo da a',new_event_period_from,new_event_period_to,False)
d.diary.append(new_period)
print(d.diary)
print(d.convert_diary_str())

name = 'name'
description = 'description'
year = 2023
month = 2
day = 10
hour = 20
minute = 35
minut_duration = 45
do = False

obj_daily = daily.daily_note(name, description, year, month, day, hour, minute, minut_duration, do)
print('TO TEST')
print(obj_daily)
