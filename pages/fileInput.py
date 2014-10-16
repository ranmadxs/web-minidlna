#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import cgi

dirName = os.path.dirname(__file__)
path, lastDir = os.path.split(dirName)

sys.path.append(path)

from mako.lookup import TemplateLookup
from module.config import Dlna
from module.fileSvc import FileSvc 

print "Content-Type: text/html; charset=UTF-8"
print ""

lookup = TemplateLookup(directories=['../webapp/templates'], input_encoding='utf-8', output_encoding='utf-8')
template = lookup.get_template("fileInput.mako")
model = {}

dlna = Dlna()
listMediaDir = dlna.getMediaDir()
model["mediaFile"] = None
model["file"] = ''
model["mediaDir"] = None
print "Revisando el post"
form   = cgi.FieldStorage()
if(form.length > 0):
    model["file"] = form.getfirst("file").strip()
    mediaDir = form.getfirst("mediaDir")
    model["mediaDir"] = mediaDir
    archivo = form.getfirst("file").strip()
    path = mediaDir + "/" +  archivo
    print path
    
    fileSvc = FileSvc()
    mimeVO = fileSvc.getMimeFile(path)
    
    print mimeVO
    model["mediaFile"] = path


print template.render(model = model, listMediaDir = listMediaDir)
