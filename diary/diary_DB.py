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
        self.id_diary = 1

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
        query = "INSERT INTO Event (univoc_id,name,description,date_start,date_and,do,repeat_event,calendar) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = list()
        cursor = conn.cursor()

        try:
            list_diary = self.read_events_DB()
            check_univoc_id = list(map(lambda x: x['univoc_id'], list_diary))

            for event in self.diary:
                #Creo lista per dati
                if str(event['univoc_id']) not in check_univoc_id:
                    values.append(str(event['univoc_id']))
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
        camp = ['id','univoc_id','name','description','date start','date and','do','repeat','calendar']
        list_event = [row for row in rows]
        dict_event = {}
        list_diary = []

        for evnet in list_event:
            dict_event['id'] = evnet[0]
            dict_event['univoc_id'] = evnet[1]
            dict_event['name'] = evnet[2]
            dict_event['description'] = evnet[3]
            dict_event['date start'] = evnet[4]
            dict_event['date and'] = evnet[5]
            dict_event['do'] = evnet[6]
            dict_event['repeat'] = evnet[7]
            dict_event['calendar'] = evnet[8]
            list_diary.append(dict_event)
            dict_event = {}

        cursor.close()
        conn.close()
        return list_diary




