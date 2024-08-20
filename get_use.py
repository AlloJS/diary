from diary.new_diary import create_diary, put_event_diary, convert_diary_str
from diary.diary_DB import create_connection, write_DB_diary_creation, write_events_DB,start_diary
from diary.daily import daily_note, modify_daily_date, switch_do_daily

# Crea una nuova connessione al database
connection = create_connection('localhost', 'Diary', 'root', 'root')
# 98286892737048743
# Crea un nuovo diario
# Creare o selezionare un diario
try:
    existing_or_new_diary = start_diary(connection,id_diary='98286892737048743')
except ValueError as e:
    print(e)
    # Potresti voler gestire la creazione di un nuovo diario in questo caso

# Aggiungere un evento al diario selezionato o creato
event = daily_note('Meeting404', 'Discussione importante', 2024, 8, 20, 15, 30, 60, False, existing_or_new_diary['id_diary'])
updated_diary = put_event_diary(existing_or_new_diary, event)

# Scrivere l'evento nel database
write_events_DB(connection, event)
