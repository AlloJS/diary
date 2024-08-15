from .new_diary import Diary
import mysql.connector
from mysql.connector import Error

class DiarySQL(Diary):
    def __init__(self,name,host,database,user,password):
        super().__init__(name)
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def _create_connection(self):
        """
        Metodo interno per creare connession con il DB
        :return: Ritorna la connesssione con il DB
        """
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if connection.is_connected():
                print("Connessione al database MySQL avvenuta con successo")

                return connection
        except Error as e:
            print(e)

    def write_events_DB(self):
        """
        Metodo che consente di scrivere l'intero diario sul DB
        :return: Ritorna la riuscita della scrittura in database
        """
        conn = self._create_connection()
        query = "INSERT INTO Event (name,description,date_start,date_and,do,repeat_event,calendar) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values = list()
        cursor = conn.cursor()

        try:
            for event in self.diary:
                #Formatto data per scrivere in DB
                data_start_parsed = self._parse_date(event['date start'])
                data_and_parsed = self._parse_date(event['date and'])
                #Creo lista per dati
                values.append(event['name'])
                values.append(event['description'])
                values.append(data_start_parsed.strftime('%Y-%m-%d %H:%M:%S'))
                values.append(data_and_parsed.strftime('%Y-%m-%d %H:%M:%S'))
                values.append(event['do'])
                values.append(0)
                values.append(event['calendar'][0])
                #Trasformo tupla per passare dati al cursore
                values = tuple(values)
                cursor.execute(query,values)
                conn.commit()
                values = list()
            print('Record inserito con successo')
        except Error as e:
            print("Scrittura non effettuata",e)




