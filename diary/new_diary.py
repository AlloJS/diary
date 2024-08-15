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

    def convert_diary_str(self):
        """
        Converte il diario in una stringa.
        :return: Diario in una stringa.
        """
        str_diary = ''
        for event in self.diary:
            try:
                data_start_parsed = datetime.datetime.strptime(event['date start'],'%Y-%m-%d %H:%M:%S')
                dsf = datetime.datetime.strftime(data_start_parsed,'%d %B %Y %H:%M:%S')
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


