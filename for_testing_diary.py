from diary.new_diary import Diary
from diary.diary_DB import DiarySQL
from diary.diary_txt import write_diary_on_txt,read_diary_txt
from diary.diary_excel import save_diary_excel
from diary import monthly
from diary import daily
from diary import period

d = DiarySQL('My diary','localhost','Diary','root','root')
# Operation to daily module
event_dealy =daily.daily_note('Daily event','My first daily event',2024,8,15,14,51,5,False)
daily.modify_daily_date(event_dealy,2024,8,15,15,0,6)
daily.switch_do_daily(event_dealy)
daily.modify_description_daily(event_dealy,'My first daily event modify')
# Operation to monthtly modules
monthly_event = monthly.monthly_note('Monthly Event','My first monthly event',2024,8,False)
monthly.modify_monthly_month(monthly_event,2024,7)
monthly.switch_do_monthly(monthly_event)
monthly.modify_monthly_description(monthly_event,'My first event monthly modify')
# Operation to period module
event_period = period.period_note('Period event','My first event period',period.get_period_from(2024,8,1,10,0),period.get_period_to(2024,8,31,10,0),False)
period.change_period(event_period,period.get_period_from(2023,8,1,10,0),period.get_period_to(2024,10,31,10,0))
period.modify_period_description(event_period,'My first event period modify')
period.switch_do_period(event_period)
d.put_event_diary(event_dealy)
d.put_event_diary(monthly_event)
d.put_event_diary(event_period)
#print(d.diary[0])
#print(d.diary[1])
#print(d.diary[2])

#print(d.convert_diary_str())
d.diary[0]['univoc_id'] = '3541791985364674716'
d.write_events_DB()







"""
d = DiarySQL('My diary','localhost','Diary','root','root')
new_event_period_from = period.get_period_from(2024,11,10,10,30)
new_event_period_to = period.get_period_to(2027 ,3,1,23,30)
new_period = period.period_note('Test periodo','Test evento periodo da a',new_event_period_from,new_event_period_to,False)
new_event_period_from2 = period.get_period_from(2024,9,8,10,30)
new_event_period_to2 = period.get_period_to(2027 ,3,1,23,30)
period.change_period(new_period,new_event_period_from2,new_event_period_to2)
event = daily.daily_note('Test Event','Test to insert invent on diary',2024,7,29,16,15,90,True)
monthly_event = monthly.monthly_note('Evento del mese','Esame AWS',2024,12,False)
d.diary.append(new_period)
d.diary.append(event)
d.diary.append(monthly_event)
d.orderby_startdata('crescente')
#d.orderby_name_event('decrescente')

str_diary = d.convert_diary_str()
write_diary_on_txt('my_test_diary_ordeby_data.txt',str_diary)
read_diary_txt('my_test_diary_ordeby_data.txt')
save_diary_excel('my_diary.xlsx',d.diary)

print(d.diary)

d.write_events_DB()

"""


