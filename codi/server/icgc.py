import requests
from pyproj import Proj, transform
SIZE = 2400

def calculaImatge(x, y, step, direction):
    xy0 = (x,y)
    xy1 = (x+step, y)
    if direction:
        xy1 = (x, y+step)
    
    (xy0,xy1) = calculateCoord(xy0, xy1)
    return getImage(xy0[0], xy0[1], xy1[0], xy1[1], SIZE, SIZE)


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
        url = 'https://geoserveis.icgc.cat/icgc_sentinel2/wms/service?REQUEST=GetMap&SERVICE=WMS&VERSION=1.3.0&LAYERS=sen2rgb_201608&STYLES=&FORMAT=image/jpeg&BGCOLOR=0xFFFFFF&TRANSPARENT=TRUE&CRS=EPSG:25831&BBOX='
    
    query = url + str(x0) + ',' + str(y0) + ',' + str(x1) + ',' + str(y1) + '&WIDTH=' + str(width) + '&HEIGHT=' + str(height)
    try:
        x = requests.get(query)
        return x.content
    except:
        print("ERROR")

def getImageHD(x0, y0, x1, y1, width, height, _ = None):
    url = 'https://geoserveis.icgc.cat/icc_ortohistorica/wms/service?REQUEST=GetMap&VERSION=1.1.0&SERVICE=WMS&SRS=EPSG:23031&BBOX='
    end = '&LAYERS=orto25c2016&STYLES=&FORMAT=JPEG&BGCOLOR=0xFFFFFF&TRANSPARENT=TRUE&EXCEPTION=INIMAGE'
    query = url + str(x0) + ',' + str(y0) + ',' + str(x1) + ',' + str(y1) + '&WIDTH=' + str(width) + '&HEIGHT=' + str(height) + end

    x = requests.get(query)

    #print(x)
    return x.content