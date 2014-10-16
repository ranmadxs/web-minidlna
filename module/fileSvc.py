'''
Created on 31-07-2013

@author: esanchez
'''

from module.config import Dlna
from model.vo import MimeVO

class FileSvc(object):
    
    def getMimeFile(self, path):
        dlna = Dlna()
        if (path != None):
            mediaFile = dlna.getTypes(path)
            if(mediaFile != None):
                mimeVO = MimeVO(mediaFile.__dict__)
                return mimeVO
        return None