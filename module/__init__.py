import sqlite3 as lite
from module.config import Dlna
from module import constantes

def dict_factory(cursor, row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class AbstractDB:
    
    con = None
    
    def __init__(self):
        dlna = Dlna()
        db_name = dlna.getDBFile()
        self.con = lite.connect(db_name)
        self.con.row_factory = dict_factory
        
        
