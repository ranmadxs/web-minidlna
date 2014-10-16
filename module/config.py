import enzyme
import os
from module import constantes
from model.vo import MediaDirVO


'''
Created on 01-07-2013

@author: esanchez
'''


class Dlna(object):
    
    def getMediaDir(self): 
        listMediaDir = []        
        i = 0
        f = open(constantes.minidlna_file_config, 'r')
        for line in f:            
            if ("media_dir" in line) and (line.index("media_dir") == 0):                
                media_dir = line.split("=")
                mediaDir = MediaDirVO()
                auxMediaDir = media_dir[1].split(",")
                mediaDir.tipo = auxMediaDir[0]
                mediaDir.path = auxMediaDir[1].strip()
                listMediaDir.append(mediaDir)
                i = i + 1               
        return listMediaDir
    
    def getDBDir(self):
        f = open(constantes.minidlna_file_config, 'r')
        for line in f:
            if ("db_dir" in line) and (line.index("db_dir") == 0):
                db_dir = line.split("=")
                return str(db_dir[1]).strip()                 
        return None   
    
    def getDBFile(self):
        return self.getDBDir() + os.sep + constantes.minidlna_db_file_name
    
    def getTypes(self, path):
        try:
            parseFile = enzyme.parse(path)
            return parseFile
        except ValueError:
            return None 