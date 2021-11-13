import requests
import cv2
import numpy as np
url = 'https://geoserveis.icgc.cat/icc_ortohistorica/wms/service?REQUEST=GetMap&VERSION=1.1.0&SERVICE=WMS&SRS=EPSG:23031&BBOX=290368.84,4538236.42,290568.28,4538436.86&WIDTH=520&HEIGHT=520&LAYERS=orto5m1994&STYLES=&FORMAT=JPEG&BGCOLOR=0xFFFFFF&TRANSPARENT=TRUE&EXCEPTION=INIMAGE'

a=requests.get(url)
nparr = np.fromstring(a.content, np.uint8)
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
cv2.imshow('hola', img)

cv2.waitKey(0)