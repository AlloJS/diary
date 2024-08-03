try:
    from .diary_except import ErrorDate  # Importazione relativa per Sphinx
except ImportError:
    from diary_except import ErrorDate   # Importazione assoluta per l'esecuzione normale

import datetime
import calendar
from dateutil import tz

def daily_note(year, month, day, description, do):
    """
    Crea una voce di diario per una data specifica.

    :param year: Anno della data del diario.
    :type year: int
    :param month: Mese della data del diario (1-12).
    :type month: int
    :param day: Giorno della data del diario (1-31).
    :type day: int
    :param description: Descrizione della voce del diario.
    :type description: str
    :param do: Stato della voce del diario (True o False).
    :type do: bool
    :return: Un dizionario che rappresenta la voce del diario, contenente la data formattata, la descrizione, lo stato e il calendario del mese.
    :rtype: dict
    :raises ErrorDate: Se il mese o il giorno non sono validi.
    """
    try:
        if month not in range(1, 13):
            raise ErrorDate('Il mese non è valido.')

        if day not in range(1, 32):
            raise ErrorDate('Il giorno non è valido.')

        time_zone = tz.gettz('Europe/Paris')
        d_d = datetime.datetime(year, month, day, tzinfo=time_zone)
        date_diary = datetime.datetime.strftime(d_d, '%Y-%m-%d %H:%M:%S')
        obj_diary = {
            'date': date_diary,
            'description': description,
            'do': do,
            'calendar': calendar.month(year, month)
        }
        return obj_diary
    except ErrorDate as ed:
        print(ed.message)

def modify_daily_date(obj_daily, year, month, day):
    """
    Modifica la data di una voce di diario esistente.

    :param obj_daily: Oggetto della voce del diario da modificare.
    :type obj_daily: dict
    :param year: Nuovo anno da impostare.
    :type year: int
    :param month: Nuovo mese da impostare (1-12).
    :type month: int
    :param day: Nuovo giorno da impostare (1-31).
    :type day: int
    :return: L'oggetto della voce del diario modificato.
    :rtype: dict
    :raises ErrorDate: Se il mese o il giorno non sono validi.
    """
    try:
        if month not in range(1, 13):
            raise ErrorDate('Il mese non è valido.')

        if day not in range(1, 32):
            raise ErrorDate('Il giorno non è valido.')

        time_zone = tz.gettz('Europe/Paris')
        d_d = datetime.datetime(year, month, day, tzinfo=time_zone)
        date_diary = datetime.datetime.strftime(d_d, '%Y-%m-%d %H:%M:%S')
        obj_daily['calendar'] = calendar.month(year, month)
        obj_daily['date'] = date_diary
        return obj_daily
    except ErrorDate as ed:
        print(ed.message)

def modify_description_daily(obj_daily, description):
    """
    Modifica la descrizione di una voce di diario esistente.

    :param obj_daily: Oggetto della voce del diario da modificare.
    :type obj_daily: dict
    :param description: Nuova descrizione da impostare.
    :type description: str
    :return: L'oggetto della voce del diario modificato.
    :rtype: dict
    """
    obj_daily['description'] = description
    return obj_daily

def switch_do_daily(obj_daily):
    """
    Cambia lo stato 'do' di una voce di diario (da True a False o viceversa).

    :param obj_daily: Oggetto della voce del diario da modificare.
    :type obj_daily: dict
    :return: L'oggetto della voce del diario modificato con lo stato 'do' aggiornato.
    :rtype: dict
    """
    obj_daily['do'] = not obj_daily['do']
    return obj_daily

def convert_daily_to_string(obj_daily):
    """
    Converte una voce di diario in una stringa formattata.

    :param obj_daily: Oggetto della voce del diario da convertire.
    :type obj_daily: dict
    :return: Una stringa che rappresenta la voce del diario.
    :rtype: str
    """
    str_daily = (
        f"{obj_daily['calendar']}\n"
        f"{obj_daily['date']}:\n{obj_daily['description']}\n"
        f"Do: {obj_daily['do']}"
    )
    return str_daily
