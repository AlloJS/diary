try:
    from .diary_except import ErrorDate  # Importazione relativa per Sphinx
except ImportError:
    from diary_except import ErrorDate   # Importazione assoluta per l'esecuzione normale

import datetime
import calendar
from dateutil import tz

def get_period_from(year,month,day)->dict:
    """
    Creazione del dict periodo di partenza

    :param year: Anno del periodo di partenza
    :param month: Mese del periodo di partenza
    :param day: Giorno del periodo di partenza
    :return: Ritora un dict del periodo di partenza
    """
    try:
        if month not in range(1,13):
            raise ErrorDate('Il mese non è valido.')

        if day not in range(1, 32):
            raise ErrorDate('Il giorno non è valido.')

        period_from = {'year':year,'month':month,'day':day}
        return period_from
    except ErrorDate as ed:
        print(ed.message)

def get_period_to(year,month,day)->dict:
    """
    Creazione del dict periodo di fine

    :param year: Anno del periodo di fine
    :param month: Mese del periodo di fine
    :param day: Giorno del periodo di fine
    :return: Ritora un dict del periodo di fine
    """
    if month not in range(1, 13):
        raise ErrorDate('Il mese non è valido.')

    if day not in range(1, 32):
        raise ErrorDate('Il giorno non è valido.')

    try:
        period_to = {'year': year, 'month': month, 'day': day}
        return period_to
    except ErrorDate as ed:
        print(ed.message)

def period_note(period_from: dict,period_to: dict,description,do):
    """
    Crea una voce di diario per un periodo specifico.
    :param period_from: Data per periodo di partenza
    :type dict
    :param period_to: Data per periodo di fine
    :type dict
    :param description: Descrizione dell'evento del periodo
    :type str
    :param do: Stato della voce del diario (True o False).
    :type Bool
    :return: Ritorna un evento scelto in un certo periodo
    """
    try:
        if period_from['month'] not in range(1, 13) and period_to['month'] not in range(1, 13):
            raise ErrorDate('Il mese non è valido.')

        if period_from['day'] not in range(1, 32) and period_to['day'] not in range(1, 32):
            raise ErrorDate('Il giorno non è valido.')

        time_zone = tz.tzutc('Europe/Paris')
        date_from = datetime.datetime(period_from['year'],period_from['month'],period_from['day'],tzinfo=time_zone)
        date_from_format = datetime.datetime.strftime(date_from)
        date_to = datetime.datetime(period_to['year'], period_to['month'], period_to['day'], tzinfo=time_zone)
        date_to_format = datetime.datetime.strftime(date_to)
        obj_period = {'period_from':date_from_format,'period_to':date_to_format,'description':description,'do':do}
        return obj_period

    except ErrorDate as ed:
        print(ed.message)