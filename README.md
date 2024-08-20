# Diary Library

Una libreria Python per la gestione di voci di diario quotidiano.

## Descrizione

La libreria `diary` fornisce strumenti per creare, modificare e gestire voci di diario quotidiano, inclusi controlli per date valide e formattazione delle voci.

## Requisiti

- Python 3.x
- MySQL

## Installazione

1. **Clona il Repository**

   ```sh
   git clone https://github.com/AlloJS/Diary.git
   cd tuo-repository
   
2. **Crea ambiente virtuale**

   ```sh
   python -m venv env
   source env/bin/activate  # Su Windows usa: .\env\Scripts\activate

3. **Installazione delle dipendenze**

   ```sh
   pip install -r requirements.txt

4. **Crea le Tabelle nel Database MySQL**

   *Esegui il comando seguente per creare le tabelle nel database specificato. 
   Sostituisci myuser, mypassword, e mydatabase con le tue credenziali e il nome del database.*
   
   ```sh
    python create_tables.py --user=myuser --password=mypassword --database=mydatabase
5. **Inizia a Usare la Libreria con il Database Sceglto**

   ```sh
   from diary.diary_sql import DiarySQL
   
   d = DiarySQL('<Name diary>','<host>','Diary','<user>','<password>')

6. **Uso della Libreria Senza Database**

   ```sh
   from diary.diary import Diary
   connection = create_connection('localhost', 'Diary', 'root', 'root')
   
   try:
       existing_or_new_diary = start_diary(connection,id_diary='98286892737048743')
   except ValueError as e:
       print(e)

7. **Utilizzo del modulo daily per gestire eventi giornalieri**
   
   ```sh
   import daily
   
   # Creazione di un nuovo evento
   event_dealy = daily.daily_note(
       title='Daily event',
       description='My first daily event',
       year=2024,
       month=8,
       day=15,
       hour=14,
       minute=51,
       duration=5,          # Durata in minuti
       is_recurring=False,  # Evento ricorrente o meno
       diary_id=d.id_diary  # ID del diario a cui associare l'evento
   )
   
   # Modifica della data e dell'orario dell'evento
   daily.modify_daily_date(
       event_dealy,
       year=2024,
       month=8,
       day=15,
       hour=15,
       minute=0,
       duration=6  # Nuova durata in minuti
   )
   
   # Attiva o disattiva l'evento
   daily.switch_do_daily(event_dealy)
   
   # Modifica della descrizione dell'evento
   daily.modify_description_daily(
   event_dealy,
   new_description='My first daily event modify'
   )

8. **Utilizzo del modulo monthly per gestire eventi mensili**
   
   ```sh
   import monthly
   
   # Creazione di un nuovo evento mensile
   monthly_event = monthly.monthly_note(
       title='Monthly Event',
       description='My first monthly event',
       year=2024,
       month=8,
       is_recurring=False,  # Evento ricorrente o meno
       diary_id=d.id_diary  # ID del diario a cui associare l'evento
   )
   
   # Modifica del mese dell'evento mensile
   monthly.modify_monthly_month(
       monthly_event,
       year=2024,
       month=7  # Nuovo mese
   )
   
   # Attiva o disattiva l'evento mensile
   monthly.switch_do_monthly(monthly_event)
   
   # Modifica della descrizione dell'evento mensile
   monthly.modify_monthly_description(
       monthly_event,
       new_description='My first event monthly modify'
   )

9. **Utilizzo del modulo period per gestire eventi di un determinato periodo**
   
   ```sh
   import period
   
   # Creazione di un nuovo evento periodico
   event_period = period.period_note(
       title='Period event',
       description='My first event period',
       start=period.get_period_from(2024, 8, 1, 10, 0),
       end=period.get_period_to(2024, 8, 31, 10, 0),
       is_recurring=False,  # Evento ricorrente o meno
       diary_id=d.id_diary  # ID del diario a cui associare l'evento
   )
   
   # Modifica del periodo dell'evento periodico
   period.change_period(
       event_period,
       start=period.get_period_from(2023, 8, 1, 10, 0),
       end=period.get_period_to(2024, 10, 31, 10, 0)
   )
   
   # Modifica della descrizione dell'evento periodico
   period.modify_period_description(
       event_period,
       new_description='My first event period modify'
   )
   
   # Attiva o disattiva l'evento periodico
   period.switch_do_period(event_period)

10. **Utilizzo della Classe per Inserire Eventi nel Diario**
   
   ```sh
   
   pdated_diary = put_event_diary(existing_or_new_diary, event)

11. **Utilizzo del modulo diary_txt**
Consente di stampare tutti gli eventi inseriti nel diario in un documento .txt
   
   ```sh
   converted_str = convert_diary_str()

12. **Utilizzo del modulo diary_excell**
Consente di creare un file xlsx per registrare tutti gli eventi inseriti nel diario
   
   ```sh
   diary.diary_excel.save_diary_excel('excel_angelo.xlsx',d.diary)

13. **Ordinamento eventi diario per nome o per data**
   ```sh
   import diary_DB
   
   connection = diary.diary.diary_DB.create_connection('localhost', 'Diary', 'root', 'root')
   order = 'crescente'
   list_events = read_events_DB(connection, id_diary=None)
   list_events = orderby_startdata(list_events, order)


