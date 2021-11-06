import ign
import dms2dec

x = 41.058622306613586
y = 0.5271303557742305

X = 292203.28
Y = 44540070.86

xy0 = (290368.84,4538236.42)
xy1 = (292203.28,4540070.86)

ixy0 = (40.968383169072574, 0.5087055414318402)
ixy1 = (40.98536182428068, 0.5298707676210743)

from pyproj import Proj, transform

sat = Proj('EPSG:25831')
maps = Proj('EPSG:4326')

answ = transform(maps, sat, ixy1[0], ixy1[1])


x = ign.getImage(xy0[0], xy0[1], xy1[0], xy1[1], 520, 520)
file = open('porfa.png', 'wb')
file.write(x)
file.close()