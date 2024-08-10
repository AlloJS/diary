import datetime
from dateutil import tz
from diary.diary_except import ErrorAllowedValue

class Diary:
    """
    Costruzione di un nuovo diario per la registrazione degli eventi

    """
    def __init__(self,name):
        """
        Costruttore per nominare un diario

        :param name: Nome da assegnare al diario
        :type str
        """
        self.name = name
        self.diary = []
        self.date_creation = self._set_data_creation()

    def __str__(self):
        """

        :return: Riporta una stringa con il nome e la data di creazione del diario
        """
        return f'New diary {self.name} created:{self.date_creation}'

    def _set_data_creation(self):
        """
        Settaggio automatico della data di creazione

        :return: Ritorna data di creazione del diario
        """
        time_zone = tz.gettz('Europe/Paris')
        self.date_creation = datetime.datetime.now(tz=time_zone)
        return self.date_creation

    def put_event_diary(self,event):
        """
        Inserimento eventi nel diario

        :param event: Oggetto evento da inserrire nel diario

        :return: Ritorna il diario con l'oggetto inserito alla fine degli altri eventi esistenti
        """
        self.diary.append(event)
        return self.diary

    def _parse_date(self, date_str):
        """
        Tenta di parsificare una data in base a diversi formati possibili.
        :param date_str: La data come stringa
        :return: L'oggetto datetime parsificato
        """
        date_formats = [
            "%Y-%m-%d %H:%M:%S",  # Formato 'YYYY-MM-DD HH:MM:SS'
            "%d-%m-%Y %H:%M:%S",  # Formato 'DD-MM-YYYY HH:MM:SS'
            "%d %m %Y %H:%M:%S",  # Formato 'DD MM YYYY HH:MM:SS'
            "%Y-%m-%d",            # Formato 'YYYY-MM-DD'
            "%d-%m-%Y",            # Formato 'DD-MM-YYYY'
            "%d %m %Y"             # Formato 'DD MM YYYY'
        ]
        for fmt in date_formats:
            try:
                return datetime.datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        raise ValueError(f"Formato della data non riconosciuto: {date_str}")

    def convert_diary_str(self):
        """
        Converte il diario in una stringa.
        :return: Diario in una stringa.
        """
        str_diary = ''
        for event in self.diary:
            try:
                data_start_parsed = self._parse_date(event['date start'])
                data_and_parsed = self._parse_date(event['date and'])
            except ValueError as e:
                print(e)
                continue

            do = 'Fatto' if event['do'] else 'Da svolgere'

            str_diary += (
                f"PERIODO: dal: {data_start_parsed.strftime('%d-%B-%Y %H:%M:%S')} "
                f"al: {data_and_parsed.strftime('%d-%B-%Y %H:%M:%S')}\n"
                f"NOME: {event['name']}\n"
                f"DESCRIZIONE: {event['description']}\n"
                f"SVOLTO: {do}\n"
                f"-------------------------------------------\n"
            )

        return str_diary

    def orderby_startdata(self,order):
        """
        Riordina il diario in ordine di data
        :param order: Può essere crescente o decrescente
        :return: Restitusce l'oggetto diario in ordine di cronologia di data
        """
        try:

            if order == 'crescente':
                verse = True
            elif order == 'decrescente':
                verse = False
            else:
                raise ErrorAllowedValue('I valori consentiti sono solo crescente o decrescente')

            self.diary = list(sorted(self.diary,key=lambda x: x['date start'],reverse=verse))
            return self.diary

        except ErrorAllowedValue as err:
            print(err.message)

    def orderby_name_event(self,order):
        """

        Riordina il diario in ordine in base al nome
        :param order: Può essere crescente o decrescente
        :type order: str
        :return: Restitusce l'oggetto diario in ordine per nome
        """

        try:
            if order == 'crescente':
                verse = True
            elif order == 'decrescente':
                verse = False
            else:
                raise ErrorAllowedValue('I valori consentiti sono solo crescente o decrescente')

            self.diary = list(sorted(self.diary,key=lambda x: x['name'].lower(),reverse=verse))
            return self.diary

        except ErrorAllowedValue as err:
            print(err.message)


