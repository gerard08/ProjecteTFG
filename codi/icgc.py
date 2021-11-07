import requests
from pyproj import Proj, transform

def calculateCoord(xy0, xy1):
    sat = Proj('EPSG:25831')
    maps = Proj('EPSG:4326')

    nxy0 = transform(maps, sat, xy0[0], xy0[1])
    nxy1 = transform(maps, sat, xy1[0], xy1[1])

    return nxy0, nxy1


def getImage(x0, y0, x1, y1, width, height, type = None):
    url = ''
    if type == 'relleu':
        url = 'https://geoserveis.icgc.cat/icgc_mdt2m/wms/service?REQUEST=GetMap&SERVICE=WMS&VERSION=1.3.0&LAYERS=MET2m&STYLES=&FORMAT=image/png&BGCOLOR=0xFFFFFF&TRANSPARENT=FALSE&CRS=EPSG:25831&BBOX='
    else:
        url = 'https://geoserveis.icgc.cat/icgc_sentinel2/wms/service?REQUEST=GetMap&SERVICE=WMS&VERSION=1.3.0&LAYERS=sen2rgb_202012&STYLES=&FORMAT=image/jpeg&BGCOLOR=0xFFFFFF&TRANSPARENT=TRUE&CRS=EPSG:25831&BBOX='
    #url = 'https://www.ign.es/wms-inspire/pnoa-ma?REQUEST=GetMap&VERSION=1.1.0&SERVICE=WMS&SRS=EPSG:25831&BBOX='
    #end = '&LAYERS=OI.OrthoimageCoverage&STYLES=&FORMAT=JPEG&BGCOLOR=0xFFFFFF&TRANSPARENT=TRUE&EXCEPTION=INIMAGE'

    query = url + str(x0) + ',' + str(y0) + ',' + str(x1) + ',' + str(y1) + '&WIDTH=' + str(width) + '&HEIGHT=' + str(height)
    x = requests.get(query)

    print(x)
    return x.content