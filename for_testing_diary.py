from diary.new_diary import Diary
from diary.diary_txt import write_diary_on_txt,read_diary_txt
from diary.diary_excel import save_diary_excel
from diary import monthly
from diary import daily
from diary import period

d = Diary('My new diary')
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

