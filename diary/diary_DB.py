from .new_diary import Diary
import mysql.connector
from mysql.connector import Error
from .generator_UID import _generate_random_id
from datetime import datetime
class DiarySQL(Diary):
    def __init__(self,name='default',host='',database='',user='',password='',id_diary='default'):
        super().__init__(name)
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.id_diary = self.start_diary(id_diary)
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
                pass

                return connection
        except Error as e:
            print(e)

    def start_diary(self,id_diary):
        """
        Permette di cominciare e verificare se il diario esiste già nel database selezionato
        :param id_diary:
        :type str
        :return: Ri torna o l'id del diario esistente oppure ne crea uno nuovo
        """
        if id_diary == 'default':
            return _generate_random_id()
        else:
            list_id_diary = self.read_is_diary_exsist()
            is_find = True if id_diary in list_id_diary else False

            if is_find == False:
                raise ValueError('Il diario da te cercato non esiste')

            return self._select_diary_DB(id_diary)


    def _select_diary_DB(self,id_diary):
        """
        Metodo interno che seleziona l'id nella lista degli id del diario nel database
        :param id_diary:
        :type str
        :return: RItorna l'id del diario selezionato
        """
        conn = self._create_connection()
        cursor = conn.cursor()
        query = f"SELECT id_diary FROM Diary WHERE id_diary = {id_diary}"
        cursor.execute(query)
        id_diary_selectd = cursor.fetchall()
        self._charge_events(id_diary)
        return id_diary_selectd[0][0]

    def _charge_events(self, id_diary):
        """
        Carica gli eventi del diario selezionato nella variabile d'istanza
        :param id_diary: Id con cui viene individuato
        :return: RItorna la variabile di istanza popolata degli eventi associati
        """
        list_events = self.read_events_DB(id_diary)
        self.diary = list_events
        return self.diary

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
            check_univoc_id = list(map(lambda x: x, list_diary))
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
                print(f'Selezionato diario {self.name} con id univoco {self.id_diary}')

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
        list_diaries = [row[0] for row in rows]
        cursor.close()
        conn.close()
        return list_diaries

    def write_events_DB(self):
        """
        Metodo che consente di scrivere l'intero diario sul DB.
        :return: Ritorna la riuscita della scrittura in database.
        """
        conn = self._create_connection()
        query = """
            INSERT INTO Event (univoc_id, id_diary, name, description, date_start, date_and, do, repeat_event, calendar)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor = conn.cursor()

        try:
            list_diary = self.read_events_DB()
            check_univoc_id = set(map(lambda x: x['univoc_id'], list_diary))  # Usa un set per cercare più velocemente

            for event in self.diary:
                univoc_id = str(event['univoc_id'])
                if univoc_id not in check_univoc_id:
                    values = (
                        univoc_id,
                        str(event['id_diary']),
                        event['name'],
                        event['description'],
                        event['date start'],
                        event['date and'],
                        event['do'],
                        event.get('repeat_event', 0),
                        event['calendar'][0]
                    )
                    cursor.execute(query, values)
                    conn.commit()
                else:
                    print(
                        f"Questo evento '{event['name']}' con id univoco {univoc_id} risulta già inserito in Data Base")

            print('Record inseriti con successo')
        except Error as e:
            print("Scrittura non effettuata:", e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def read_events_DB(self, id_diary=None):
        conn = self._create_connection()
        try:
            cursor = conn.cursor()

            if id_diary is None:
                query = "SELECT * FROM Event"
                cursor.execute(query)
            else:
                query = "SELECT * FROM Event WHERE id_diary = %s"
                cursor.execute(query, (id_diary,))

            rows = cursor.fetchall()

            list_diary = [
                {
                    'univoc_id': row[1],
                    'id_diary': row[2],
                    'name': row[3],
                    'description': row[4],
                    'date_start': row[5],
                    'date_and': row[6],
                    'do': row[7],
                    'repeat': row[8],
                    'calendar': row[9]
                }
                for row in rows
            ]
        finally:
            cursor.close()
            conn.close()

        return list_diary




