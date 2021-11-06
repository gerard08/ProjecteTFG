import requests
import io
import cv2
import numpy as np

KEY = '3JKpV0otSPCzL6Xkge82Mf1aZtQsI1wQtfAyiz6I'


def getImage(lon, lat, date = '2018-01-01', dim = 0.15):
    """Demanem imatges al servidor de la NASA

    Args:
        lon (float): longitud del satèl·lit
        lat (float): latitud del satèl·lit
        date (string): data de la imatge en format (YYYY-MM-DD)
        dim (float): Altura i amplada de la imatge en graus

    Returns:
        img(matrix): matriu de la imatge llegida amb cv2
    """
    query = ('https://api.nasa.gov/planetary/earth/imagery?lon=' + str(lon)
            + '&lat=' + str(lat) + '&date=' + date + '&dim=' + str(dim) + '&api_key=' + KEY)
            
    r = requests.get(query)
    if r.status_code != 200: raise ValueError('Error ' + str(r.status_code) + ' en la solicitud')
    data = io.BytesIO(r.content)
    data.seek(0)
    file_bytes = np.asarray(bytearray(data.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    return img

