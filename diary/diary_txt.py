from diary.new_diary import Diary
import os
import io
import errno
try:
    from .diary_except import ErrorDate  # Importazione relativa per Sphinx
except ImportError:
    from diary_except import ErrorDate   # Importazione assoluta per l'esecuzione normale

def write_diary_on_txt(path,my_diary_str):
    """
    Scrivi il diario su un foglio txt
    :param path: Percorso dove scrivere il testo
    :param my_diary_str: Diario da scrivere su .txt
    :return: Non ritorna nulla
    """
    try:
        with open(path,'wb') as file:
            buffer_writer = io.BufferedWriter(file)
            buffer_writer.write(my_diary_str.encode('utf-8'))
            buffer_writer.flush()
            return
    except IOError as err:
        print(os.strerror(err.errno))

def read_diary_txt(path):
    """
    Leggere file .txt di un Diario
    :param path: Percorso dove prendere il file da leggere
    :return: Stampa in console le righe del diario
    """
    try:
        with open(path,'rb') as file:
            buffer_read = io.BufferedReader(file)
            line = buffer_read.readline()
            while line:
                print(line.decode('utf-8'))
                line = buffer_read.readline()
    except IOError as err:
        print(os.strerror(err.errno))



