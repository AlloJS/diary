try:
    from .diary_except import ErrorDate  # Importazione relativa per Sphinx
except ImportError:
    from diary_except import ErrorDate   # Importazione assoluta per l'esecuzione normale

import datetime
import calendar
from dateutil import tz

def get_period_from(year,month,day,hour,minute)->dict:
    """
    Creazione del dict periodo di partenza
    :param year: Anno del periodo di partenza
    :type year int
    :param month: Mese del periodo di partenza
    :type month int
    :param day: Giorno del periodo di partenza
    :type day int
    :param hour: Ora del periodo di partenza
    :type hour int
    :param minute: Minuti del periodo di partenza
    :type minute int
    :return: Ritora un dict del periodo di partenza
    """
    try:
        if month not in range(1,13):
            raise ErrorDate('Il mese non è valido.')

        if day not in range(1, 32):
            raise ErrorDate('Il giorno non è valido.')

        if hour not in range(0,25):
            raise ErrorDate('Le ore non sono valide.')

        if minute not in range(0,60):
            raise ErrorDate('I minuti non sono validi.')

        period_from = {'year':year,'month':month,'day':day,'hour':hour,'minute':minute}
        return period_from
    except ErrorDate as ed:
        print(ed.message)

def get_period_to(year,month,day,hour,minute)->dict:
    """
    Creazione del dict periodo di fine
    :param year: Anno del periodo di fine
    :type year int
    :param month: Mese del periodo di fine
    :type month int
    :param day: Giorno del periodo di fine
    :type day int
    :param hour: Ora del periodo di fine
    :type hour int
    :param minute: Minuti del periodo di fine
    :type minute int
    :return: Ritora un dict del periodo di fine
    """
    if month not in range(1, 13):
        raise ErrorDate('Il mese non è valido.')

    if day not in range(1, 32):
        raise ErrorDate('Il giorno non è valido.')

    if hour not in range(0, 24):
        raise ErrorDate('Le ore non sono valide.')

    if minute not in range(0, 60):
        raise ErrorDate('I minuti non sono validi.')

    try:
        period_to = {'year': year, 'month': month, 'day': day,'hour':hour,'minute':minute}
        return period_to
    except ErrorDate as ed:
        print(ed.message)

def period_note(name,description,period_from: dict,period_to: dict,do):
    """
    Crea una voce di diario per un periodo specifico.
    :param name: Nome per periodo di partenza
    :type name str
    :param description: Descrizione dell'evento del periodo
    :type description str
    :param period_from: Data per periodo di partenza
    :type period_from dict
    :param period_to: Data per periodo di fine
    :type period_to dict
    :param do: Stato della voce del diario (True o False).
    :type do Bool
    :return: Ritorna un evento scelto in un certo periodo
    """
    try:
        if period_from['month'] not in range(1, 13) and period_to['month'] not in range(1, 13):
            raise ErrorDate('Il mese non è valido.')

        if period_from['day'] not in range(1, 32) and period_to['day'] not in range(1, 32):
            raise ErrorDate('Il giorno non è valido.')

        if period_from['hour'] not in range(0, 24) and period_to['hour'] not in range(0, 24):
            raise ErrorDate('L\'ora non è valida.')

        if period_from['minute'] not in range(0, 60) and period_to['minute'] not in range(0, 60):
            raise ErrorDate('I minuti non sono validi.')

        time_zone = tz.gettz('Europe/Paris')
        date_from = datetime.datetime(period_from['year'],period_from['month'],period_from['day'],period_from['hour'],period_from['minute'],tzinfo=time_zone)
        date_from_format = datetime.datetime.strftime(date_from,'%d %B %Y %H:%M:%S')
        date_to = datetime.datetime(period_to['year'], period_to['month'], period_to['day'], period_to['hour'], period_to['minute'], tzinfo=time_zone)
        date_to_format = datetime.datetime.strftime(date_to,'%d %B %Y %H:%M:%S')
        calendar_period = []

        if period_from['year'] == period_to['year']:
            calendar_period = [calendar.month(period_from['year'], month) for month in range(period_from['month'],period_to['month'] + 1)]
        else:
            for year in range(period_from['year'], period_to['year'] + 1):
                if year == period_from['year']:
                    for month in range(period_from['month'],13):
                        calendar_period.append(calendar.month(year,month))

                if year != period_to['year'] and year != period_from['year']:
                    calendar_period.append(calendar.calendar(year))

                if year == period_to['year']:
                    for month in range(1,period_to['month']+1):
                        calendar_period.append(calendar.month(year, month))


        obj_period = {
            'name': name,
            'description': description,
            'date start': date_from_format,
            'date and': date_to_format,
            'do': do,
            'repeat': False,
            'calendar': calendar_period
        }

        return obj_period

    except ErrorDate as ed:
        print(ed.message)