from .new_diary import Diary
import mysql.connector
from mysql.connector import Error
from .generator_UID import _generate_random_id
from datetime import datetime
class DiarySQL(Diary):
    def __init__(self,name,host,database,user,password):
        super().__init__(name)
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.id_diary = _generate_random_id()
        self.write_DB_diary_creation()

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

    def write_DB_diary_creation(self):
        """
        Crea la riga diario su database con il suo codice univoco
        :return: None
        """
        try:
            conn = self._create_connection()
            query = "INSERT INTO Diary (id_diary,name,data_creation) VALUES (%s,%s,%s)"
            values = list()
            cursor = conn.cursor()
            list_diary = self.read_is_diary_exsist()
            check_univoc_id = list(map(lambda x: x['id_diary'], list_diary))
            date_creation_str = self.date_creation.strftime("%Y-%m-%d %H:%M:%S")
            date_creation_datetime = datetime.fromisoformat(date_creation_str)
            date_creation_formattata = date_creation_datetime.strftime("%Y-%m-%d %H:%M:%S")

            if self.id_diary not in check_univoc_id:
                values.append(str(self.id_diary))
                values.append(str(self.name))
                values.append(str(date_creation_formattata))
                values = tuple(values)
                cursor.execute(query, values)
                conn.commit()
                values = list()
            else:
                print(f'Queesto diario {self.name} con id univoco {self.id_diary} risulta già inserito in Data Base')

        except Error as e:
            print("Scrittura non effettuata",e)

    def read_is_diary_exsist(self):
        """
        Legge per verificare se un diario è gia stato registrato
        :return: Ritorna la lista di tutti gli id univoci esistenti in database
        """
        conn = self._create_connection()
        cursor = conn.cursor()
        query = "SELECT id_diary FROM Diary"
        cursor.execute(query)
        rows = cursor.fetchall()
        list_diaries = [row for row in rows]
        dict_diary = {}
        list_diary = []

        for diary in list_diaries:
            dict_diary['id_diary'] = diary[0]

        cursor.close()
        conn.close()
        return list_diary

    def write_events_DB(self):
        """
        Metodo che consente di scrivere l'intero diario sul DB
        :return: Ritorna la riuscita della scrittura in database
        """
        conn = self._create_connection()
        query = "INSERT INTO Event (univoc_id,id_diary,name,description,date_start,date_and,do,repeat_event,calendar) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = list()
        cursor = conn.cursor()

        try:
            list_diary = self.read_events_DB()
            check_univoc_id = list(map(lambda x: x['univoc_id'], list_diary))

            for event in self.diary:
                #Creo lista per dati
                if str(event['univoc_id']) not in check_univoc_id:
                    values.append(str(event['univoc_id']))
                    values.append(str(event['id_diary']))
                    values.append(event['name'])
                    values.append(event['description'])
                    values.append(event['date start'])
                    values.append(event['date start'])
                    values.append(event['do'])
                    values.append(0)
                    values.append(event['calendar'][0])
                    #Trasformo tupla per passare dati al cursore
                    values = tuple(values)
                    cursor.execute(query,values)
                    conn.commit()
                    values = list()
                else:
                    print(f'Queesto evento {event['name']} con id univoco {event['univoc_id']} risulta già inserito in Data Base')

            print('Record inserito con successo')
        except Error as e:
            print("Scrittura non effettuata",e)

    def read_events_DB(self):
        conn = self._create_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Event"
        cursor.execute(query)
        rows = cursor.fetchall()
        list_event = [row for row in rows]
        dict_event = {}
        list_diary = []

        for evnet in list_event:
            dict_event['id'] = evnet[0]
            dict_event['univoc_id'] = evnet[1]
            dict_event['id_diary'] = evnet[2]
            dict_event['name'] = evnet[3]
            dict_event['description'] = evnet[4]
            dict_event['date start'] = evnet[5]
            dict_event['date and'] = evnet[6]
            dict_event['do'] = evnet[7]
            dict_event['repeat'] = evnet[8]
            dict_event['calendar'] = evnet[9]
            list_diary.append(dict_event)
            dict_event = {}

        cursor.close()
        conn.close()
        return list_diary




