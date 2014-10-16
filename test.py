from model.vo import MimeVO
from module.fileSvc import FileSvc
import os
from os.path import basename
from module.dbConnect import DetailsSvc
from model.entity import DETAILS


#print parseFile.video

fileSvc = FileSvc()
file = "/home/esanchez/naruto.mp4"
mimeVO = fileSvc.getMimeFile(file)

print mimeVO
print "===================================================="
fileFullName = os.path.basename(file)
print fileFullName
print os.path.splitext(fileFullName)[0]
print os.path.splitext(fileFullName)[-1]

print "===================================================="

#Se busca primero en DETAILS POR NOMBRE DE ARCHIVO, SI NO SE ENCUENTRA SE BUSCA LA CARPETA, SI NO SE ENCUENTRA SE EMPIESA A DESARMAR EL DIRECTORIO


print file

dirName = os.path.dirname(file)
print dirName

#os.path.

path, lastDir = os.path.split(dirName)
print path



#sys.path.append(path)

print "================================================="
details = DETAILS()
details.PATH = "/home/pi/media/wd/Anime/American Dad/Season 2/American Dad - S02E01 - Camp Refoogee.avi"
detailSvc = DetailsSvc()
details = detailSvc.getDetails(details)
print details
#for video in mimeVO.video:
#    print video.length



