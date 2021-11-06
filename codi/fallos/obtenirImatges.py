ACCESSTOKEN = 'pk.eyJ1IjoiZ2VyeTA4IiwiYSI6ImNrdjVoNmE3MTJuZHMybnF3ajk0b3ZjeDkifQ.-p3dmIniwRQqoJelI55bgg'

import os
import requests # The requests package allows use to call URLS
import shutil   # shutil will be used to copy the image to the local

os.system("pip install -r requirements.txt")
os.chdir('C:/Users/ger-m/Desktop/UNI/4t/TFG/codi')
# os.mkdir('satellite_images')
# os.mkdir('elevation_images')
# os.mkdir('composite_images')

lat_lng = [43.640918, -79.371478]

delta=0.05
tl = [lat_lng[0]+delta, lat_lng[1]-delta]
br = [lat_lng[0]-delta, lat_lng[1]+delta]
z = 15 # Set the resolution (max at 15)

# find the tile set IDs (x/y) for the top left and bottom right at the zoom level
import mercantile
tl_tiles = mercantile.tile(tl[1],tl[0],z)
br_tiles = mercantile.tile(br[1],br[0],z)

x_tile_range = [tl_tiles.x,br_tiles.x];print(x_tile_range)
y_tile_range = [tl_tiles.y,br_tiles.y];print(y_tile_range)

# Loop over the tile ranges
for i,x in enumerate(range(x_tile_range[0],x_tile_range[1]+1)):
  for j,y in enumerate(range(y_tile_range[0],y_tile_range[1]+1)):
   # Call the URL to get the image back
   r = requests.get('https://api.mapbox.com/v4/mapbox.terrain-rgb/'+str(z)+'/'+str(x)+'/'+str(y)+'@2x.pngraw?access_token=' + ACCESSTOKEN, stream=True)
   # Next we will write the raw content to an image
   with open('./elevation_images/' + str(i) + '.' + str(j) + '.png', 'wb') as f:
       r.raw.decode_content = True
       shutil.copyfileobj(r.raw, f) 
   # Do the same for the satellite data
   r =requests.get('https://api.mapbox.com/v4/mapbox.satellite/'+ str(z)+'/'+str(x)+'/'+str(y)+'@2x.pngraw?' + ACCESSTOKEN, stream=True)
   with open('./satellite_images/' + str(i) + '.' + str(j) + '.png', 'wb') as f:
       r.raw.decode_content = True
       shutil.copyfileobj(r.raw, f)



# Import the image, math and os libraries
from PIL import Image
import math
from os import listdir
from os.path import isfile, join
# Loop over the elevation and satellite image set
for img_name in ['elevation','satellite']:
   # Make a list of the image names   
   image_files = ['./' + img_name + '_images/' + f for f in listdir('./' + img_name + '_images/')]
    # Open the image set using pillow
   images = [Image.open(x) for x in image_files]
   # Calculate the number of image tiles in each direction
   edge_length_x = x_tile_range[1] - x_tile_range[0]
   edge_length_y = y_tile_range[1] - y_tile_range[0]
   edge_length_x = max(1,edge_length_x)
   edge_length_y = max(1,edge_length_y)
   # Find the final composed image dimensions  
   width, height = images[0].size
   total_width = width*edge_length_x
   total_height = height*edge_length_y
   # Create a new blank image we will fill in
   composite = Image.new('RGB', (total_width, total_height))
   # Loop over the x and y ranges
   y_offset = 0
   for i in range(0,edge_length_x):
     x_offset = 0
     for j in range(0,edge_length_y):
        # Open up the image file and paste it into the composed image at the given offset position
        tmp_img = Image.open('./' + img_name + '_images/' + str(i) + '.' + str(j) + '.png')
        composite.paste(tmp_img, (y_offset,x_offset))
        x_offset += width # Update the width
     y_offset += height # Update the height
# Save the final image
composite.save('./composite_images/' + img_name + '.png')