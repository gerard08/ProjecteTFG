USERNAME = 'gery08'
PASSWORD = 'TFG2021_22'

from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt

api = SentinelAPI(USERNAME, PASSWORD, 'https://scihub.copernicus.eu/dhus',show_progressbars=True)
footprint = geojson_to_wkt(read_geojson('busca.geojson'))
products = api.query(footprint,
                     date = ("20171001","20171030"),
                     platformname = 'Sentinel-2',
                     cloudcoverpercentage = '[0 TO 100]')

                     
print(len(products))
api.to_geojson(products)
api.download_all(products[next(iter(products))])
