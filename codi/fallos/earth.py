import ee


def initialize():

    ee.Authenticate()
    ee.Initialize()

def obtenirElevacio():
    # Print the elevation of Mount Everest.
    dem = ee.Image('USGS/SRTMGL1_003')
    xy = ee.Geometry.Point([86.9250, 27.9881])
    elev = dem.sample(xy, 30).first().get('elevation').getInfo()
    print('Mount Everest elevation (m):', elev)
    uab = ee.Geometry.Point([2.10523, 41.50116])
    elev = dem.sample(uab, 30).first().get('elevation').getInfo()
    print('UAB elevation (m):', elev)

    return dem

def obtenirImatge(dem):
# Load a Landsat image.
    img = ee.Image('LANDSAT/LT05/C01/T1_SR/LT05_034033_20000913')

    # Print image object WITHOUT call to getInfo(); prints serialized request instructions.
    print(img)

    # Print image object WITH call to getInfo(); prints image metadata.
    print(img.getInfo())

initialize()
dem = obtenirElevacio()
obtenirImatge(dem)