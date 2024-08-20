import mysql.connector
from mysql.connector import Error
from datetime import datetime

try:
    from new_diary import create_diary, put_event_diary
    from generator_UID import _generate_random_id
except ImportError:
    from .new_diary import create_diary, put_event_diary
    from .generator_UID import _generate_random_id

def create_connection(host, database, user, password):
    """
    Crea una connessione al database.
    :return: Connessione al database.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(e)
        return None


def start_diary(connection,name=None, id_diary=None):
    """
    Verifica se il diario esiste già nel database selezionato o crea uno nuovo.
    :param connection: Connessione al database.
    :param id_diary: Id del diario da selezionare (opzionale).
    :return: Diario esistente o uno nuovo.
    """
    if id_diary is None:
        # Crea un nuovo diario se non è fornito un id_diary
        new_diary = create_diary(name)
        write_DB_diary_creation(connection, new_diary)
        return new_diary
    else:
        # Cerca se il diario esiste nel database
        list_id_diary = read_is_diary_exist(connection)
        if id_diary not in list_id_diary:
            raise ValueError('Il diario da te cercato non esiste')

        # Se esiste, recupera il diario e i suoi eventi
        existing_diary = {
            'id_diary': id_diary,
            'name': 'Diario Esistente',  # Puoi ottenere il nome reale dal database se necessario
            'diary': read_events_DB(connection, id_diary)
        }
        return existing_diary

def read_is_diary_exist(connection):
    """
    Legge e verifica se un diario è già stato registrato.
    :param connection: Connessione al database.
    :return: Lista degli id dei diari esistenti.
    """
    cursor = connection.cursor()
    query = "SELECT id_diary FROM Diary"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return [row[0] for row in rows]


def write_DB_diary_creation(connection, diary):
    """
    Scrive un nuovo diario nel database.
    :param connection: Connessione al database.
    :param diary: Il diario da scrivere nel database.
    """
    cursor = connection.cursor()
    query = "INSERT INTO Diary (id_diary, name, data_creation) VALUES (%s, %s, %s)"
    date_creation_str = diary['date_creation'].strftime("%Y-%m-%d %H:%M:%S")
    values = (diary['id_diary'], diary['name'], date_creation_str)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()

def write_events_DB(connection, event):
    """
    Scrive gli eventi di un diario nel database.
    :param connection: Connessione al database.
    :param diary: Il diario da cui prendere gli eventi.
    """
    cursor = connection.cursor()
    query = """
        INSERT INTO Event (univoc_id, id_diary, name, description, date_start, date_and, do, repeat_event, calendar)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        event['univoc_id'],
        event['id_diary'],
        event['name'],
        event['description'],
        event['date_start'],
        event['date_and'],
        event['do'],
        event['repeat'],
        event['calendar'][0]
    )

    cursor.execute(query, values)
    connection.commit()
    cursor.close()


def read_events_DB(connection, id_diary=None):
    """
    Legge gli eventi di un diario dal database.
    :param connection: Connessione al database.
    :param id_diary: Id del diario di cui leggere gli eventi.
    :return: Lista degli eventi.
    """
    cursor = connection.cursor()
    if id_diary is None:
        query = "SELECT * FROM Event"
        cursor.execute(query)
    else:
        query = "SELECT * FROM Event WHERE id_diary = %s"
        cursor.execute(query, (id_diary,))

    rows = cursor.fetchall()
    cursor.close()

    return [
        {
            'univoc_id': row[1],
            'id_diary': row[2],
            'name': row[3],
            'description': row[4],
            'date_start': datetime.strftime(row[5],'%Y-%m-%d %H:%M:%S'),
            'date_and': datetime.strftime(row[6],'%Y-%m-%d %H:%M:%S'),
            'do': row[7],
            'repeat': row[8],
            'calendar': [row[9]]
        }
        for row in rows
    ]
