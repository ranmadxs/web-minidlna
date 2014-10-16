#!/usr/bin/python
# -*- coding: utf-8 -*-

from mako.lookup import TemplateLookup
from module import constantes
from module.config import Dlna

print "Content-Type: text/html; charset=UTF-8"
print ""

mylookup = TemplateLookup(directories=['webapp/templates'], input_encoding='utf-8', output_encoding='utf-8')
mytemplate = mylookup.get_template("index.mako")
model = {}
model["dlnaFileConfig"] = constantes.minidlna_file_config
dlna = Dlna()
listMediaDir = dlna.getMediaDir()
model["db_dir"] = dlna.getDBFile()
print mytemplate.render(model = model, listMediaDir = listMediaDir)
