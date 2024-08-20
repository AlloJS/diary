import datetime
from dateutil import tz
try:
    from generator_UID import _generate_random_id
    from diary_except import ErrorAllowedValue
except ImportError:
    from .generator_UID import _generate_random_id
    from .diary_except import ErrorAllowedValue

def _set_data_creation():
    """
    Settaggio automatico della data di creazione
    :return: Ritorna data di creazione del diario
    """
    time_zone = tz.gettz('Europe/Paris')
    return datetime.datetime.now(tz=time_zone)


def create_diary(name):
    """
    Crea un nuovo diario con nome e altre informazioni base.
    :param name: Nome del diario.
    :return: Dizionario con le informazioni del diario.
    """
    return {
        'name': name,
        'diary': [],
        'date_creation': _set_data_creation(),
        'id_diary': _generate_random_id(),
    }


def put_event_diary(diary, event):
    """
    Inserisce un evento nel diario.
    :param diary: Il diario in cui inserire l'evento.
    :param event: L'evento da inserire.
    :return: Il diario aggiornato.
    """
    diary['diary'].append(event)
    return diary


def convert_diary_str(diary):
    """
    Converte il diario in una stringa.
    :param diary: Il diario da convertire.
    :return: Diario in una stringa.
    """
    str_diary = ''
    for event in diary['diary']:
        try:
            data_start_parsed = datetime.datetime.strptime(event['date_start'], '%Y-%m-%d %H:%M:%S')
            dsf = datetime.datetime.strftime(data_start_parsed, '%d %B %Y %H:%M:%S')
            data_and_parsed = datetime.datetime.strptime(event['date and'], '%Y-%m-%d %H:%M:%S')
            daf = datetime.datetime.strftime(data_and_parsed, '%d %B %Y %H:%M:%S')
        except ValueError as e:
            print(e)
            continue

        do = 'Fatto' if event['do'] else 'Da svolgere'

        str_diary += (
            f"PERIODO: dal: {dsf} "
            f"al: {daf}\n"
            f"NOME: {event['name']}\n"
            f"DESCRIZIONE: {event['description']}\n"
            f"SVOLTO: {do}\n"
            f"-------------------------------------------\n"
        )

    return str_diary


def orderby_startdata(diary, order):
    """
    Riordina il diario in ordine di data.
    :param diary: Il diario da ordinare.
    :param order: Può essere 'crescente' o 'decrescente'.
    :return: Il diario ordinato.
    """
    if order not in ['crescente', 'decrescente']:
        raise ErrorAllowedValue('I valori consentiti sono solo crescente o decrescente')

    reverse = True if order == 'decrescente' else False


    # Verifica che diary sia una lista di dizionari
    print(f"Tipo di 'diary': {type(diary)}")
    print(f"Contenuto di 'diary': {diary}")

    # Procedi con l'ordinamento
    diary = sorted(diary, key=lambda x: x['date_start'], reverse=reverse)
    return diary


def orderby_name_event(diary, order):
    """
    Riordina il diario in ordine in base al nome.
    :param diary: Il diario da ordinare.
    :param order: Può essere 'crescente' o 'decrescente'.
    :return: Il diario ordinato.
    """
    if order not in ['crescente', 'decrescente']:
        raise ErrorAllowedValue('I valori consentiti sono solo crescente o decrescente')

    verse = order == 'decrescente'
    diary['diary'] = sorted(diary['diary'], key=lambda x: x['name'].lower(), reverse=verse)
    return diary
