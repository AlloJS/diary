
from diary.new_diary import Diary
from diary.diary_DB import DiarySQL
from diary import monthly
from diary import daily
from diary import period
import diary.diary_excel
# 65592250285068942839
d = DiarySQL('My diary new','localhost','Diary','root','root','65592250285068942839')

#print(d.__dict__)

# Operation to daily module
event_dealy =daily.daily_note('Daily event3','My first daily event2',2024,8,15,14,51,5,False,d.id_diary)
daily.modify_daily_date(event_dealy,2024,8,15,15,0,6)
daily.switch_do_daily(event_dealy)
daily.modify_description_daily(event_dealy,'My first daily event modify2')
# Operation to monthtly modules
monthly_event = monthly.monthly_note('Monthly Event3','My first monthly event2',2024,8,False,d.id_diary)
monthly.modify_monthly_month(monthly_event,2024,7)
monthly.switch_do_monthly(monthly_event)
monthly.modify_monthly_description(monthly_event,'My first event monthly modify2')
# Operation to period module
event_period = period.period_note('Period event3','My first event period2',period.get_period_from(2024,8,1,10,0),period.get_period_to(2024,8,31,10,0),False,d.id_diary)
period.change_period(event_period,period.get_period_from(2023,8,1,10,0),period.get_period_to(2024,10,31,10,0))
period.modify_period_description(event_period,'My first event period modify2')
period.switch_do_period(event_period)
#d.put_event_diary(event_dealy)
#d.put_event_diary(monthly_event)
#d.put_event_diary(event_period)

#print(d.convert_diary_str())
#d.diary[0]['univoc_id'] = '3541791985364674716'

#d.write_events_DB()
#diary.diary_excel.save_diary_excel('excel_angelo.xlsx',d.diary)
d.orderby_startdata('decrescente')
print(d.diary[0])
print(d.diary[1])
print(d.diary[2])
print(d.diary[3])
print(d.diary[4])
print(d.diary[5])
print(d.diary[6])
print(d.diary[7])
print(d.diary[8])


