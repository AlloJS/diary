import datetime
from dateutil import tz

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
        Converte il diario in una stringa
        :return: Diario in una stringa
        """
        str_diary = ''

        for event in self.diary:

            str_diary += (
                f"{event['date start']}-{event['date and']}\n"
                f"{event['name']}\n"
                f"{event['description']}\n"
                f"Do: {event['do']}\n"
                f"-------------------------------------------\n"
            )
            calendar_str = ''

        return str_diary
    """
    TO COMPLETE
    
    def orderby_startdata(self):
        new_diary = []
        for event in self.diary:
            #new_diary.append(map(lambda x: x['date start'], event))
            #new_diary.append(sorted(event,key=lambda x: x[0]))
            print(event['date start'])
            pass
        print(new_diary)
        self.diary = new_diary
        return self.diary
"""
