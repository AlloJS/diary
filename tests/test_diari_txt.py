import pytest
from unittest.mock import mock_open,patch,MagicMock
from diary.diary_txt import write_diary_on_txt,read_diary_txt
import io

def test_write_diary_on_txt():
    # Definisci il percorso e il contenuto del diario per il test
    mock_path = 'test_diary.txt'
    mock_diary_content = "Questo è il mio diario"
    # Crea un mock per open
    m = mock_open()
    # Crea un mock per BufferedWriter
    mock_buffer_writer = MagicMock(spec=io.BufferedWriter)
    # Patch sia 'open' che 'io.BufferedWriter'
    with patch('diary.open', m), patch('io.BufferedWriter', mock_buffer_writer):
        write_diary_on_txt(mock_path, mock_diary_content)
    # Verifica che 'open' sia stato chiamato con i parametri corretti
    m.assert_called_once_with(mock_path, 'wb')
    # Verifica che 'BufferedWriter' sia stato creato con il file mockato
    mock_buffer_writer.assert_called_once_with(m())
    # Verifica che il contenuto sia stato scritto correttamente
    mock_buffer_writer().write.assert_called_once_with(mock_diary_content.encode('utf-8'))
    # Verifica che 'flush' sia stato chiamato
    mock_buffer_writer().flush.assert_called_once()

def test_write_diary_on_txt_ioerror():
    # Definisci il percorso e il contenuto del diario per il test
    mock_path = 'test_diary.txt'
    mock_diary_content = "Questo è il mio diario"

    # Crea un mock per open che solleva un IOError
    m = mock_open()
    m.side_effect = IOError(2, 'No such file or directory')

    # Patch 'open' con il mock che solleva l'errore
    with patch('tua_libreria.open', m):
        write_diary_on_txt(mock_path, mock_diary_content)

    # Verifica che 'open' sia stato chiamato con i parametri corretti
    m.assert_called_once_with(mock_path, 'wb')

"""
def test_read_diary_txt:
    pass
"""
