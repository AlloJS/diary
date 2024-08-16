from unittest.mock import patch, MagicMock, call, ANY
from diary.diary_DB import DiarySQL

def normalize_sql(sql):
    """Rimuove spazi extra e ritorni a capo dalla stringa SQL per il confronto."""
    return ' '.join(sql.split())

@patch.object(DiarySQL, '_create_connection')
@patch('mysql.connector.connect')
def test_write_events_DB(mock_connect, mock_create_conn):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_create_conn.return_value = mock_conn

    diary_sql = DiarySQL(name='test', host='localhost', database='test_db', user='user', password='password')
    diary_sql.diary = [
        {
            'univoc_id': '123',
            'id_diary': '1',
            'name': 'Test Event',
            'description': 'This is a test event',
            'date start': '2024-08-15 10:00:00',
            'date and': '2024-08-15 11:00:00',
            'do': 'Test Action',
            'calendar': ['Test Calendar']
        }
    ]

    diary_sql.write_events_DB()

    print("Chiamate effettive:")
    for call in mock_cursor.execute.call_args_list:
        print(call)

    expected_calls = [
        call('SELECT id_diary FROM Diary'),
        call('INSERT INTO Diary (id_diary,name,data_creation) VALUES (%s,%s,%s)', (ANY, 'test', ANY)),
        call('SELECT * FROM Event'),
        call("""
            INSERT INTO Event (univoc_id, id_diary, name, description, date_start, date_and, do, repeat_event, calendar)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        ('123', '1', 'Test Event', 'This is a test event', '2024-08-15 10:00:00', '2024-08-15 11:00:00', 'Test Action', 0, 'Test Calendar'))
    ]

    actual_calls = [(normalize_sql(call[0]), call[1]) for call in mock_cursor.execute.call_args_list]
    expected_calls_normalized = [(normalize_sql(call[0]), call[1]) for call in expected_calls]

    for expected in expected_calls_normalized:
        assert expected in actual_calls, f"Expected call {expected} not found in actual calls"

    mock_conn.commit.assert_called_once()
