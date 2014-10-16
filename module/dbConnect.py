import sqlite3 as lite
from model.entity import OBJECTS
from model.entity import DETAILS
from module.config import Dlna
from module import AbstractDB

'''
Created on 30-06-2013

@author: esanchez
'''

class DetailsSvc(AbstractDB):
       
    def getDetails(self, details = None):
        if(details != None):
            with self.con:
                #self.con.row_factory = lite.Row
                cur = self.con.cursor()
                sql = "SELECT * FROM DETAILS WHERE PATH =:path "                
                cur.execute(sql, {"path":details.PATH})
                rows = cur.fetchone()
                if(rows == None):
                    return None                
                details = DETAILS(rows)
                return details                        
            return None        
        return None



class ObjectsSvc(object):
    
    def getObject(self, object = None):
        if(object != None):
            return None        
        return None
    