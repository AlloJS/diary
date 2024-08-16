try:
    from .diary_except import ErrorDate  # Importazione relativa per Sphinx
except ImportError:
    from diary_except import ErrorDate   # Importazione assoluta per l'esecuzione normale

import datetime
import calendar
from .generator_UID import _generate_random_id

def monthly_note(name,description,year,month,do,id_diary):
    """
    Crea una voce di diario per un mese specifico.

    :param year: Anno della data del diario.
    :type year: int
    :param month: Mese della data del diario (1-12).
    :type month: int
    :param description: Descrizione della voce del diario.
    :type description: str
    :param do: Stato della voce del diario (True o False).
    :type do: bool
    :param id_diary: Id univoco riferito al diario.
    :type id_diary: str
    :return: Un dizionario che rappresenta la voce del diario, contenente il mese e l'anno formattati, la descrizione, lo stato e il calendario del mese.
    :rtype: dict
    :raises ErrorDate: Se il mese o il giorno non sono validi.
    """

    try:
        if month not in range(1, 13):
            raise ErrorDate('Il mese non è valido.')
        
        start_date = datetime.date(year,month,1)
        date_start = datetime.date.strftime(start_date,'%Y-%m-%d %H:%M:%S')
        and_date = datetime.date(year, month, calendar.monthrange(year, month)[1])
        date_and = datetime.date.strftime(and_date,'%Y-%m-%d %H:%M:%S')

        obj_monthly = {
            'univoc_id': _generate_random_id(),
            'id_diary': id_diary,
            'name': name,
            'description': description,
            'date start': date_start,
            'date and': date_and,
            'do': do,
            'repeat': False,
            'calendar': [calendar.month(year, month)]
        }

        return obj_monthly
    
    except ErrorDate as ed:
        print(ed.message)
        
def modify_monthly_month(obj_monthly,year,month):
    '''
     Modifica il mese e l'anno di una voce di diario esistente.

    :param obj_monthly: Oggetto della voce del diario da modificare.
    :type obj_monthly: dict
    :param year: Nuovo anno da impostare.
    :type year: int
    :param month: Nuovo mese da impostare (1-12).
    :type month: int
    :return: L'oggetto della voce del diario modificato.
    :rtype: dict
    :raises ErrorDate: Se il mese o il giorno non sono validi.
    '''

    try:
        if month not in range(1, 13):
            raise ErrorDate('Il mese non è valido.')
        
        start_date = datetime.date(year, month, 1)
        date_start = datetime.date.strftime(start_date, '%Y-%m-%d %H:%M:%S')
        obj_monthly['date start'] = date_start
        and_date = datetime.date(year, month, calendar.monthrange(year, month)[1])
        date_end = datetime.date.strftime(and_date, '%Y-%m-%d %H:%M:%S')
        obj_monthly['date and'] = date_end
        obj_monthly['calendar'] = [calendar.month(year, month)]
        return obj_monthly
    
    except ErrorDate as ed:
        print(ed.message)
        
def modify_monthly_description(obj_monthly,description):
    """
    Modifica la descrizione di una voce di diario mensile esistente.

    :param obj_monthly: Oggetto della voce del diario da modificare.
    :type obj_monthly: dict
    :param description: Nuova descrizione da impostare.
    :type description: str
    :return: L'oggetto della voce del diario monthly modificato.
    :rtype: dict
    """
    obj_monthly['description'] = description
    return obj_monthly

def switch_do_monthly(obj_monthly):
    """
    Cambia lo stato 'do' di una voce di diario (da True a False o viceversa).

    :param obj_monthly: Oggetto della voce del diario da modificare.
    :type obj_monthly: dict
    :return: L'oggetto della voce del diario modificato con lo stato 'do' aggiornato.
    :rtype: dict
    """

    if obj_monthly['do'] == True:
        obj_monthly['do'] = False
    else:
        obj_monthly['do'] = True
    return obj_monthly

        

