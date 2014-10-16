'''
Created on 31-07-2013

@author: esanchez
'''

from model import AbstractUtilDTO

# 5448|2$8$6AF|2$8|64$4$1C$2$B|item.videoItem|1881|True Blood 5x12 - Save Yourself
class OBJECTS(AbstractUtilDTO):
    ID                      = None
    OBJECT_ID               = None
    PARENT_ID               = None
    REF_ID                  = None
    CLASS                   = None # container.storageFolder item.videoItem    
    DETAIL_ID               = None
    NAME                    = None

# 1881|/home/pi/media/wd/Series/True Blood/Season 5/True Blood 5x12 - Save Yourself.mp4|549392510|1361456765|True Blood 5x12 - Save Yourself|0:55:13.152|165821|48000||||||2|||2013-02-21T14:26:05|720x404|0|1178||AVC_MP4_HP_HD_AAC|video/mp4
class DETAILS(AbstractUtilDTO):
    ID                      = None
    PATH                    = None
    SIZE                    = None
    TIMESTAMP               = None
    TITLE                   = None
    DURATION                = None
    BITRATE                 = None
    SAMPLERATE              = None
    CREATOR                 = None
    ARTIST                  = None
    ALBUM                   = None
    GENRE                   = None
    COMMENT                 = None
    CHANNELS                = None
    DISC                    = None
    TRACK                   = None
    DATE                    = None
    RESOLUTION              = None
    THUMBNAIL               = 0
    ALBUM_ART               = 0
    ROTATION                = None
    DLNA_PN                 = None
    MIME                    = None

# 1178|/home/pi/db/minidlna/art_cache/home/pi/media/wd/Series/True Blood/Season 5/folder.jpg
class ALBUM_ART(AbstractUtilDTO):
    ID                      = None
    PATH                    = None

# 1881|/home/pi/media/wd/Series/True Blood/Season 5/True Blood 5x12 - Save Yourself.srt
# Obs: al parecer el mismo ID que se usa en DETAILS SE OCUPA EN CAPTIONS    
class CAPTIONS(AbstractUtilDTO):
    ID                      = None
    PATH                    = None
    
    