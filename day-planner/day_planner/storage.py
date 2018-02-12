import os.path as Path
import sqlite3


SQL_SELECT_ALL = " SELECT id, text_planner, it_ok, created FROM day_planner "
SQL_ADD_TASK = " INSERT INTO day_planner (text_planner) VALUES(?) "
SQL_FIND_TASK_BY_ID = " SELECT text_planner FROM day_planner WHERE id=? "
SQL_SET_NEW_TASK = " UPDATE day_planner SET text_planner=? WHERE id=? "
SQL_FIND_STATUS_BY_ID = " SELECT it_ok FROM day_planner WHERE id=? "
SQL_SET_NEW_STATUS = "UPDATE day_planner SET it_ok=? WHERE id=?"


def connect(db_name=None):
  
    if db_name is None:
        db_name = ':memory:'
    connection = sqlite3.connect(Path.join(Path.dirname(__file__),db_name))
    #
    return connection

def initialize(conn, creation_script=None):
    if creation_script is None:
        creation_script = Path.join(Path.dirname(__file__),'resources','schema.sql')
    with conn, open(creation_script) as f:
        conn.executescript(f.read())

def add_task(new_task, connection):
    with connection:
        connection.execute(SQL_ADD_TASK, (new_task,))

def return_all_rows(connection):
    with connection:
        cursor = connection.execute(SQL_SELECT_ALL)
    return cursor.fetchall()

def get_exist_task(connection, id):
    with connection:
        old_task=connection.execute(SQL_FIND_TASK_BY_ID, (id,)).fetchone()
    return old_task[0]

def set_new_text(connection, new_text, id):
    with connection:
        connection.execute(SQL_SET_NEW_TASK, (new_text, id,))
    return True

def get_status(connection,id):
    with connection:
        old_status=connection.execute(SQL_FIND_STATUS_BY_ID, (id,)).fetchone()
    return old_status[0]

def set_new_status(connection, new_status,id):
    with connection:
        connection.execute(SQL_SET_NEW_STATUS, (new_status, id,))
    return True